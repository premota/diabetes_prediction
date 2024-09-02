import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder

from src.config.config_manager import DataTransformationConfig
from src.utils.exception import CustomException
from src.utils.logger import logging
from src.utils.util import save_to_pickle

import sys

class DataTransformationComponent:
    def __init__(self, data: pd.DataFrame, config: DataTransformationConfig) -> None:
        self.config = config
        self.data  = data

    def initiate_data_transformation(self):
        try:
            logging.info("data transformation started")
            logging.info(f"data dimension before transformatiom: {self.data.shape} ")
            df = self.data.copy()
            target_feature = self.config.target_feature

            # remove target feature
            df = df.drop([target_feature], axis=1)

            # select numerical and categorical features
            numerical_features = df.select_dtypes(exclude = "object").columns.to_list()
            categorical_features = df.select_dtypes(include = "object").columns.to_list()
            
            logging.info("importing numerical and categorical data transformers")
            # Transformers
            numerical_transformer = MinMaxScaler()
            categorical_transformer = OneHotEncoder(drop = 'if_binary')
            
            # define column transformer object
            pipeline = ColumnTransformer(
            [
            ("numerical transformer", numerical_transformer, numerical_features),
            ("categorical transformer", categorical_transformer, categorical_features)
            ])
            
            # apply transformer
            transformed_array = pipeline.fit_transform(df)
            
            # Get the transformed column names
            transformed_numerical_columns = pipeline.transformers_[0][2]
            transformed_categorical_columns = pipeline.transformers_[1][1].get_feature_names_out(input_features=categorical_features)
            
            # Combine numerical and categorical transformed column names
            transformed_column_names = list(transformed_numerical_columns) + list(transformed_categorical_columns)
            
            # convert array to dataframe
            transformed_data = pd.DataFrame(transformed_array, columns=transformed_column_names)
            
            
            # attach target feature
            transformed_data[target_feature] = self.data[target_feature]
            logging.info(f"transformation completed, data dimension: {transformed_data.shape}")

            save_to_pickle(obj_path=self.config.transformation_artifact_file, obj=pipeline)
            logging.info("transformer object saved as pickle file")

            return transformed_data
            
        except Exception as e:
            raise CustomException(e,sys)
