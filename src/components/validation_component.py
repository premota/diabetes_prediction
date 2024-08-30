from src.config.entity_config import DataSchemaConfig
from src.utils.exception import CustomException
from src.utils.logger import logging

import sys

import pandas as pd


class DataValidationComponent():
    def __init__(self, config: DataSchemaConfig) -> None:
        self.config = config.data_schema_validation
        self.data = pd.read_csv(config.data)

    def validate_features(self):
        try:
            logging.info("validating features initiated")
            data_features = set(self.data.columns)
            schema_features = set(self.config.keys())
            logging.info("checking for unwanted and missing features")
            unwanted_features = data_features -  schema_features
            missing_features = schema_features - data_features

            if unwanted_features:
                raise ValueError(f"the following features are in the data but not in the schema {unwanted_features}")
            
            if missing_features:
                raise ValueError(f"the following features are missing in your data {missing_features}")
            logging.info("features validation completed")
            return self.data
        
        except Exception as e:
            raise CustomException(e,sys)
    

    def validate_data_types(self):
        try:
            logging.info("data types validation initiated")
            datatype_map = self.config
            data = self.data.astype(datatype_map)
            logging.info("data types validation completed")
            return data

        except KeyError as e:
            raise CustomException(f"column mismatch error: {e}", sys)
        except ValueError as e:
            raise CustomException(f"Data type conversion error: {e}", sys)
        except Exception as e:
            raise CustomException(e,sys)
    

            
