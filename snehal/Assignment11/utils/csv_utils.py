import csv
from utils.logger import get_logger
logger = get_logger()

def read_csv_file(file_path):
    data = []

    try:
        logger.info("Reading CSV file: %s",file_path)
        with open(file_path,"r",newline="") as file:
            reader = csv.DictReader(file)
            print("Header:",reader.fieldnames)

            logger.info("Header: %s",reader.fieldnames)

            for row in reader:
                selected_data = (row["Customer_ID"],row["Name"],row["City"],row["Salary"])
                data.append(selected_data)

        logger.info("CSV file read successfully")

        logger.info("Total records: %s",len(data))

        print("Total records:",len(data))

        return data
    except Exception as e:
        logger.exception("CSV reading error")

        print("CSV Error:",e)
        return []