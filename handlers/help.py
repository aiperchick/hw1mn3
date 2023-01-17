from telebot import types
from handlers.constans import HELP_TEXT


async def help(message: types.Message):
    """
    выводит все команды пользователя
    """
    await message.answer(text=HELP_TEXT)
