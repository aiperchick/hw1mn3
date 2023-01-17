from telebot import types


async def upper_letters(message: types.Message):
    """
    делает буквы большими
    """
    letters = message.text.split(' ')
    if len(letters) >= 3:
        await message.answer(message.text.upper())
    else:
        await message.answer(message.text)
