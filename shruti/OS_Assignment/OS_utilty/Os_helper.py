import logging
import os
from OS_utilty.logger import logger

logger = logger(__name__)

def file_ext(file):
    try:

        if file.endswith('.csv'):
            return 'csv'
        elif file.endswith('.txt'):
            return 'txt'
        elif file.endswith('.json'):
            return 'json'
        else:
            return None

    except Exception as e:
        logger.error("File extension creation failed".format(e))



def destination_folder(destination_path):
    try:
        file_exts = ['csv', 'txt', 'json']
        for file_type in file_exts:
            exts_dest = os.path.join(destination_path, file_type)
            os.makedirs(exts_dest)
        logger.info("created folders at: {},{} ".format(destination_path,exts_dest))

    except Exception as e:
        logger.error("Destination folder creation failed".format(e))

def read_then_write(source_file, dest_file):
    try:
        with open(source_file, 'r') as source:
            data = source.read()
        with open(dest_file, 'w') as destination:
            destination.write(data)
        os.remove(source_file)

        logger.info("extracted file from source and loaded in destination ")

    except Exception as e:
        logger.error("Source file creation failed".format(e))
