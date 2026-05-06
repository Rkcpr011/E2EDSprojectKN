import logging
import os
from datetime import datetime

# log file ka nam
LOG_FILE_NAME=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# log folder ka nam
LOG_DIR_NAME=os.path.join(os.getcwd(),"logs")
# log folder bn gya
os.makedirs(LOG_DIR_NAME,exist_ok=True)

# log file ko kaha rakhna hai
LOG_FILE_PATH=os.path.join(LOG_DIR_NAME,LOG_FILE_NAME)


# log file ka creation
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

