#!/usr/bin/env python3
"""Local web page for the KVA coordination channel (.coord/, branch `coord`).

    python3 scripts/coord_web.py            # then open http://localhost:8765
    python3 scripts/coord_web.py 9000       # other port

Shows: sync state vs origin/coord, messages, agents' status, SITUAZIONE/TASKS.
Actions: Sync now, send a message (to all or one person).
Standard library only. Listens on 127.0.0.1 only. Never reads .env.
"""
import html
import subprocess
import sys
import urllib.parse
from datetime import datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CO = ROOT / ".coord"
COORD_SH = ROOT / "scripts" / "coord.sh"
PEOPLE = ["filippo", "giorgia", "sian"]
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8765


def run(args, cwd=ROOT, timeout=60):
    try:
        p = subprocess.run(args, cwd=cwd, capture_output=True, text=True, timeout=timeout)
        return p.returncode, (p.stdout + p.stderr).strip()
    except Exception as e:  # noqa: BLE001
        return 1, str(e)


def me():
    f = ROOT / ".coord-me"
    return f.read_text().strip() if f.exists() else "?"


def read(p: Path, limit=None):
    if not p.exists():
        return "(missing)"
    lines = p.read_text(errors="replace").splitlines()
    return "\n".join(lines[-limit:] if limit else lines)


def sync_state():
    run(["git", "fetch", "-q", "origin", "coord"], cwd=CO)
    _, counts = run(["git", "rev-list", "--left-right", "--count", "HEAD...origin/coord"], cwd=CO)
    _, dirty = run(["git", "status", "--porcelain"], cwd=CO)
    _, last = run(["git", "log", "-1", "--format=%cd · %s", "--date=format:%H:%M"], cwd=CO)
    try:
        ahead, behind = (int(x) for x in counts.split())
    except ValueError:
        return False, f"cannot read state: {counts}"
    n_dirty = len([line for line in dirty.splitlines() if line.strip()])
    ok = ahead == 0 and behind == 0 and n_dirty == 0
    txt = (f"to send: {ahead} commit, {n_dirty} changed files · to receive: {behind} commit"
           f" · last commit {last}")
    return ok, txt


def messages(limit=40):
    d = CO / "messages"
    if not d.exists():
        return []
    out = []
    for f in sorted(d.glob("*.md"), reverse=True)[:limit]:
        meta, body, lines = {}, [], f.read_text(errors="replace").splitlines()
        in_meta = False
        for i, line in enumerate(lines):
            if i == 0 and line == "---":
                in_meta = True
                continue
            if in_meta and line == "---":
                in_meta = False
                continue
            if in_meta and ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip()
            elif not in_meta:
                body.append(line)
        out.append((meta, "\n".join(body).strip()))
    return out


CSS = """
:root{--ink:#18181b;--muted:#64748b;--bg:#f4f4f5;--card:#fff;--acc:#2563eb;--ok:#15803d;--bad:#b91c1c}
@media (prefers-color-scheme:dark){:root{--ink:#e4e4e7;--muted:#a1a1aa;--bg:#18181b;--card:#27272a;--acc:#60a5fa;--ok:#4ade80;--bad:#f87171}}
body{font-family:Inter,system-ui,sans-serif;background:var(--bg);color:var(--ink);margin:0;padding:16px;max-width:1100px;margin:auto}
h1{font-size:20px;margin:4px 0 12px}h2{font-size:15px;margin:0 0 8px;color:var(--acc)}
.card{background:var(--card);border-radius:10px;padding:14px;margin-bottom:14px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:14px}
pre{white-space:pre-wrap;word-wrap:break-word;font-size:12.5px;margin:0;max-height:340px;overflow:auto}
.msg{border-top:1px solid #8884;padding:8px 0}.meta{font-size:12px;color:var(--muted)}
.ok{color:var(--ok);font-weight:600}.bad{color:var(--bad);font-weight:600}
input,select,textarea,button{font:inherit;padding:6px 8px;border-radius:6px;border:1px solid #8886;background:var(--card);color:var(--ink)}
textarea{width:100%;box-sizing:border-box;min-height:70px}button{background:var(--acc);color:#fff;border:0;cursor:pointer}
.row{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin-bottom:8px}
.flash{background:#2563eb22;padding:8px;border-radius:6px;margin-bottom:10px;font-size:13px}
"""


