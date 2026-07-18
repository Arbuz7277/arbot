# handlers/start.py
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from keyboards.inline import main_menu

router = Router()

@router.message(CommandStart())
async def start(msg: Message) -> None:
    await msg.answer("Hello!", reply_markup=main_menu())
