from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# Platzhalter-Routen, damit die Menüpunkte anklickbar sind
@app.route("/guides")
def guides():
    return render_template("index.html")

@app.route("/builds")
def builds():
    return render_template("index.html")

@app.route("/klassen")
def klassen():
    return render_template("index.html")

@app.route("/welt")
def welt():
    return render_template("index.html")

@app.route("/tipps")
def tipps():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
