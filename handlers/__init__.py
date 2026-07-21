# handlers/__init__.py

"""
Инициализатор хендлеров.
"""

from aiogram import Router, Dispatcher
from .start import router as start_router
from .ping import router as ping_router
from .gen_password import router as gen_password_router

router = Router()

def include_handlers(dp: Dispatcher) -> None:
    router.include_router(start_router)
    router.include_router(ping_router)
    router.include_router(gen_password_router)

    dp.include_router(router)
