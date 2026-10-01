import os
from log_utils.log_config import log_confing
logger = log_confing(str(__file__).split("\\")[-1])

def write_file(destination,data,file,extension):
    folder = os.path.join(destination, extension)
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, file)

    try:
        logger.info("Writing file: %s", path)
        with open(path, 'wb') as fp:
            fp.write(data)
        logger.info("File written successfully: %s", file)

    except Exception as e:
        logger.error("Error writing file %s: %s", file, e)
        print(e)
