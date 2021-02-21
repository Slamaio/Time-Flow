import os

TOKEN = os.getenv("TELEGRAM_API_TOKEN")
IS_LOCAL = int(os.getenv("IS_LOCAL"))
WEBHOOK_HOST = os.getenv("WEBHOOK_HOST")
OWNER_ID = int(os.getenv("BOT_OWNER_ID"))
DB_URL = os.getenv("DATABASE_URL")
WEBAPP_PORT = os.getenv("PORT", 5000)
