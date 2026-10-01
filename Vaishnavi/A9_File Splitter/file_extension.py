import os
from log_utils.log_config import log_confing
logger = log_confing(str(__file__).split("\\")[-1])

def file_ext(source,file):
    extension_file  = os.path.join(source,file)
    extension = extension_file.split("\\")[-1].split(".")[-1]
    logger.info("Extension found for %s: %s", file, extension)
    return extension