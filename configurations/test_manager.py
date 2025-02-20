import os
from pathlib import Path
from utilities.deserialize_json import DeserializeJson
from models.test_data_model import DataModel

class TestManager:
    BASE_DIR = os.path.dirname(os.getcwd())
    config_file_path = Path(os.path.join(BASE_DIR, "pythonProject3/resourses/test_data.json")).resolve()

    @classmethod
    def get_test_data(cls):
        return DataModel.model_validate_json(DeserializeJson().deserialize_json(cls.config_file_path))
