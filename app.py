from flask import Flask, render_template

# alles aus dem Repo-Root laden (deine Wahl ohne Ordnerstruktur)
app = Flask(
    __name__,
    template_folder=".",   # HTML liegt im Root
    static_folder=".",     # CSS/Bilder auch im Root
    static_url_path=""     # erreichbar unter /styles.css, /logo.png, /guide1.jpg ...
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
