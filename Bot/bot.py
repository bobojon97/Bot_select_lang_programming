import config
import logging

from aiogram.types import ReplyKeyboardRemove
from aiogram import Bot, Dispatcher, executor, types

from keyboard import menu, web, soft, mob

bot  = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=["start"])
async def echo(message: types.Message):
    await message.answer("<b>Добро пожаловать. Выберите, какую направление хотите изучить</b>", parse_mode='html', reply_markup=menu)


@dp.message_handler(text="Веб разработка")
async def send_mess(message: types.Message):

    await message.answer(f"<b>{message.text}</b>. Точняк! Ты по одресу. Теперь выберите направление", parse_mode='html', reply_markup=web)

@dp.message_handler(text="Front-end")
async def front(message: types.Message):

    await message.answer(f"<b>{message.text}.</b> Крутая штука. Для того чтобы стать фронтенд разработчиком, надо изучить следующый технологии.\n"
                            f"1) <b>HTML</b>\n https://html.com/ \n 2) <b>CSS</b>\n https://css.com/ \n3) <b>JS</b>\n https://learn.javascript.ru/", parse_mode='html')

@dp.message_handler(text="Back-end")
async def front(message: types.Message):

    await message.answer(f" ОУ! <b>{message.text}.</b> Бэкендом надо узучить следующий технологии\n"
                            f"1) <b>Python</b>\n https://www.python.org/ \n 2) <b>Go</b>\n https://go.dev/ \n 3) <b>PHP</b>\n https://www.php.net/", parse_mode='html')

@dp.message_handler(text="Начат тест заново")
async def send_mess(message: types.Message):

    await message.answer(f"<b>Вы начали тест заново</b>", parse_mode='html',  reply_markup=menu)


@dp.message_handler(text="Создание игр")
async def send_mess(message: types.Message):

    await message.answer(f"<b>{message.text}-ы.</b> Отличный выбор. Чтобы освоит себя в этом професии, надо знать следующий языки.\n"
                f"1) <b>C#</b>\n https://learn.microsoft.com/ru-ru/dotnet/csharp/ \n 2) <b>Js</b>\n https://learn.javascript.ru/\n 3) <b>C++</b>\n https://learn.microsoft.com/ru-ru/cpp/cpp/cpp-language-reference?view=msvc-170", parse_mode='html')

@dp.message_handler(text="Создание ИИ")
async def send_mess(message: types.Message):

    await message.answer(f"<b>{message.text}.</b>\nСупер крутая выбор. Могу рекомендовать тебя только <b>Python</b>\n https://www.python.org/", parse_mode='html')

@dp.message_handler(text="Обработка данных")
async def send_mess(message: types.Message):

    await message.answer(f"<b>{message.text}.</b>\nНеплохой направление\n<b>Python</b> подходит для обработка больших данных\n https://www.python.org/", parse_mode='html')

@dp.message_handler(text="Софт для компютера")
async def send_mess(message: types.Message):

    await message.answer(f"<b>{message.text}.</b>\nВыберите, именно какую направление вы хотите", parse_mode='html', reply_markup=soft)

@dp.message_handler(text="Windows")
async def front(message: types.Message):

    await message.answer(f"<b>{message.text}.</b>\nМогу рекомендовать тебя <b>C#</b>\n https://learn.microsoft.com/ru-ru/dotnet/csharp/", parse_mode='html')

@dp.message_handler(text="Mac")
async def front(message: types.Message):

    await message.answer(f"<b>{message.text}</b>\nТогда тебя стоит узучить <b>Swift</b> \nhttps://developer.apple.com/swift/", parse_mode='html')

@dp.message_handler(text="Все платформы")
async def front(message: types.Message):

    await message.answer(f"<b>{message.text}.</b>\nМогу рекомендовать тебя <b>Java</b>\n https://www.java.com/ru/", parse_mode='html')

@dp.message_handler(text="Начат тест заново")
async def send_mess(message: types.Message):

    await message.answer(f"<b>Вы начали тест заново</b>.", parse_mode='html',  reply_markup=menu)

@dp.message_handler(text="Мобильное приложение")
async def send_mess(message: types.Message):

    await message.answer(f"<b>{message.text}.</b>\nОтличное направление, выберите, под какую <b>ОС</b> вы хотите создать", parse_mode='html', reply_markup=mob)

@dp.message_handler(text="IOS")
async def front(message: types.Message):

    await message.answer(f"<b>{message.text}.</b>\nРекомендую <b>Swift</b> \n https://developer.apple.com/swift/" , parse_mode='html')

@dp.message_handler(text="Android")
async def front(message: types.Message):

    await message.answer(f"<b>{message.text}.</b>\nМогу рекомендовать тебя <b>Kotlin</b>\n https://kotlinlang.org/", parse_mode='html')

@dp.message_handler(text="Кроссплатформенный")
async def front(message: types.Message):

    await message.answer(f"<b>{message.text}.</b>\nМогу рекомендовать тебя <b>Flutter</b>\n https://flutter.dev/", parse_mode='html')

@dp.message_handler(text="Начат тест заново")
async def send_mess(message: types.Message):

    await message.answer(f"<b>Вы начали тест заново</b>.", parse_mode='html',  reply_markup=menu)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)