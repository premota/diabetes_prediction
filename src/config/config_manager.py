from yaml_config.yaml_path import PIPELINE_CONFIG_PATH
from src.config.entity_config import (DataExtractionConfig, DataSchemaConfig,
                                      DataTransformationConfig)

from src.utils.util import read_yaml, create_folder
from src.utils.exception import CustomException
from src.utils.logger import logging

import sys

class ConfigManager:
    # changes
        # changes

    def get_extraction_config(self)-> DataExtractionConfig:
        try:
            logging.info("collecting extraction config")
            config = self.pipeline_config.data_extraction
            data_extraction_config = DataExtractionConfig(source_url = config.source_url,
                                                        prefix = config.prefix,
                                                        local_data_file = config.local_data_file,
                                                        local_load_dir = config.local_load_dir)
            logging.info("extraction config completed")
            return data_extraction_config
        except Exception as e:
            raise CustomException(e,sys)


    def get_schema_validation_config(self)-> DataSchemaConfig:
        try:
            data_path = self.pipeline_config.data_extraction.local_data_file
            logging.info("collecting schema validation config")
            config = self.pipeline_config.data_schema_validation
            data_schema_validation_config = DataSchemaConfig(data_schema_validation= config, data=data_path)
            logging.info("validation config completed")
            return data_schema_validation_config
        except Exception as e:
            raise CustomException(e, sys)
        

    def get_data_transformation_config(self)-> DataTransformationConfig:
        try:
            config = self.pipeline_config.data_transformation
            transformation_config = DataTransformationConfig(transformation_artifact_file=config.transformation_artifact_file,
                                                        target_feature = config.target_feature)
            logging.info("transformation config completed")
            return transformation_config

        except Exception as e:
            raise CustomException(e,sys)