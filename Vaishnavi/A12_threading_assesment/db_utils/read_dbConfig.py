import json
from log_utils.log_config import custom_log
logger = custom_log(str(__file__).split("\\")[-1])

def read_dbConfig(filename):

    try:
        logger.info("Reading database configuration")

        with open("{}".format(filename)) as fp:
            data = json.load(fp)

        logger.info("Database configuration read successfully")

        return data

    except Exception as e:
        logger.error("Error while reading database configuration: {}".format(e))
        print(e)
