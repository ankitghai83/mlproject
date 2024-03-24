# utils.py : This is one place where we will place all the functionality like function etc. that can be used commonly by the entire project.

import os
import sys
import numpy as np
import pandas as pd
import dill # used to create the .pkl file

from src.logger import logging
from src.exception import CustomException

from sklearn.metrics import r2_score

def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,'wb') as file_obj:
            dill.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)
    
# Create model_evaluate function that will be called in model trainer
def evaluate_models(X_train,y_train,X_test,y_test,models):
    try:
        report={}
        for i in range(len(models)):
            model=list(models.values())[i]
            model.fit(X_train,y_train) # train model
            y_train_pred=model.predict(X_train)
            y_test_pred=model.predict(X_test)

            train_model_score=r2_score(y_train,y_train_pred)
            test_model_score=r2_score(y_test,y_test_pred)

            report[list(models.keys())[i]]=test_model_score

        return report

    except Exception as e:
        raise CustomException(e,sys)