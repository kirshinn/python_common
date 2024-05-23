from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard_start = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Меню'),
            KeyboardButton(text='О магазине'),
            KeyboardButton(text='Варианты оплаты'),
            KeyboardButton(text='Варианты доставки'),
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='Что вас интересует?',
)
