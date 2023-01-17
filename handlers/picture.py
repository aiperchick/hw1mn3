import os
import random
from telebot import types

async def picture(message: types.Message):
     await message.answer_photo(
         open('./images/' + random.choice(os.listdir('images')), 'rb'),
         caption="помнишь? это ты"
     )