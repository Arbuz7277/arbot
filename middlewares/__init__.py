# middlewares/__init__.py

from aiogram import Dispatcher

# Import all middlewares
from .example import ExampleMiddleware

OUTER_MIDDLEWARES = [
    ExampleMiddleware,
    # And more...
]

def include_middlewares(dp: Dispatcher) -> None:
    for middleware in OUTER_MIDDLEWARES:
        dp.update.outer_middleware(middleware())

