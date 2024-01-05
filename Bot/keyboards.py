from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

menu = ReplyKeyboardMarkup(row_width=2, 
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
                                   KeyboardButton(text="Софт для компьютера"),
                                   KeyboardButton(text="Мобильное приложение"),
                               ],
                               [
                                   KeyboardButton(text="Блокчейн и криптовалюты"),
                                   KeyboardButton(text="Системное программирование"),
                               ],
                               [
                                   KeyboardButton(text="Безопасность"),
                                   KeyboardButton(text="Data Science и анализ данных"),
                               ],
                               [
                                   KeyboardButton(text="DevOps"),
                                   KeyboardButton(text="Компьютерная графика"),
                               ],
                               [
                                   KeyboardButton(text="Интернет вещей (IoT)"),
                                   KeyboardButton(text="Другое"),
                               ]
                           ], 
                           resize_keyboard=True)
