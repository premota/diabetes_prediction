from pathlib import Path
import yaml

from box import Box
import sys
import os

from src.utils.exception import CustomException



def read_yaml(path: Path) -> Box:
    try:
        with open(path) as file:
            data = yaml.safe_load(file)
            return Box(data)
    except Exception as e:
        raise CustomException(e,sys)
    
def create_folder(path: Path):
    try:
        os.makedirs(path, exist_ok = True)
    except Exception as e:
        raise CustomException(e, sys)