from utils.read_data import read_file
from utils.write_File import write_file
from file_extension import file_ext
from fetch_files import fetch_files
from log_utils.log_config import log_confing
import os
logger = log_confing(str(__file__).split("\\")[-1])

def main():
    logger.info("Program started")

    current_directory = os.getcwd()
    source = os.path.join(current_directory, 'source')
    destination = os.path.join(current_directory, 'destination')

    files = fetch_files(source)
    for file in files:
        data = read_file(source,file)
        extension = file_ext(source,file)
        write_file(destination,data,file,extension)

    logger.info("Program completed")

if __name__ == '__main__':
    main()
