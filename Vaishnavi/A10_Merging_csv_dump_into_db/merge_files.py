import csv
import os
from log_utils.log_config_data import log_config

logger = log_config(str(__file__).split("\\")[-1])

def merge_csv_file(source, header, data):
    logger.info("Merging CSV data into merged.csv")
    try:
        file = r"{}\{}".format(source, "merged.csv")
        file_exists = os.path.exists(file)

        with open(file, "a", newline='') as fp:
            writter = csv.DictWriter(fp, fieldnames=header)
            if not file_exists:
                writter.writeheader()
                logger.info("Header written to merged.csv")
            writter.writerows(data)

        logger.info("CSV data merged successfully")

    except Exception as e:
        logger.error("Error while merging CSV data: {}".format(e))
        print(e)