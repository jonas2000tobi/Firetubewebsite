from flask import Flask, render_template

# ALLES aus dem Repo-Root laden (HTML, CSS, Bilder)
app = Flask(
    __name__,
    template_folder=".",   # <-- HTML liegt im Root
    static_folder=".",     # <-- CSS/Images auch im Root
    static_url_path=""     # <-- erreichbar direkt unter /styles.css, /logo.png
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/guides")
def guides():
    return render_template("guides.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/health")
def health():
    return "ok", 200

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
