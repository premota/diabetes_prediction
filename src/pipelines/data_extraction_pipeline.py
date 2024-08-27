from src.config.config_manager import ConfigManager
from src.components.extraction_component import Extract
from src.utils.exception import CustomException

import sys


class ExtractionPipeline:
    def __init__(self):
        pass

    def extract_data(self):
        try:
            config_obj = ConfigManager()
            injestion_config = config_obj.get_extraction_config()
            extract_obj = Extract(config=injestion_config)
            extract_obj.extract_data()
        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    obj = ExtractionPipeline()
    obj.extract_data()