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
            validation_obj.validate_features()

            #validate datatypes
            validation_obj.validate_data_types()

        except Exception as e:
            raise CustomException(e,sys)



if __name__ == "__main__":
    obj = DataValidationPipeline()
    obj.validate_data()









