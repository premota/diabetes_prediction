import pandas as pd

from src.utils.exception import CustomException

import sys

class Extract():
    def __init__(self, data_frame):
        self.data_frame = data_frame
        self.url = 

    
    def extract_data(self):
        try:
            data = pd.read_csv()

        except Exception as e:
            raise CustomException(e,sys)
