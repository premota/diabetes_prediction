from src.config.config_manager import ConfigManager
from src.components.validation_component import DataValidationComponent
from src.utils.exception import CustomException

import sys


class DataValidationPipeline:
    def __init__(self) -> None:
        pass
        
    def validate_data(self):
        try:
            config_obj = ConfigManager()
            validation_config = config_obj.get_schema_validation_config()
            validation_obj = DataValidationComponent(config = validation_config)
            
            #validate features
            df = validation_obj.validate_features()

            #validate datatypes
            df = validation_obj.validate_data_types(df)
            return df

        except Exception as e:
            raise CustomException(e,sys)









