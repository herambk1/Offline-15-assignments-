import csv
import logging


def read_csv_file(filename):

    data = []

    try:

        with open(filename, "r") as file:

            reader = csv.DictReader(file)

            for row in reader:
                data.append(row)

        logging.info("CSV file read successfully")
        print("CSV file read successfully")

    except Exception as e:

        logging.error("CSV reading error: %s", e)
        print("CSV reading error:", e)

    return data