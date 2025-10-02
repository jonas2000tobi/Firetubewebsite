# Firetube Website (Flask) – für Railway

## Quickstart (lokal)
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
export CHANNEL_NAME="Firetube"
export TAGLINE="Throne and Liberty Guides"
export YOUTUBE_URL="https://youtube.com/@Firetube"
export DISCORD_URL="https://discord.gg/yourinvite"
python app.py
```

## Deploy auf Railway
1. Repo in GitHub pushen.
2. In Railway: **New Project → Deploy from GitHub Repo** und dein Repo auswählen.
3. Railway erkennt Flask automatisch via `requirements.txt` + `Procfile`.
4. In **Variables** diese ENV Variablen setzen (optional):
   - `CHANNEL_NAME`, `TAGLINE`, `YOUTUBE_URL`, `DISCORD_URL`, `TWITTER_URL`, `TIKTOK_URL`
5. Deploy abwarten → App öffnet sich unter `https://deinprojekt.up.railway.app`.
6. Eigene Domain verbinden: Project → **Settings → Domains → Add Custom Domain** und DNS setzen.

**Hinweise**
- Healthcheck: `/health`
- Statische Dateien: `static/`, Templates: `templates/`
- Thumbnails ersetzen in `static/img/guide*.jpg` und `guides.json` anpassen.
