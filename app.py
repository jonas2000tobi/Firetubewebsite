from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# Platzhalter-Routen – du kannst später echte Seiten bauen
@app.route("/guides")
def guides():
    return "<h1>Guides</h1>"

@app.route("/builds")
def builds():
    return "<h1>Builds</h1>"

@app.route("/klassen")
def klassen():
    return "<h1>Klassen</h1>"

@app.route("/welt")
def welt():
    return "<h1>Welt</h1>"

@app.route("/tipps")
def tipps():
    return "<h1>Tipps & Tricks</h1>"

@app.route("/ueber-mich")
def about():
    return "<h1>Über mich</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
