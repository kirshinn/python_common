from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# 1 способ создания клавиатуры
keyboard_start = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Меню'),
            KeyboardButton(text='О магазине'),
        ],
        [
            KeyboardButton(text='Варианты оплаты'),
            KeyboardButton(text='Варианты доставки'),
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='Что вас интересует?',
)

# способ удаления клавиатуры
keyboard_delete = ReplyKeyboardRemove()

# 2 способ создания клавиатуры
keyboard_start_builder = ReplyKeyboardBuilder()

keyboard_start_builder.add(
    KeyboardButton(text='Меню'),
    KeyboardButton(text='О магазине'),
    KeyboardButton(text='Варианты оплаты'),
    KeyboardButton(text='Варианты доставки'),
)

keyboard_start_builder.adjust(2, 2)

# расширение существующей клавиатуры
keyboard_start_builder_attach = ReplyKeyboardBuilder()

keyboard_start_builder_attach.attach(keyboard_start_builder)

keyboard_start_builder_attach.row(
    KeyboardButton(text='Оставить отзыв'),
)

# клавиатура с запросом номера и местоположения
keyboard_query = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Создать Опрос', request_poll=KeyboardButtonPollType()),
            KeyboardButton(text='Отправить номер', request_contact=True),
            KeyboardButton(text='Отправить местоположение', request_location=True),
        ],
    ],
    resize_keyboard=True,
)
