import gdown

from src.config.entity_config import DataExtractionConfig
from src.utils.exception import CustomException
from src.utils.logger import logging
from src.utils.util import create_folder

import sys


class ExtractionComponent():
    def __init__(self, config: DataExtractionConfig):
        self.config = config

    
    def extract_data(self):
        try:
            logging.info("data extraction initiated")
            url = self.config.source_url
            prefix = self.config.prefix
            data_path = self.config.local_data_file
            extraction_dir = self.config.local_load_dir
            file_id = url.split("/")[-2]

            logging.info("data extraction folder created")
            create_folder(extraction_dir)

            logging.info("download about to begin")
            gdown.download(prefix + file_id, data_path)
            logging.info("extraction completed")
        except Exception as e:
            raise CustomException(e,sys)
        
