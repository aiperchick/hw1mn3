

START_TEXT = """
приветствуем вас, {first_name}, в телеграм боте нашего фаст фуда. 
вы можете заказать разные виды шаурмы и гамбургера.
"""

HELP_TEXT = """
/help - список команд
/myinfo - получить информацию о себе
/picture - получить случайную картинку
"""

MYINFO_TEXT = """
твой id - {message.from_user.id}
твое имя - {message.from_user.first_name} твоя фамлия - {message.from_user.last_name}
твое полное имя - {message.from_user.full_name}
твой ник - {message.from_user.username}
"""