# utils.py : This is one place where we will place all the functionality like function etc. that can be used commonly by the entire project.

import os
import sys
import numpy as np
import pandas as pd
import dill # used to create the .pkl file

from src.logger import logging
from src.exception import CustomException

def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,'wb') as file_obj:
            dill.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)