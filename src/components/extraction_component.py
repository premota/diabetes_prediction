import gdown

from src.config.entity_config import DataExtractionConfig
from src.utils.exception import CustomException
from src.utils.logger import logging

import sys

class Extract():
    def __init__(self, config: DataExtractionConfig):
        self.config = config

    
    def extract_data(self):
        try:
            logging.info("data extraction initiated")
            url = self.config.source_url
            prefix = self.config.prefix
            data_path = self.config.local_data_file
            file_id = url.split("/")[-2]
            logging.info("download about to begin")
            gdown.download(prefix + file_id, data_path)
            logging.info("extraction completed")
        except Exception as e:
            raise CustomException(e,sys)
        
