# callbacks/about.py
from aiogram import Router
from aiogram.types import CallbackQuery


router = Router()

@router.callback_query(lambda c: c.data == "about")
async def about(callback: CallbackQuery) -> None:
    await callback.message.edit_text(
        "О боте\n\n"
        "это бот",
    )
