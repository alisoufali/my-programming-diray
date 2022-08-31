import json
from pathlib import Path
from typing import Optional


class Configs:

    DEFAULT_CONFIG_PATH = Path("./config.json").resolve()
    DEFAULT_DATABASE_PATH = Path("./data/data.db").resolve()

    @classmethod
    def load_configs(cls, config_path: Optional[Path] = None) -> None:
        if config_path is None:
            config_path = cls.DEFAULT_CONFIG_PATH
        with open(file=config_path, mode="r") as config_file:
            config_data = json.load(fp=config_file)
        cls.DATABASE_PATH = config_data.get(
            "database_path", cls.DEFAULT_DATABASE_PATH)
