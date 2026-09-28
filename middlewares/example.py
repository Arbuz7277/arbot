# middlewares/example.py

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from typing import Callable, Dict, Any, Awaitable

class ExampleMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        data: Dict[str, Any]
    ) -> Any:
        # Any logic

        # Let's pass control on
        return await handler(evenv, data)

