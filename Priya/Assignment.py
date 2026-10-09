import csv
import logging
import os

logging.basicConfig(level=10,filename='server.log',
                    format='%(asctime)s - %(name)s- %(levelname)s - %(message)s',
                    datefmt='%d-%m-%Y %H-%M-%S-%p')

logger = logging.getLogger("assignment.py")

def read_file(filepath):
    filename = os.path.basename(filepath)
    logging.info("Reading file: %s", filename)
    with open(filepath, newline="") as fp:
        reader = csv.reader(fp)
        data = list(reader)
    logging.info("File reading completed: %s", filename)
    return data

def main():
    filepath = r"C:\Users\Admin\PycharmProjects\OSMODULEPR\empsal_part_buck.csv"
    data = read_file(filepath)
    print(data)

if __name__ == "__main__":
    main()