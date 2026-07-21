# Program 1: Basic Logging
print("Program 1: Basic Logging ")

import logging

logging.basicConfig(
    level = logging.INFO ,
    filename = "app.log" ,
    filemode = "w" ,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("Program Started")
logging.info("User Logged In")
logging.info("User Logged Out")
logging.info("Program Closed")