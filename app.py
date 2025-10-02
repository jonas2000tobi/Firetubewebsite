import os
from flask import Flask, render_template, Response

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TPL_DIR  = os.path.join(BASE_DIR, "templates")
ST_DIR   = os.path.join(BASE_DIR, "static")

app = Flask(
    __name__,
    template_folder=TPL_DIR,
    static_folder=ST_DIR,
    static_url_path="/static",
)

def _log_tree():
    def ls(path):
        try:
            return ", ".join(sorted(os.listdir(path)))
        except Exception as e:
            return f"<ERR {e}>"
    print("== APP PATHS ==")
    print("BASE_DIR:", BASE_DIR)
    print("TPL_DIR :", TPL_DIR, "->", ls(TPL_DIR))
    print("ST_DIR  :", ST_DIR,  "->", ls(ST_DIR))
    print("index.html exists:", os.path.exists(os.path.join(TPL_DIR, "index.html")))
    print("================")

# Statt before_first_request: einfach beim Import einmal loggen
_log_tree()

@app.route("/_diag")
def diag():
    lines = [
        f"BASE_DIR: {BASE_DIR}",
        f"TEMPLATES: {TPL_DIR}",
        f"STATIC: {ST_DIR}",
        f"templates/: {', '.join(sorted(os.listdir(TPL_DIR)))}",
        f"static/: {', '.join(sorted(os.listdir(ST_DIR)))}",
        f"index.html exists: {os.path.exists(os.path.join(TPL_DIR, 'index.html'))}",
    ]
    return Response("\n".join(lines), mimetype="text/plain")

@app.route("/")
def home():
    idx = os.path.join(TPL_DIR, "index.html")
    if not os.path.exists(idx):
        _log_tree()
        return Response(
            "Template 'index.html' NICHT gefunden.\n"
            "Sieh dir /_diag an und prüfe Ordner & Dateinamen (Case-Sensitive!).",
            mimetype="text/plain",
            status=500,
        )
    return render_template("index.html")

@app.route("/health")
def health():
    return "ok", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
