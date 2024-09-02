import sys


from src.utils.exception import CustomException
from src.components.transformation_component import DataTransformationComponent
from src.config.config_manager import ConfigManager




class DataTransformationPipeline:
    def __init__(self, data):
        self.data = data

    def transform_data(self):
        try:
            # get transformation config
            config_obj = ConfigManager().get_data_transformation_config()
            # transformation component
            transform_component = DataTransformationComponent(data=self.data, 
                                                              config=config_obj)
            
            #initiate data trasformation
            transform_component.initiate_data_transformation()
        except Exception as e:
            raise CustomException(e,sys)


if __name__ == "__main__":
    from src.pipelines.data_validation_pipeline import DataValidationPipeline

    obj = DataValidationPipeline()
    df = obj.validate_data()

    trans_obj = DataTransformationPipeline(df)
    trans_obj.transform_data()