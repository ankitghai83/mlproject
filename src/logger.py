import logging
# Any execution happen , we need log all that information in some files.So that we should be able to track if there is any error even 
# the custom exception error we should log that in txt file.
import os
from datetime import datetime
# creating the log file name with below naming convention

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# Create path where log file will save . Here we are creating the folders like pwd>logs>folder with above naming convention and then above log file
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
# Even though there are files & folders, when new log file created . keep on appending the same in the location
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

# To overwrite the functionality of logging we need to set that up in the logging.basicconfig
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,



)

'''
if  __name__=="__main__":
    logging.info("Logging has started")'''