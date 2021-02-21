from config import TOKEN, WEBHOOK_HOST, WEBAPP_PORT
import os
import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import postgres as db


bot = Bot(token=TOKEN)
memory_storage = MemoryStorage()
dp = Dispatcher(bot, storage=memory_storage)
logging.basicConfig(level=logging.INFO)


# webhook settings
WEBHOOK_HOST = WEBHOOK_HOST
WEBHOOK_PATH = '/' + TOKEN
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"


# webserver settings
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = WEBAPP_PORT


async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)
    # insert code here to run it after start
    db.create_tables()


async def on_shutdown(dp):
    logging.warning('Shutting down..')

    # insert code here to run it before shutdown
    db.close()

    # Remove webhook (not acceptable in some cases)
    # await bot.delete_webhook()

    logging.warning('Bye!')
