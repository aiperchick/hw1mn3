import os
from aiogram import Bot, Dispatcher, executor
from aiogram.utils import executor
from dotenv import load_dotenv
from os import getenv
from telebot import types
import random

load_dotenv()

bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(text=f"привет, {message.from_user.first_name}, я твой мама бот")
    await message.delete()


@dp.message_handler(commands=["help"])
async def help(message: types.Message):
    # noinspection PyArgumentList
    await message.answer(text=f"""start - начало
help - список команд
myinfo - получить информацию о себе
picture - получить случайную картинку""")


@dp.message_handler(commands=["myinfo"])
async def myinfo(message: types.Message):
    await message.answer(text=f"""
твой id - {message.from_user.id}
твое имя - {message.from_user.first_name}
твоя фамлия - {message.from_user.last_name}
твое полное имя - {message.from_user.full_name}
твой ник - {message.from_user.username}
""")


@dp.message_handler(commands=["picture"])
async def picture(message: types.Message):
    await message.answer_photo(
        open('./images/' + random.choice(os.listdir('images')), 'rb'),
        caption="помнишь? это ты"
    )


@dp.message_handler()
async def upper_letters(message: types.Message):
    letters = message.text.split(' ')
    if len(letters) >= 3:
        await message.answer(message.text.upper())
    else:
        await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp)
