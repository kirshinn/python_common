from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command, or_f
from aiogram.enums import ParseMode

from filters.chat_types import ChatTypeFilter
from keyboards import reply

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))


@user_private_router.message(CommandStart())
async def cmd_start(message: types.Message) -> None:
    await message.answer('Привет, я виртуальный помощник!',
                         reply_markup=reply.keyboard_start_builder_attach.as_markup(
                             resize_keyboard=True,
                             input_field_placeholder='Что вас интересует?',
                         ))


@user_private_router.message(or_f(Command('menu'), F.text.lower() == 'меню'))
async def cmd_menu(message: types.Message) -> None:
    await message.answer('меню', reply_markup=reply.keyboard_delete)


@user_private_router.message(Command('about'))
async def cmd_menu(message: types.Message) -> None:
    await message.answer('о магазине')


@user_private_router.message(Command('payment'))
@user_private_router.message(F.text, F.text.lower().contains('оплат'))
async def cmd_menu(message: types.Message) -> None:
    await message.answer('варианты оплаты')


@user_private_router.message(Command('shipping'))
@user_private_router.message(F.text, F.text.lower().contains('доставк'))
async def cmd_menu(message: types.Message) -> None:
    await message.answer('<b>варианты доставки</b>', parse_mode=ParseMode.HTML)


@user_private_router.message(F.contact)
async def get_contact(message: types.Message) -> None:
    await message.answer(f'номер получен')
    await message.answer(str(message.contact))


@user_private_router.message(F.location)
async def get_location(message: types.Message) -> None:
    await message.answer(f'локация получена')
    await message.answer(str(message.location))
