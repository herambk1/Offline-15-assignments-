import os

from file_organizer import organize_files
from Utility.logger_app import get_logger_name

logger = get_logger_name(__name__)

def main():

    try:
        current_directory = os.getcwd()
        source_path = os.path.join(current_directory, 'source')

        destination_path = os.path.join(current_directory,'destination')

        logger.info("Source folder: {}".format(source_path))

        logger.info("Destination folder: {}".format(destination_path))

        organize_files(source_path,destination_path)

        print("Files have been organized successfully.")

    except Exception as e:

        logger.exception("Error in main program: {}".format(e))

        print("Something went wrong. Please check server.log.")

if __name__ == '__main__':
    main()