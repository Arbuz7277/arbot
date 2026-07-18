# main.py
from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from handlers import include_handlers
from callbacks import include_callbacks
from config import config
from dotenv import load_dotenv
import logging
import sys
import os
import asyncio
import time

logging.basicConfig(
    level=logging.INFO,
    format=config.log_format,
    handlers=[
        logging.FileHandler(config.logs / config.log_file_name, encoding='utf-8'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# Загрузка апи
load_dotenv()
api_bot = os.getenv("API_BOT")

async def main(api_bot: str | None = None) -> None:
    """Точка входа бота."""
    if api_bot == None:
        logger.critical("api_bot is None. Save the bot's API to a variable. If you don't have one, look it up in the @BotFather.")
        sys.exit(1)
    
    bot = Bot(token=api_bot)
    dp = Dispatcher()
    
    include_handlers(dp)
    include_callbacks(dp)
    
    try:
        logger.info("Bot running")
        await dp.start_polling(bot)
    except Unauthorized:
        logger.critical("API is not valid")
        sys.exit(1)


if __name__ == '__main__':
    asyncio.run(main(api_bot))

