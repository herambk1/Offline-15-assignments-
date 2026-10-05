from utils.sftp import download_file
from utils.database import insert_data
from utils.logger import get_logger


def main():

    logger = get_logger()

    try:

        logger.info("Program started")

        # Download file from SFTP
        download_file()

        logger.info("File downloaded")

        # Insert data into database
        insert_data()

        logger.info("Data inserted")

        print("Process completed successfully")

    except Exception as e:

        logger.error("Error: {}".format(e))

        print("Process failed")


if __name__ == "__main__":
    main()