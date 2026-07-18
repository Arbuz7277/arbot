# handlers/ping.py
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
import time

router = Router()

@router.message(Command("ping"))
async def ping(msg: Message) -> None:
    """Выводит пинг"""
    st = time.monotonic_ns()  # Не зависит от времени
    await msg.bot.get_me()
    ping = (time.monotonic_ns() - st) / 1_000_000  # В мс
    
    await msg.answer(f"⚡ Ping: {ping:,.2f} ms")


