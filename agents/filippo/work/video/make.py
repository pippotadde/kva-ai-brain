"""Render captioned slides and encode the 48 s idea video (H.264 + silent AAC)."""
import subprocess, sys, textwrap
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import imageio_ffmpeg

OUT = Path(__file__).parent
F = "/usr/share/fonts/truetype/lato/Lato-{}.ttf"
W, H = 1280, 720
BG, FG, MUTED, ACCENT, RED = "#0f1720", "#f4f1ea", "#9aa5b1", "#f2b134", "#e5534b"

def font(style, size):
    return ImageFont.truetype(F.format(style), size)

# Each slide: (seconds, kicker, title, body lines, footnote)
SLIDES = [
    (8, "IL PROBLEMA", "Un allergene non dichiarato\nin un prodotto confezionato.",
     ["È la prima causa di richiami alimentari negli USA:",
      "38,8% dei richiami FDA + USDA nel 2025."],
     "Fonte: Statista su dati FDA/USDA 2025"),
    (8, "PERCHÉ SUCCEDE", "Le informazioni c'erano già.\nErano sparse.",
     ["Mail del fornitore: \"la farina ora può contenere soia\"",
      "Linea 2 pulita con la procedura vecchia (rev. A)",
      "Report di turno: macchina spostata vicino alle nocciole"],
     "Nessuno le mette insieme in tempo."),
    (7, "PER CHI", "Il responsabile qualità\ndi uno stabilimento alimentare",
     ["con più allergeni sulle stesse linee:",
      "dolciario, prodotti da forno, co-packer."],
     ""),
    (9, "LA NOSTRA IDEA", "Un cervello AI che ricorda\ne collega lo stabilimento",
     ["Legge ogni documento appena arriva",
      "Collega fornitore → ingrediente → macchina → lotto → etichetta",
      "Ogni fatto con fonte, autore e data; sa cosa è superato"],
     ""),
    (8, "AVVISA PRIMA, NON DOPO", "Rischio + prove → il manager approva",
     ["Blocco mirato dei soli lotti coinvolti",
      "Istruzioni ai lavoratori appena c'è la firma",
      "L'AI propone, una persona decide. Tutto resta tracciato."],
     ""),
    (8, "OGGI TESTIAMO", "Trova il rischio incrociando\n3 documenti sparsi?",
     ["Stabilimento dolciario, dati sintetici dichiarati.",
      "Votaci se vuoi vederlo funzionare stasera."],
     "Team KVA · KVA Hackathon \"AI brain for industry\" · 14.11.2026"),
]

def render(i, sec, kicker, title, body, foot):
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    x = 90
    d.rectangle([x, 90, x + 60, 96], fill=ACCENT)
    d.text((x, 112), kicker, font=font("Bold", 30), fill=ACCENT)
    y = 165
    for line in title.split("\n"):
        d.text((x, y), line, font=font("Black", 58), fill=FG)
        y += 72
    y += 30
    for b in body:
        d.ellipse([x, y + 16, x + 12, y + 28], fill=ACCENT)
        d.text((x + 30, y), b, font=font("Regular", 34), fill=FG)
        y += 54
    if foot:
        d.text((x, H - 80), foot, font=font("Italic", 24), fill=MUTED)
    # progress bar
    d.rectangle([0, H - 8, int(W * (i + 1) / len(SLIDES)), H], fill=ACCENT)
    p = OUT / f"s{i}.png"
    im.save(p)
    return p

def main():
    lines = []
    for i, s in enumerate(SLIDES):
        p = render(i, *s)
        lines += [f"file '{p.name}'", f"duration {s[0]}"]
    lines.append(f"file '{p.name}'")  # concat demuxer needs the last file repeated
    (OUT / "slides.txt").write_text("\n".join(lines) + "\n")
    total = sum(s[0] for s in SLIDES)
    ff = imageio_ffmpeg.get_ffmpeg_exe()
    cmd = [ff, "-y", "-f", "concat", "-safe", "0", "-i", str(OUT / "slides.txt"),
           "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
           "-map", "0:v:0", "-map", "1:a:0", "-t", str(total),
           "-vf", "fps=30,format=yuv420p", "-c:v", "libx264", "-preset", "medium",
           "-crf", "26", "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart",
           str(OUT / "idea.mp4")]
    subprocess.run(cmd, check=True, capture_output=True)
    print("total seconds:", total)

if __name__ == "__main__":
    main()
