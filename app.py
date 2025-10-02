from flask import Flask, render_template, jsonify
import json
import os

app = Flask(
    __name__,
    template_folder=".",   # HTML im Root
    static_folder="."      # CSS/Bilder auch im Root
)

def load_guides():
    try:
        with open("guides.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print("Fehler beim Laden von guides.json:", e)
        return []

@app.route("/")
def index():
    guides = load_guides()
    return render_template("index.html", guides=guides,
                           CHANNEL_NAME=os.getenv("CHANNEL_NAME", "Firetube"),
                           TAGLINE=os.getenv("TAGLINE", "Throne and Liberty Guides"))

@app.route("/guides")
def guides():
    guides = load_guides()
    return render_template("guides.html", guides=guides,
                           CHANNEL_NAME=os.getenv("CHANNEL_NAME", "Firetube"),
                           TAGLINE=os.getenv("TAGLINE", "Throne and Liberty Guides"))

@app.route("/about")
def about():
    return render_template("about.html",
                           CHANNEL_NAME=os.getenv("CHANNEL_NAME", "Firetube"),
                           TAGLINE=os.getenv("TAGLINE", "Throne and Liberty Guides"))

@app.route("/api/guides")
def api_guides():
    return jsonify(load_guides())

@app.route("/health")
def health():
    return "ok", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
