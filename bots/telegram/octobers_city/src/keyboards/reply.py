from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard_start = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Меню')
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='Что вас интересует?',
)
