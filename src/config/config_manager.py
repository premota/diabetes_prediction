from yaml_config.yaml_path import PIPELINE_CONFIG_PATH
from src.config.entity_config import DataExtractionConfig
from src.utils.util import read_yaml, create_folder
from src.utils.exception import CustomException
from src.utils.logger import logging

import sys

class ConfigManager:
    def __init__(self, pipline_config = PIPELINE_CONFIG_PATH):
        self.pipeline_config = read_yaml(pipline_config)

    
    def get_extraction_config(self)-> DataExtractionConfig:
        try:
            logging.info("collecting extraction config")
            config = self.pipeline_config.data_extraction
            logging.info("data extraction folder created")
            create_folder(config.local_load_dir)

            data_extraction_config = DataExtractionConfig(source_url = config.source_url,
                                                        prefix = config.prefix,
                                                        local_data_file = config.local_data_file,
                                                        local_load_dir = config.local_load_dir)
            logging.info("extraction config completed")
            return data_extraction_config
        except Exception as e:
            raise CustomException(e,sys)

