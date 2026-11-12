"""Smoke test: one tiny call per configured provider. Prints which keys work."""
import os
import sys

from dotenv import load_dotenv

load_dotenv()
worked = False

if os.getenv("GEMINI_API_KEY"):
    try:
        from google import genai

        client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
        r = client.models.generate_content(model="gemini-2.5-flash", contents="Reply with the single word: ready")
        print(f"  gemini: {r.text.strip()}")
        worked = True
    except Exception as e:  # noqa: BLE001 - we want any failure reported
        print(f"  gemini: ERROR {type(e).__name__}: {e}")

if os.getenv("ANTHROPIC_API_KEY"):
    try:
        import anthropic

        client = anthropic.Anthropic()
        r = client.messages.create(
            model="claude-haiku-5-5", max_tokens=10,
            messages=[{"role": "user", "content": "Reply with the single word: ready"}],
        )
        print(f"  anthropic: {r.content[0].text.strip()}")
        worked = True
    except Exception as e:  # noqa: BLE001
        print(f"  anthropic: ERROR {type(e).__name__}: {e}")

if not worked:
    print("  no working API key found in .env")
sys.exit(0 if worked else 1)
