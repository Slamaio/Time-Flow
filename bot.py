import handlers
from webhook import dp, WEBHOOK_PATH, on_startup, on_shutdown, WEBAPP_HOST, WEBAPP_PORT
from aiogram.utils.executor import start_webhook, start_polling
from config import IS_LOCAL

if __name__ == "__main__":
    if IS_LOCAL == 1:
        start_polling(dispatcher=dp, on_startup=on_startup, on_shutdown=on_shutdown, skip_updates=True)
    else:
        start_webhook(
            dispatcher=dp,
            webhook_path=WEBHOOK_PATH,
            on_startup=on_startup,
            on_shutdown=on_shutdown,
            skip_updates=True,
            host=WEBAPP_HOST,
            port=WEBAPP_PORT)
