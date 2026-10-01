import logging

from utils.csv_utils import read_csv_files
from utils.mysql_connection import create_connection


SOURCE_FOLDER = "source"

logging.basicConfig(level=10,force = True, filename='app.log',
                   format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                   datefmt='%d-%m-%Y %H:%M:%S %p')
