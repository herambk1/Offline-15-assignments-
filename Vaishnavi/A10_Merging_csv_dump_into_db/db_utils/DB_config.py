import json
from log_utils.log_config_data import log_config

logger = log_config(str(__file__).split("\\")[-1])


def read_config_file(filename):
    logger.info("Reading config file: {}".format(filename))
    try:
        with open(filename) as fp:
            data = json.load(fp)

        logger.info("Config file read successfully")
        return data

    except Exception as e:
        logger.error("Error while reading config file: {}".format(e))
