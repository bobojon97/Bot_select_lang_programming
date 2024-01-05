import config
import logging

from aiogram.types import ReplyKeyboardRemove
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from keyboards import *

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("<b>Добро пожаловать! Выберите направление, которое вы хотите изучить:</b>", parse_mode='html', reply_markup=menu)

@dp.message_handler(text="Веб разработка")
async def web_dev(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    buttons = [
        types.InlineKeyboardButton(text="Front-end", callback_data="front_end"),
        types.InlineKeyboardButton(text="Back-end", callback_data="back_end"),
        types.InlineKeyboardButton(text="Fullstack", callback_data="fullstack"),
    ]
    keyboard.add(*buttons)
    await message.answer(f"<b>{message.text}.</b> Отличный выбор! Теперь выберите конкретное направление:", parse_mode='html', reply_markup=keyboard)


# Обработка непредвиденных ответов
@dp.message_handler(lambda message: message.text not in ["Front-end", "Back-end", "Fullstack", "Создание игр",
                                                          "Создание ИИ", "Обработка данных", "Софт для компьютера", "Мобильное приложение",
                                                          "Блокчейн и криптовалюты", "Системное программирование", "Безопасность",
                                                          "Data Science и анализ данных", "DevOps", "Компьютерная графика",
                                                          "Интернет вещей (IoT)", "Другое"], state='*')
async def handle_unexpected(message: types.Message, state: FSMContext):
    await message.reply("Пожалуйста, используйте кнопки для выбора направления.")


@dp.callback_query_handler(text="front_end")
async def front_end(callback_query: types.CallbackQuery):
    await callback_query.answer()
    text = (
        "<b>Front-end.</b> Отличный выбор! Для становления фронтенд-разработчиком, вам следует изучить следующие технологии:\n"
        "1. [HTML](https://html.com/)\n"
        "2. [CSS](https://css.com/)\n"
        "3. [JavaScript (JS)](https://learn.javascript.ru/)\n"
        "<b>Дополнительно:</b>\n"
        "4. [React](https://reactjs.org/)\n"
        "5. [Vue.js](https://vuejs.org/)\n"
        "6. [Angular](https://angular.io/)"
    )
    await bot.send_message(callback_query.from_user.id, text, parse_mode='html')

@dp.callback_query_handler(text="back_end")
async def back_end(callback_query: types.CallbackQuery):
    await callback_query.answer()
    text = (
        "<b>Back-end.</b> Отличный выбор! Для становления бэкенд-разработчиком, вам следует изучить следующие технологии:\n"
        "1. [Python](https://www.python.org/)\n"
        "2. [NodeJS](https://nodejs.org/)\n"
        "3. [Go](https://go.dev/)\n"
        "4. [PHP](https://www.php.net/)\n"
        "<b>Дополнительно:</b>\n"
        "5. [Django](https://www.djangoproject.com/)\n"
        "6. [Laravel](https://laravel.com/)"
    )
    await bot.send_message(callback_query.from_user.id, text, parse_mode='html')

@dp.callback_query_handler(text="fullstack")
async def fullstack(callback_query: types.CallbackQuery):
    await callback_query.answer()
    text = (
        "<b>Fullstack.</b> Отличный выбор! Для становления Fullstack-разработчиком, вам следует изучить как фронтенд-, так и бэкенд-технологии:\n"
        "Фронтенд:\n"
        "1. [HTML](https://html.com/)\n"
        "2. [CSS](https://css.com/)\n"
        "3. [JavaScript (JS)](https://learn.javascript.ru/)\n"
        "Дополнительно:\n"
        "4. [React](https://reactjs.org/)\n"
        "5. [Vue.js](https://vuejs.org/)\n"
        "6. [Angular](https://angular.io/)\n\n"
        "Бэкенд:\n"
        "1. [Python](https://www.python.org/)\n"
        "2. [NodeJS](https://nodejs.org/)\n"
        "3. [Go](https://go.dev/)\n"
        "4. [PHP](https://www.php.net/)\n"
        "Дополнительно:\n"
        "5. [Django](https://www.djangoproject.com/)\n"
        "6. [Laravel](https://laravel.com/)"
    )
    await bot.send_message(callback_query.from_user.id, text, parse_mode='html')


@dp.message_handler(text="Создание игр")
async def create_games_handler(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    buttons = [
        types.InlineKeyboardButton(text="Python", callback_data="games_python"),
        types.InlineKeyboardButton(text="Unity", callback_data="games_unity"),
    ]
    keyboard.add(*buttons)
    await message.answer(f"<b>{message.text}.</b> Отличный выбор! Теперь выберите язык программирования для создания игр:", parse_mode='html', reply_markup=keyboard)

@dp.callback_query_handler(text="games_python")
async def games_python(callback_query: types.CallbackQuery):
    await callback_query.answer()
    text = (
        "<b>Python для создания игр.</b> Отличный выбор! Для создания игр на Python вам может потребоваться изучить библиотеки и фреймворки, такие как:\n"
        "1. [Pygame](https://www.pygame.org/)\n"
        "2. [Ren'Py](https://www.renpy.org/)\n"
        "3. [Godot Engine](https://godotengine.org/) (с использованием GDScript)"
    )
    await bot.send_message(callback_query.from_user.id, text, parse_mode='html')

@dp.callback_query_handler(text="games_unity")
async def games_unity(callback_query: types.CallbackQuery):
    await callback_query.answer()
    text = (
        "<b>Unity для создания игр.</b> Отличный выбор! Unity поддерживает использование C# для программирования игр. "
        "Для начала работы с Unity, вы можете изучить официальную документацию и учебные материалы на сайте: [Unity Learn](https://learn.unity.com/)"
    )
    await bot.send_message(callback_query.from_user.id, text, parse_mode='html')


@dp.message_handler(text="Создание ИИ")
async def ai_creation_handler(message: types.Message):
    text = (
        "<b>Создание ИИ.</b> Прежде чем приступить к созданию искусственного интеллекта, рекомендуется изучить язык программирования Python. "
        "Python - прекрасный выбор для начала вашего пути в программировании. После изучения Python, вы можете выбрать подкатегорию создания ИИ:"
    )
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    buttons = [
        types.InlineKeyboardButton(text="Машинное обучение", callback_data="ai_ml"),
        types.InlineKeyboardButton(text="Глубокое обучение", callback_data="ai_dl"),
    ]
    keyboard.add(*buttons)
    await message.answer(text, parse_mode='html', reply_markup=keyboard)

@dp.callback_query_handler(text="ai_ml")
async def ai_ml(callback_query: types.CallbackQuery):
    await callback_query.answer()
    text = (
        "<b>Машинное обучение для создания ИИ.</b> Отличный выбор! Для создания ИИ с использованием машинного обучения, "
        "вам может потребоваться изучить следующие технологии:\n"
        "1. [Scikit-learn](https://scikit-learn.org/)\n"
        "2. [TensorFlow](https://www.tensorflow.org/)\n"
        "3. [PyTorch](https://pytorch.org/)"
    )
    await bot.send_message(callback_query.from_user.id, text, parse_mode='html')

@dp.callback_query_handler(text="ai_dl")
async def ai_dl(callback_query: types.CallbackQuery):
    await callback_query.answer()
    text = (
        "<b>Глубокое обучение для создания ИИ.</b> Отличный выбор! Для создания ИИ с использованием глубокого обучения, "
        "вам может потребоваться изучить следующие технологии:\n"
        "1. [TensorFlow](https://www.tensorflow.org/)\n"
        "2. [PyTorch](https://pytorch.org/)\n"
        "3. [Keras](https://keras.io/)"
    )
    await bot.send_message(callback_query.from_user.id, text, parse_mode='html')

@dp.message_handler(text="Обработка данных")
async def data_processing_handler(message: types.Message):
    text = (
        "<b>Обработка данных.</b> Рекомендуется использовать Python для обработки данных. "
        "Python предлагает множество библиотек для эффективной работы с данными. "
        "Выберите направление для обработки данных:"
    )
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    buttons = [
        types.InlineKeyboardButton(text="Анализ данных с использованием Pandas", callback_data="data_pandas"),
    ]
    keyboard.add(*buttons)
    await message.answer(text, parse_mode='html', reply_markup=keyboard)

@dp.callback_query_handler(text="data_pandas")
async def data_pandas(callback_query: types.CallbackQuery):
    await callback_query.answer()
    text = (
        "<b>Анализ данных с использованием Pandas.</b> Отличный выбор! "
        "Pandas - мощная библиотека для обработки и анализа данных в Python. "
        "Для изучения Pandas вы можете использовать официальную документацию: [Pandas Documentation](https://pandas.pydata.org/docs/)"
    )
    await bot.send_message(callback_query.from_user.id, text, parse_mode='html')

@dp.message_handler(text="Софт для компьютера")
async def software_for_computers_handler(message: types.Message):
    text = (
        "<b>Софт для компьютера.</b> Выберите подкатегорию в области создания программного обеспечения для компьютера:"
    )
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    buttons = [
        types.InlineKeyboardButton(text="Windows", callback_data="software_windows"),
        types.InlineKeyboardButton(text="macOS", callback_data="software_macos"),
        types.InlineKeyboardButton(text="Cross-Platform", callback_data="software_cross_platform"),
    ]
    keyboard.add(*buttons)
    await message.answer(text, parse_mode='html', reply_markup=keyboard)

@dp.callback_query_handler(text="software_windows")
async def software_windows(callback_query: types.CallbackQuery):
    await callback_query.answer()
    text = (
        "<b>Windows-приложения.</b> Для разработки программного обеспечения под Windows, вы можете использовать различные языки программирования, такие как:\n"
        "1. [C#](https://docs.microsoft.com/en-us/dotnet/csharp/) с использованием [Windows Forms](https://docs.microsoft.com/en-us/dotnet/desktop/winforms/)\n"
        "2. [C++](https://docs.microsoft.com/en-us/cpp/) с использованием [WinAPI](https://docs.microsoft.com/en-us/windows/win32/apiindex/windows-api-list)\n"
        "3. [Python](https://www.python.org/) с использованием [PyQt](https://riverbankcomputing.com/software/pyqt/) или [Tkinter](https://docs.python.org/3/library/tkinter.html)"
    )
    await bot.send_message(callback_query.from_user.id, text, parse_mode='html')

@dp.callback_query_handler(text="software_macos")
async def software_macos(callback_query: types.CallbackQuery):
    await callback_query.answer()
    text = (
        "<b>macOS-приложения.</b> Для разработки программного обеспечения под macOS, вы можете использовать следующие языки программирования:\n"
        "1. [Swift](https://developer.apple.com/swift/)\n"
        "2. [Objective-C](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/Introduction/Introduction.html)\n"
        "3. [Python](https://www.python.org/) с использованием [PyQt](https://riverbankcomputing.com/software/pyqt/) или [Tkinter](https://docs.python.org/3/library/tkinter.html)"
    )
    await bot.send_message(callback_query.from_user.id, text, parse_mode='html')

@dp.callback_query_handler(text="software_cross_platform")
async def software_cross_platform(callback_query: types.CallbackQuery):
    await callback_query.answer()
    text = (
        "<b>Кросс-платформенные приложения.</b> Для создания кросс-платформенного программного обеспечения, вы можете использовать:\n"
        "1. [Electron](https://www.electronjs.org/) с использованием веб-технологий (HTML, CSS, JavaScript)\n"
        "2. [Qt](https://www.qt.io/) с использованием [PyQt](https://riverbankcomputing.com/software/pyqt/)"
    )
    await bot.send_message(callback_query.from_user.id, text, parse_mode='html')

@dp.message_handler(text="Мобильное приложение")
async def mobile_app_handler(message: types.Message):
    text = (
        "<b>Мобильные приложения.</b> Выберите подкатегорию в области создания мобильных приложений:"
    )
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    buttons = [
        types.InlineKeyboardButton(text="iOS-приложения", callback_data="mobile_ios"),
        types.InlineKeyboardButton(text="Android-приложения", callback_data="mobile_android"),
    ]
    keyboard.add(*buttons)
    await message.answer(text, parse_mode='html', reply_markup=keyboard)

@dp.callback_query_handler(text="mobile_ios")
async def mobile_ios(callback_query: types.CallbackQuery):
    await callback_query.answer()
    text = (
        "<b>iOS-приложения.</b> Для разработки мобильных приложений под iOS, вы можете использовать следующие языки программирования:\n"
        "1. [Swift](https://developer.apple.com/swift/)\n"
        "2. [Objective-C](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/Introduction/Introduction.html)"
    )
    await bot.send_message(callback_query.from_user.id, text, parse_mode='html')

@dp.callback_query_handler(text="mobile_android")
async def mobile_android(callback_query: types.CallbackQuery):
    await callback_query.answer()
    text = (
        "<b>Android-приложения.</b> Для разработки мобильных приложений под Android, вы можете использовать язык программирования:\n"
        "1. [Java](https://developer.android.com/studio/index.html)\n"
        "2. [Kotlin](https://developer.android.com/kotlin)"
    )
    await bot.send_message(callback_query.from_user.id, text, parse_mode='html')

@dp.message_handler(text="Блокчейн и криптовалюты")
async def blockchain_and_crypto_handler(message: types.Message):
    text = (
        "<b>Блокчейн и криптовалюты.</b> Выберите подкатегорию в области блокчейн-технологий и криптовалют:"
    )
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    buttons = [
        types.InlineKeyboardButton(text="Разработка на блокчейне", callback_data="blockchain_dev"),
        types.InlineKeyboardButton(text="Создание криптовалют", callback_data="crypto_creation"),
    ]
    keyboard.add(*buttons)
    await message.answer(text, parse_mode='html', reply_markup=keyboard)

@dp.callback_query_handler(text="blockchain_dev")
async def blockchain_dev(callback_query: types.CallbackQuery):
    await callback_query.answer()
    text = (
        "<b>Разработка на блокчейне.</b> Для разработки на блокчейне вы можете использовать следующие технологии:\n"
        "1. [Ethereum](https://ethereum.org/)\n"
        "2. [Hyperledger Fabric](https://www.hyperledger.org/use/fabric)\n"
        "3. [Solidity](https://docs.soliditylang.org/)"
    )
    await bot.send_message(callback_query.from_user.id, text, parse_mode='html')

@dp.callback_query_handler(text="crypto_creation")
async def crypto_creation(callback_query: types.CallbackQuery):
    await callback_query.answer()
    text = (
        "<b>Создание криптовалют.</b> Для создания собственной криптовалюты вы можете использовать:\n"
        "1. [Bitcoin](https://bitcoin.org/)\n"
        "2. [Litecoin](https://litecoin.org/)\n"
        "3. [Ripple](https://ripple.com/)"
    )
    await bot.send_message(callback_query.from_user.id, text, parse_mode='html')

@dp.message_handler(text="Системное программирование")
async def system_programming_handler(message: types.Message):
    text = (
        "<b>Системное программирование.</b> Выберите подкатегорию в области разработки системного программного обеспечения:"
    )
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    buttons = [
        types.InlineKeyboardButton(text="Разработка ядра операционной системы", callback_data="kernel_dev"),
        types.InlineKeyboardButton(text="Драйверы устройств", callback_data="device_drivers"),
    ]
    keyboard.add(*buttons)
    await message.answer(text, parse_mode='html', reply_markup=keyboard)

@dp.callback_query_handler(text="kernel_dev")
async def kernel_dev(callback_query: types.CallbackQuery):
    await callback_query.answer()
    text = (
        "<b>Разработка ядра операционной системы.</b> Для разработки ядра операционной системы вы можете использовать следующие технологии и языки программирования:\n"
        "1. [C](https://www.learn-c.org/)\n"
        "2. [Assembly](https://www.assembly.com/)\n"
        "3. [Linux Kernel Development](https://www.kernel.org/)"
    )
    await bot.send_message(callback_query.from_user.id, text, parse_mode='html')

@dp.callback_query_handler(text="device_drivers")
async def device_drivers(callback_query: types.CallbackQuery):
    await callback_query.answer()
    text = (
        "<b>Драйверы устройств.</b> Для разработки драйверов устройств вы можете использовать следующие технологии и языки программирования:\n"
        "1. [C](https://www.learn-c.org/)\n"
        "2. [C++](https://www.learncpp.com/)\n"
    )
    await bot.send_message(callback_query.from_user.id, text, parse_mode='html')


@dp.message_handler(text="Безопасность")
async def security_handler(message: types.Message):
    text = (
        "<b>Безопасность.</b> Выберите подкатегорию в области информационной безопасности:"
    )
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    buttons = [
        types.InlineKeyboardButton(text="Кибербезопасность", callback_data="cybersecurity"),
        types.InlineKeyboardButton(text="Разработка безопасных приложений", callback_data="secure_app_dev"),
    ]
    keyboard.add(*buttons)
    await message.answer(text, parse_mode='html', reply_markup=keyboard)

@dp.callback_query_handler(text="cybersecurity")
async def cybersecurity(callback_query: types.CallbackQuery):
    await callback_query.answer()
    text = (
        "<b>Кибербезопасность.</b> В области кибербезопасности вы можете изучать следующие темы:\n"
        "1. [Этичное взломчестсво (Ethical Hacking)](https://www.eccouncil.org/programs/certified-ethical-hacker-ceh/)\n"
        "2. [Сетевая безопасность](https://www.cisco.com/c/en/us/training-events/training-certifications/certifications/security.html)"
    )
    await bot.send_message(callback_query.from_user.id, text, parse_mode='html')

@dp.callback_query_handler(text="secure_app_dev")
async def secure_app_dev(callback_query: types.CallbackQuery):
    await callback_query.answer()
    text = (
        "<b>Разработка безопасных приложений.</b> При разработке безопасных приложений рекомендуется изучить:\n"
        "1. [OWASP Top Ten](https://owasp.org/www-project-top-ten/)\n"
        "2. [Безопасное программирование (Secure Coding)](https://www.securecoding.cert.org/)\n"
        "3. [Cryptography](https://csrc.nist.gov/projects/cryptographic-standards-and-guidelines)"
    )
    await bot.send_message(callback_query.from_user.id, text, parse_mode='html')

@dp.message_handler(text="Data Science и анализ данных")
async def data_science_handler(message: types.Message):
    text = (
        "<b>Data Science и анализ данных.</b> Выберите подкатегорию в области анализа данных и машинного обучения:"
    )
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    buttons = [
        types.InlineKeyboardButton(text="Машинное обучение", callback_data="machine_learning"),
        types.InlineKeyboardButton(text="Анализ данных", callback_data="data_analysis"),
    ]
    keyboard.add(*buttons)
    await message.answer(text, parse_mode='html', reply_markup=keyboard)

@dp.callback_query_handler(text="machine_learning")
async def machine_learning(callback_query: types.CallbackQuery):
    await callback_query.answer()
    text = (
        "<b>Машинное обучение.</b> Для изучения машинного обучения, вы можете ознакомиться с следующими ресурсами:\n"
        "1. [Coursera: Машинное обучение от Andrew Ng](https://www.coursera.org/learn/machine-learning)\n"
        "2. [TensorFlow](https://www.tensorflow.org/)\n"
        "3. [Scikit-learn](https://scikit-learn.org/)"
    )
    await bot.send_message(callback_query.from_user.id, text, parse_mode='html')

@dp.callback_query_handler(text="data_analysis")
async def data_analysis(callback_query: types.CallbackQuery):
    await callback_query.answer()
    text = (
        "<b>Анализ данных.</b> При изучении анализа данных, полезными будут следующие ресурсы:\n"
        "1. [Coursera: Специализация по анализу данных](https://www.coursera.org/specializations/data-science-python)\n"
        "2. [Pandas](https://pandas.pydata.org/)\n"
        "3. [Matplotlib](https://matplotlib.org/)"
    )
    await bot.send_message(callback_query.from_user.id, text, parse_mode='html')

@dp.message_handler(text="DevOps")
async def devops_skills_handler(message: types.Message):
    text = (
        "<b>Навыки DevOps.</b>\n\n"
        "1. Soft Skills: Коммуникация, сотрудничество, решение проблем.\n"
        "2. Системы управления версиями: Git, SVN.\n"
        "3. CI/CD: Jenkins, GitLab CI, Travis CI.\n"
        "4. Контейнеры: Docker, Kubernetes.\n"
        "5. Автоматизация: Ansible, Puppet, Chef.\n"
        "6. Облако: AWS, Azure, Google Cloud.\n"
        "7. Тестирование: Unit-тестирование, интеграционное тестирование.\n"
        "8. Безопасность: Основы безопасности, обеспечение безопасности CI/CD.\n"
        "9. Платформы: Операционные системы, виртуализация.\n"
        "10. Программирование: Основы скриптования (Bash, Python).\n"
        "11. Сети: Основы сетевых технологий.\n"
        "12. Инструменты DevOps: Terraform, Ansible, Jenkins, Git.\n"
        "\nРекомендуется изучить каждый из указанных скиллов для успешной работы в области DevOps."
    )
    await message.answer(text, parse_mode='html')


@dp.message_handler(text="Компьютерная графика")
async def computer_graphics_handler(message: types.Message):
    text = (
        "<b>Компьютерная графика.</b> Выберите подкатегорию в области компьютерной графики:"
    )
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    buttons = [
        types.InlineKeyboardButton(text="2D Графика", callback_data="2d_graphics"),
        types.InlineKeyboardButton(text="3D Графика", callback_data="3d_graphics"),
    ]
    keyboard.add(*buttons)
    await message.answer(text, parse_mode='html', reply_markup=keyboard)

@dp.callback_query_handler(text="2d_graphics")
async def two_dimensional_graphics(callback_query: types.CallbackQuery):
    await callback_query.answer()
    text = (
        "<b>2D Графика.</b> Для работы с 2D графикой рекомендуется изучить следующие технологии:\n"
        "1. [Adobe Photoshop](https://www.adobe.com/products/photoshop.html)\n"
        "2. [CorelDRAW](https://www.coreldraw.com/)\n"
        "3. [Inkscape](https://inkscape.org/)"
    )
    await bot.send_message(callback_query.from_user.id, text, parse_mode='html')

@dp.callback_query_handler(text="3d_graphics")
async def three_dimensional_graphics(callback_query: types.CallbackQuery):
    await callback_query.answer()
    text = (
        "<b>3D Графика.</b> При работе с 3D графикой полезно изучить следующие технологии:\n"
        "1. [Autodesk Maya](https://www.autodesk.com/products/maya/overview)\n"
        "2. [Blender](https://www.blender.org/)\n"
        "3. [Cinema 4D](https://www.maxon.net/en/cinema-4d)"
    )
    await bot.send_message(callback_query.from_user.id, text, parse_mode='html')


@dp.message_handler(text="Интернет вещей (IoT)")
async def iot_handler(message: types.Message):
    text = (
        "<b>Интернет вещей (IoT).</b> Выберите подкатегорию в области IoT:"
    )
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    buttons = [
        types.InlineKeyboardButton(text="Устройства IoT", callback_data="iot_devices"),
        types.InlineKeyboardButton(text="Программирование для IoT", callback_data="iot_programming"),
    ]
    keyboard.add(*buttons)
    await message.answer(text, parse_mode='html', reply_markup=keyboard)

@dp.callback_query_handler(text="iot_devices")
async def iot_devices(callback_query: types.CallbackQuery):
    await callback_query.answer()
    text = (
        "<b>Устройства IoT.</b> При работе с устройствами IoT полезно изучить следующие технологии:\n"
        "1. [Raspberry Pi](https://www.raspberrypi.org/)\n"
        "2. [Arduino](https://www.arduino.cc/)\n"
        "3. [ESP8266](https://www.espressif.com/en/products/socs/esp8266)"
    )
    await bot.send_message(callback_query.from_user.id, text, parse_mode='html')

@dp.callback_query_handler(text="iot_programming")
async def iot_programming(callback_query: types.CallbackQuery):
    await callback_query.answer()
    text = (
        "<b>Программирование для IoT.</b> При программировании для IoT рекомендуется изучить следующие языки и платформы:\n"
        "1. [MicroPython](https://micropython.org/)\n"
        "2. [Node-RED](https://nodered.org/)\n"
        "3. [PlatformIO](https://platformio.org/)"
    )
    await bot.send_message(callback_query.from_user.id, text, parse_mode='html')


@dp.message_handler(text="Другое")
async def other_handler(message: types.Message):
    text = (
        "<b>Другие темы.</b> Выберите интересующую вас тему из области IT:"
        "\n1. Разработка игр"
        "\n2. Различные языки программирования"
        "\n3. Архитектура ПО"
        "\n4. Другие темы"
    )
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    buttons = [
        types.InlineKeyboardButton(text="Разработка игр", callback_data="game_development"),
        types.InlineKeyboardButton(text="Различные языки программирования", callback_data="misc_languages"),
        types.InlineKeyboardButton(text="Архитектура ПО", callback_data="software_architecture"),
        types.InlineKeyboardButton(text="Другие темы", callback_data="other_topics"),
    ]
    keyboard.add(*buttons)
    await message.answer(text, parse_mode='html', reply_markup=keyboard)

@dp.callback_query_handler(text="game_development")
async def game_development(callback_query: types.CallbackQuery):
    await callback_query.answer()
    text = (
        "<b>Разработка игр.</b> При разработке игр полезно изучить следующие технологии:\n"
        "1. [Unity](https://unity.com/)\n"
        "2. [Unreal Engine](https://www.unrealengine.com/)\n"
        "3. [Godot Engine](https://godotengine.org/)"
    )
    await bot.send_message(callback_query.from_user.id, text, parse_mode='html')

@dp.callback_query_handler(text="misc_languages")
async def misc_languages(callback_query: types.CallbackQuery):
    await callback_query.answer()
    text = (
        "<b>Различные языки программирования.</b> Рекомендую вам изучит один из этих  язык программирование:"
    )
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    buttons = [
        types.InlineKeyboardButton(text="Python", callback_data="python_language"),
        types.InlineKeyboardButton(text="Rust", callback_data="rust_language"),
    ]
    keyboard.add(*buttons)
    await bot.send_message(callback_query.from_user.id, text, parse_mode='html', reply_markup=keyboard)

@dp.callback_query_handler(text="python_language")
async def python_language(callback_query: types.CallbackQuery):
    await callback_query.answer()
    text = (
        "<b>Python.</b> Язык программирования Python широко используется для разработки веб-приложений, научных вычислений, искусственного интеллекта и многого другого.\n"
        "1. [Официальный сайт Python](https://www.python.org/)\n"
        "2. [Learn Python - Codecademy](https://www.codecademy.com/learn/learn-python)"
    )
    await bot.send_message(callback_query.from_user.id, text, parse_mode='html')

@dp.callback_query_handler(text="rust_language")
async def rust_language(callback_query: types.CallbackQuery):
    await callback_query.answer()
    text = (
        "<b>Rust.</b> Язык программирования Rust известен своей производительностью и безопасностью. Он часто используется для системного программирования и разработки надежных приложений.\n"
        "1. [Официальный сайт Rust](https://www.rust-lang.org/)\n"
        "2. [Rust by Example](https://doc.rust-lang.org/rust-by-example/)"
    )
    await bot.send_message(callback_query.from_user.id, text, parse_mode='html')

@dp.callback_query_handler(text="software_architecture")
async def software_architecture(callback_query: types.CallbackQuery):
    await callback_query.answer()
    text = (
        "<b>Архитектура программного обеспечения.</b> Выберите аспект архитектуры программного обеспечения для получения дополнительной информации:"
    )
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    buttons = [
        types.InlineKeyboardButton(text="Микросервисная архитектура", callback_data="microservices_architecture"),
        types.InlineKeyboardButton(text="Событийно-ориентированная архитектура", callback_data="event_driven_architecture"),
    ]
    keyboard.add(*buttons)
    await bot.send_message(callback_query.from_user.id, text, parse_mode='html', reply_markup=keyboard)

@dp.callback_query_handler(text="microservices_architecture")
async def microservices_architecture(callback_query: types.CallbackQuery):
    await callback_query.answer()
    text = (
        "<b>Микросервисная архитектура.</b> Микросервисы представляют собой подход к разработке программного обеспечения, при котором приложение состоит из небольших и независимых служб.\n"
        "1. [Микросервисная архитектура - Martin Fowler](https://martinfowler.com/articles/microservices.html)\n"
        "2. [Building Microservices - O'Reilly](https://www.oreilly.com/library/view/building-microservices/9781491950357/)"
    )
    await bot.send_message(callback_query.from_user.id, text, parse_mode='html')

@dp.callback_query_handler(text="event_driven_architecture")
async def event_driven_architecture(callback_query: types.CallbackQuery):
    await callback_query.answer()
    text = (
        "<b>Событийно-ориентированная архитектура.</b> Этот подход основан на обмене сообщениями и реагировании на события в системе.\n"
        "1. [Event-Driven Architecture - Microsoft Docs](https://docs.microsoft.com/en-us/azure/architecture/guide/architecture-styles/event-driven)\n"
        "2. [Event-Driven Microservices - Red Hat](https://www.redhat.com/architect/event-driven-microservices-architecture-ebook)"
    )
    await bot.send_message(callback_query.from_user.id, text, parse_mode='html')

@dp.callback_query_handler(text="other_topics")
async def other_topics(callback_query: types.CallbackQuery):
    await callback_query.answer()
    text = (
        "<b>Учись тому, что есть в пунктах выше.</b> Предлагаем вам обучиться и практиковаться в темах, представленных в предыдущих разделах. Возможно, вы найдете что-то новое и интересное для себя!\n"
        "Не стесняйтесь погружаться в разные области и экспериментировать."
    )
    await bot.send_message(callback_query.from_user.id, text, parse_mode='html')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
