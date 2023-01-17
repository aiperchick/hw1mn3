import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.utils import executor
from dotenv import load_dotenv

from handlers.myinfo import myinfo
from handlers.picture import picture
from handlers.shop import shop_start
from handlers.start import start
from handlers.upper_letters import upper_letters

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
# наш бот
    load_dotenv()
    bot = Bot(os.getenv('TOKEN'))
    dp = Dispatcher(bot)

# регистрируем обработчики
    dp.register_message_handler(start, commands=["start"])
    dp.register_message_handler(myinfo, commands=["myinfo"])
    dp.register_message_handler(picture, commands=["picture"])
    dp.register_callback_query_handler(shop_start, text='shop_start')

    dp.register_message_handler(upper_letters)

    executor.start_polling(dp)
