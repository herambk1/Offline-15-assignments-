import os
from log_utils.log_config import log_confing
logger = log_confing(str(__file__).split("\\")[-1])

def fetch_files(source):
    logger.info("Fetching files from source")
    file_list = [file for file in os.listdir(source)]
    logger.info("Files fetched successfully")
    return file_list
