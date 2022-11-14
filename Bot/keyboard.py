from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


menu = ReplyKeyboardMarkup( row_width=2,
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
            KeyboardButton(text="Back-end"),
            KeyboardButton(text="Начат тест заново")
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
            KeyboardButton(text="Начат тест заново")
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
            KeyboardButton(text="Начат тест заново")
        ]
    ],
    resize_keyboard=True
)