def page(flash=""):
    e = html.escape
    ok, state = sync_state()
    who = me()
    msgs = messages()
    opts = "".join(f"<option>{p}</option>" for p in ["all"] + [p for p in PEOPLE if p != who])
    msg_html = "".join(
        f'<div class="msg"><div class="meta">{e(m.get("date", ""))} · <b>{e(m.get("from", "?"))}</b>'
        f' → {e(m.get("to", "?"))} · {e(m.get("subject", ""))}</div><pre>{e(b)}</pre></div>'
        for m, b in msgs
    ) or "<p>No messages.</p>"
    status_html = "".join(
        f'<div class="card"><h2>{p}</h2><pre>{e(read(CO / "agents" / p / "status.md", 25))}</pre></div>'
        for p in PEOPLE
    )
    flash_html = f'<div class="flash"><pre>{e(flash)}</pre></div>' if flash else ""
    badge = '<span class="ok">✔ in sync</span>' if ok else '<span class="bad">✖ not in sync</span>'
    return f"""<!doctype html><html lang="it"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>KVA Coord</title>
<meta http-equiv="refresh" content="60"><style>{CSS}</style></head><body>
<h1>KVA coord · I am <b>{e(who)}</b> · {datetime.now():%H:%M:%S}</h1>
{flash_html}
<div class="card"><div class="row">{badge}<span class="meta">{e(state)}</span>
<form method="post" action="/sync"><button>Sync now</button></form></div>
<div class="meta">Page reloads every 60 s (checks only; press Sync to send/receive).</div></div>
<div class="card"><h2>Send a message</h2><form method="post" action="/msg">
<div class="row">To <select name="to">{opts}</select>
<input name="subject" placeholder="subject" required style="flex:1"></div>
<textarea name="text" placeholder="text" required></textarea>
<div class="row" style="margin-top:8px"><button>Send + sync</button></div></form></div>
<div class="grid">{status_html}</div>
<div class="grid"><div class="card"><h2>Messages (newest first)</h2>{msg_html}</div>
<div><div class="card"><h2>SITUAZIONE</h2><pre>{e(read(CO / "SITUAZIONE.md"))}</pre></div>
<div class="card"><h2>TASKS</h2><pre>{e(read(CO / "TASKS.md"))}</pre></div></div></div>
</body></html>"""


class H(BaseHTTPRequestHandler):
    def _send(self, body, code=200):
        data = body.encode()
        self.send_response(code)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        if self.path.split("?")[0] != "/":
            return self._send("not found", 404)
        self._send(page())

    def do_POST(self):
        n = int(self.headers.get("Content-Length", 0))
        form = {k: v[0] for k, v in urllib.parse.parse_qs(self.rfile.read(n).decode()).items()}
        if self.path == "/sync":
            _, out = run(["bash", str(COORD_SH), "sync"])
        elif self.path == "/msg":
            to = form.get("to", "all")
            if to not in ["all"] + PEOPLE:
                return self._send("bad recipient", 400)
            _, out = run(["bash", str(COORD_SH), "msg", to,
                          form.get("subject", "").strip() or "(no subject)", form.get("text", "").strip()])
        else:
            return self._send("not found", 404)
        self._send(page(out))

    def log_message(self, *a):
        pass


if __name__ == "__main__":
    if not CO.exists():
        sys.exit("No .coord/ folder: run `bash scripts/coord.sh init <name>` first.")
    print(f"KVA coord page: http://localhost:{PORT}  (Ctrl+C to stop)")
    ThreadingHTTPServer(("127.0.0.1", PORT), H).serve_forever()
