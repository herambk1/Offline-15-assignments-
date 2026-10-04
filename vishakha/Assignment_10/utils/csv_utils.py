import csv
import os
import logging

def read_csv_files(source_folder):
    all_data = []
    header = None

    try:
        logging.info("Starting CSV file reading")
        files = os.listdir(source_folder)

        for file in files:
            if file.endswith(".csv"):
                file_path = os.path.join(source_folder,file)
                logging.info("Reading CSV file: %s", file)

                with open(file_path, "r") as csv_file:
                    reader = csv.reader(csv_file)
                    current_header = next(reader)

                    # Get header from first file
                    if header is None:
                        header = current_header

                        logging.info("Header found: %s",header)

                    # Read data rows
                    for row in reader:
                        all_data.append(row)

        logging.info("CSV files merged successfully")

        logging.info("Total records read: %s",len(all_data))
        return header, all_data

    except Exception as e:
        print("CSV reading error:", e)
        logging.error("CSV reading error: %s",e)

        return None, []