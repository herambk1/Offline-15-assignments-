from log_utils.log_config_data import log_config
logger = log_config(str(__file__).split("\\")[-1])
import os

logger.info("csv file fetching started...")
def fetch_csv_file(source):
    csv_files = [file for file in os.listdir(source) if file.endswith(".csv")]
    return csv_files
logger.info("csv file fetching finished...")