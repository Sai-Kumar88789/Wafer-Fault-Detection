import logging as lg 
import os
from datetime import datetime


LOG_FILE = f"{datetime.now().strftime('%m_%d_%y_%H_%M_%S')}.log"

LOG_PATH = os.path.join(os.getcwd(),"logs",LOG_FILE)

os.makedirs(LOG_PATH,exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_PATH,LOG_FILE)

lg.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)s %(name)s - %(levelname)s - %(message)s",
    level= lg.INFO,
)
