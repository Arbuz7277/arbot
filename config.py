# config.py
from pathlib import Path
from dataclasses import dataclass

# Загрузка апи
load_dotenv()
api_bot = os.getenv("API_BOT")

@dataclass
class Config:
    api_bot: str = api_bot

    logs: Path = Path("logs")
    log_file_name: str = "app.log"
    log_format: str = "[%(asctime)s %(levelname)s] : %(name)s  - %(message)s"

    logs.mkdir(parents=True, exist_ok=True)

config = Config()
