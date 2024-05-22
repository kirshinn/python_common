from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command, or_f

from filters.chat_types import ChatTypeFilter

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))


@user_private_router.message(CommandStart())
async def cmd_start(message: types.Message) -> None:
    await message.answer('Привет, я виртуальный помощник!')


@user_private_router.message(or_f(Command('menu'), F.text.lower() == 'меню'))
async def cmd_menu(message: types.Message) -> None:
    await message.answer('меню')


@user_private_router.message(Command('about'))
async def cmd_menu(message: types.Message) -> None:
    await message.answer('о нас')


@user_private_router.message(Command('payment'))
@user_private_router.message(F.text, F.text.lower().contains('оплат'))
async def cmd_menu(message: types.Message) -> None:
    await message.answer('оплата')


@user_private_router.message(Command('shipping'))
@user_private_router.message(F.text, F.text.lower().contains('доставк'))
async def cmd_menu(message: types.Message) -> None:
    await message.answer('варианты доставки')
