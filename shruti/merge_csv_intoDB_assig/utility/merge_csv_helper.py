import os
import csv
import json
from email import header

from utility.logger import logger

logger = logger(__name__)

def read_config(filename):
    try:
        with open(filename) as f:
            config = json.load(f)
        return config
    except Exception as e:
        logger("{} file not found ".format(filename,e))

def get_all_csv_files(input_dir):
    try:
        files = os.listdir(input_dir)
        csv_files = []

        for file in files:
            if file.endswith(".csv"):
                csv_files.append(os.path.join(input_dir, file))

        return csv_files

    except Exception as e:
        logger.error("{} file not found: {}".format(input_dir, e))
        return []

def merge_csv_files(csv_files):
    try:
        header = None
        data = []

        for file in csv_files:

            with open(file, newline="") as fp:
                reader = csv.reader(fp)

                current_header = next(reader)

                if header is None:
                    header = current_header

                elif current_header != header:
                    logger.error("Header does not match: {}".format(file))
                    continue

                for row in reader:
                    data.append(row)

        logger.info("Total records: {}".format(len(data)))

        return header, data

    except Exception as e:
        logger.error("File not merged: {}".format(e))
        return None, None

def write_merged_csv(filename, header, data):
    try:
        with open(filename, "w", newline="") as fp:

            writer = csv.writer(fp)

            writer.writerow(header)
            writer.writerows(data)

        logger.info("{} merged file created".format(filename))

    except Exception as e:
        logger.error("File not written: {}".format(e))





