from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup



choice = InlineKeyboardMarkup(
        inline_keyboard= [
            [
                InlineKeyboardButton(text="Начать тест заново", callback_data="menu")
            ]
        ]
)


menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Веб разработка"),
            KeyboardButton(text="Создание игр"),
            
           
        ],
        [
            KeyboardButton(text="Создание ИИ "),
            KeyboardButton(text="Обработка данных"),
        ],
        [
            KeyboardButton(text="Софт для компютера"),
            KeyboardButton(text="Мобильное приложение"),
        ]

    ],
    resize_keyboard=True
)

web = ReplyKeyboardMarkup(
    keyboard= [
        [
            KeyboardButton(text="Front-end"),
            KeyboardButton(text="Back-end")
        ]
    ],
    resize_keyboard=True
)


soft = ReplyKeyboardMarkup(
    keyboard= [
        [
            KeyboardButton(text="Windows"),
            KeyboardButton(text="Mac"),
            KeyboardButton(text="Все платформы"),
        ]
    ],
    resize_keyboard=True
)

mob = ReplyKeyboardMarkup(
    keyboard= [
        [
            KeyboardButton(text="IOS"),
            KeyboardButton(text="Android"),
            KeyboardButton(text="Кроссплатформенный"),
        ]
    ],
    resize_keyboard=True
)