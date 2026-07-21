# handlers/gen_password.py
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from utils.gen_password import gen_password

router = Router()

@router.message(Command("gen_password"))
async def gen_password(msg: Message) -> None:
    args = msg.text.split()

    if len(args) < 2:
        msg.answer("Использование: /gen_password <длинна>")
        return

    try:
        length = int(args[1])
    except TypeError:
        msg.answer("Длинна должна быть в виде числа!")
        return

    length = max(1, min(256, length))  # 1 <= legth <= 256

    password = gen_password(length)

    msg.answer(f"Пароль: `{password}`", parse_mode="markdown")

