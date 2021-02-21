from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from webhook import dp, bot
from config import OWNER_ID
import postgres as db


@dp.message_handler(commands="start", state="*")
async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer("I am alive!!!!!")