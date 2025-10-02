from flask import Flask, render_template, url_for
import os, json

app = Flask(__name__)

# --- Config ---
CHANNEL_NAME = os.getenv("CHANNEL_NAME", "Firetube")
TAGLINE = os.getenv("TAGLINE", "Throne and Liberty Guides")
YOUTUBE_URL = os.getenv("YOUTUBE_URL", "https://youtube.com")
DISCORD_URL = os.getenv("DISCORD_URL", "https://discord.gg/yourinvite")
TWITTER_URL = os.getenv("TWITTER_URL", "")
TIKTOK_URL = os.getenv("TIKTOK_URL", "")

# Load demo guides
def load_guides():
    path = os.path.join(os.path.dirname(__file__), "guides.json")
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []

@app.context_processor
def inject_globals():
    return dict(
        CHANNEL_NAME=CHANNEL_NAME,
        TAGLINE=TAGLINE,
        YOUTUBE_URL=YOUTUBE_URL,
        DISCORD_URL=DISCORD_URL,
        TWITTER_URL=TWITTER_URL,
        TIKTOK_URL=TIKTOK_URL
    )

@app.route("/")
def index():
    guides = load_guides()[:6]
    return render_template("index.html", guides=guides)

@app.route("/guides")
def guides():
    guides = load_guides()
    return render_template("guides.html", guides=guides)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/health")
def health():
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
