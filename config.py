# config.py

import os
from dotenv import load_dotenv
from pathlib import Path
from dataclasses import dataclass

# Загрузка апи
load_dotenv()
api_bot = os.getenv("API_BOT")

@dataclass
class Config:
    base_dir = Path(__file__).resolve().parent

    api_bot: str = api_bot
    owners: tuple[int] = (0,)  # Telegram ids

    logs: Path = base_dir / "logs"
    log_file_name: str = "app.log"
    log_format: str = "[%(asctime)s %(levelname)s] : %(name)s  - %(message)s"

    data_dir = base_dir / "data"
    db_path: Path = data_dir / "database.db"

    logs.mkdir(parents=True, exist_ok=True)
    data_dir.mkdir(parents=True, exist_ok=True)

config = Config()
