from telebot import types
from handlers.constans import START_TEXT
from aiogram import InlineKeyboardButton, InlineKeyboardMarkup

start_kb = InlineKeyboardMarkup(resize_keyboard=True)
start_kb.add(
    InlineKeyboardButton('меню', callback_data='shop_start'),
    InlineKeyboardButton('наш адресс', callbck_data='address')
)


async def start(messege: types.Message):
    """
    приветствие пользователя
    """
    await messege.answer(text=START_TEXT.format(
        first_name=messege.from_user.first_name)
    )
    await messege.delete()
