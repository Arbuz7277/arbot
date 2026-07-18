# callbacks/__init__.py
from aiogram import Router, Dispatcher
from .about import router as about_router

router = Router()

def include_callbacks(dp: Dispatcher) -> None:
    router.include_router(about_router)

    dp.include_router(router)
