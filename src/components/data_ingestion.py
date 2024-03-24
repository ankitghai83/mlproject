# custom exception calling using below lib
import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd # need to work with dataframe
from sklearn.model_selection import train_test_split
from dataclasses import dataclass # Used to create class variable

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig
from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer


# Any input required by the data ingestion component like saving raw data , saving Test & Train data will be given here. Output of data ingestion
# config class will be like numpy array or file saved at location.
# @dataclass will used as decorator to create class variable inside the datingestionconfig class which otherwise require __init__
# If only variable is required to be defined then use the @dataclass else we can use __init__ for defining the function.

@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join("artifacts","train.csv") # i/p to this class of data ingestion component is folder path where all output of data ingestion component will save
    test_data_path:str=os.path.join("artifacts","test.csv")
    raw_data_path:str=os.path.join("artifacts","data.csv")



class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig() # it will store above 3 path in this class variable wen we call the DataIngestion class,

    def initiate_data_ingestion(self):# This have code to read the data from any source like data base where their client will be set up in utils.py
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv("notebook\data\stud.csv")
            logging.info("Read the dataset as dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info("Ingestion of data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )

        except Exception as e:
            raise CustomException(e,sys)



      
if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()
    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))
             
         

     