from models.config_model import Settings
import os
from pathlib import Path
from utilities.deserialize_json import DeserializeJson


class ConfigManager:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    config_file_path = Path(os.path.join(BASE_DIR, "../resourses", "config.json")).resolve()

    @classmethod
    def get_config_data(cls):
        return Settings.model_validate_json(DeserializeJson().deserialize_json(cls.config_file_path))
