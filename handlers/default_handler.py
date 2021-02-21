from aiogram import types
from webhook import dp


@dp.message_handler(content_types=types.ContentTypes.ANY, state="*")
async def all_other_messages(message: types.Message):
    await message.reply("No such command/option")