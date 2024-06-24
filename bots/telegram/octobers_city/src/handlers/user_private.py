from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command, or_f

from filters.chat_types import ChatTypeFilter
from keyboards import reply

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))


@user_private_router.message(CommandStart())
async def cmd_start(message: types.Message) -> None:
    await message.answer('Привет, я виртуальный помощник!', reply_markup=reply.keyboard_start)


@user_private_router.message(or_f(Command('menu'), F.text.lower() == 'меню'))
async def cmd_menu(message: types.Message) -> None:
    await message.answer('меню')
