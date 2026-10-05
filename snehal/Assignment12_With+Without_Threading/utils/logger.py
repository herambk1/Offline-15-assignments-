import logging

logging.basicConfig(
    level=logging.INFO,
    filename="logfile.log",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d-%m-%Y %H:%M:%S")

def get_logger():
    return logging.getLogger()