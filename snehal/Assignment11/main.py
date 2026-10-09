from utils.sftp_utils import download_file
from utils.csv_utils import read_csv_file
from utils.mysql_connection import insert_data
from utils.logger import get_logger

logger = get_logger()

def main():

    try:
        print("===================================")
        print("Starting Assignment No. 11")
        print("===================================")

        logger.info(
            "Assignment No. 11 started"
        )

        # Step 1: Download exact file from SFTP

        file_path = download_file()

        if file_path is None:

            logger.error("File download failed")

            print("File download failed")

            return

        # Step 2: Read CSV
        # Select required columns

        data = read_csv_file(file_path)

        if not data:

            logger.error("No data found in CSV")

            print("No data found in CSV")

            return

        # Step 3: Insert data into MySQL

        insert_data(data)

        logger.info("Assignment No. 11 completed successfully")

        print("===================================")
        print("Assignment No. 11 completed")
        print("===================================")

    except Exception as e:

        logger.exception("Unexpected error occurred")

        print("Main Error:",e)

if __name__ == "__main__":
    main()