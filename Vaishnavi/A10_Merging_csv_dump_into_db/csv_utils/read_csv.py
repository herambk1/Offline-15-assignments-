from log_utils.log_config_data import log_config

logger = log_config(str(__file__).split("\\")[-1])
import csv
def read_csv_file(source,file):
    logger.info("Reading CSV file: {}".format(file))
    try:
        with open(r"{}\{}".format(source,file),'r',newline='') as fp:
            reader = csv.DictReader(fp)
            data = list(reader)
        logger.info("CSV file read successfully: {}".format(file))
        return data

    except Exception as e:
        logger.error("Error while reading CSV file {}: {}".format(file, e))
