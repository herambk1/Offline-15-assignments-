import os
from Utility.logger_app import get_logger_name
logger = get_logger_name(__name__)

def create_destination_folders(destination_path):
    #Create folders for different file types.

    try:
        file_types = ['csv', 'pdf', 'json', 'yaml']
        for file_type in file_types:
            folder_path = os.path.join(destination_path,file_type)
            os.makedirs(folder_path,exist_ok=True)

            logger.info("Created folder: {}".format(folder_path))

    except Exception as e:
        logger.exception("Error while creating destination folders: {}".format(e))


def get_file_type(file_name):
    #Get file extension from file name.

    try:
        extension = os.path.splitext(file_name)[1]
        extension = extension.lower()
        if extension == '.csv':
            return 'csv'
        elif extension == '.pdf':
            return 'pdf'
        elif extension == '.json':
            return 'json'
        elif extension == '.yaml' or extension == '.yml':
            return 'yaml'
        else:
            return None
    except Exception as e:
        logger.exception("Error while getting file type: {}".format(e))
        return None
def move_file(source_file, destination_file):
    #Move a file
    try:
        with open(source_file, 'rb') as source:
            file_data = source.read()
        with open(destination_file, 'wb') as destination:
            destination.write(file_data)
        os.remove(source_file)
        logger.info(
            "File moved from {} to {}".format(source_file,destination_file))

    except Exception as e:
        logger.exception("Error while moving file {}: {}".format(source_file,e))

def organize_files(source_path, destination_path):
    #Read files from source folder and put them
    #into their respective destination folders.

    try:
        if not os.path.exists(source_path):
            logger.error("Source folder does not exist: {}".format(source_path))

            return
        create_destination_folders(destination_path)
        files = os.listdir(source_path)
        for file_name in files:
            source_file = os.path.join(source_path,file_name)
            if not os.path.isfile(source_file):
                continue

            file_type = get_file_type(file_name)

            if file_type is None:
                logger.info(
                    "File skipped because extension is not supported: {}".format(file_name))
                continue

            destination_folder = os.path.join(destination_path,file_type)

            destination_file = os.path.join(destination_folder,file_name)

            move_file(source_file,destination_file)

    except Exception as e:
        logger.exception("Error while organizing files: {}".format(e))