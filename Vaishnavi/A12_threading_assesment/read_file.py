import csv
from log_utils.log_config import custom_log
logger = custom_log(str(__file__).split("\\")[-1])

def read_file(filename):

    try:
        logger.info("Reading file: {}".format(filename))

        with open("{}".format(filename))as fp:
            reader = csv.DictReader(fp)
            data = list(reader)

        logger.info("File read successfully: {}".format(filename))

        return data

    except Exception as e:
        logger.error("Error while reading file: {}".format(e))
        print(e)

