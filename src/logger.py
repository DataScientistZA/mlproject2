import logging
import os
from datetime import datetime


# This line MUST be the first line of execution for LOG_FILE
LOG_FILE = f'{datetime.now().strftime("%m_%d_%Y_%H_%M_%S")}.log' 

# Fix the directory/path logic
LOGS_DIR = os.path.join(os.getcwd(), "log") 
os.makedirs(LOGS_DIR, exist_ok=True)
LOG_FILE_PATH = os.path.join(LOGS_DIR, LOG_FILE)

# LOG_FILE = f'{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log'

# logs_path = os.path.join(os.getcwd(), "log", LOG_FILE)
# os.makedirs(logs_path, exist_ok=True)
# LOG_FILE = f'{datetime.now().strftime("%m_%d_%Y_%H_%M_%S")}.log'

# LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format= "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO

)

if __name__ == "__main__":
    logging.info('logging has started')