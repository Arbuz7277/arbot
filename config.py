# config.py
from pathlib import Path
from dataclasses import dataclass

@dataclass
class Config:
    logs: Path = Path("logs")
    log_file_name: str = "app.log"
    log_format: str = "[%(asctime)s %(levelname)s] : %(name)s  - %(message)s"

    logs.mkdir(parents=True, exist_ok=True)

config = Config()
