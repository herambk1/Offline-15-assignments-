from OS_Module.city_merging import log_config
from csv_utils.fetch_csv_files import fetch_csv_file
from csv_utils.fetch_header import fetch_header
from csv_utils.read_csv import read_csv_file
from db_utils.database_connection import DB_connection
from db_utils.DB_config import  read_config_file as DB_config
from db_utils.db_query import DB_query
from merge_files import merge_csv_file
from log_utils.log_config_data import log_config

logger = log_config(str(__file__).split("\\")[-1])


def main():
    logger = log_config(str(__file__).split("\\")[-1])
    logger.info("program started...")
    source = r"C:\Users\vaish\OneDrive\Documents\Destination"
    logger.info("source is {}".format(source))

    logger.info("fetching csv files")
    files = fetch_csv_file(source)
    logger.info("files is {}".format(files))

    config = DB_config('config.json')

    for file in files:
        logger.info("reading file {}".format(file))
        data = read_csv_file(source,file)
        print(data)
        header = fetch_header(data[0])
        logger.debug("header is {}".format(header))
        print(header)
        logger.info("mergging started")
        write_data = merge_csv_file(source,header,data)
        logger.info("all files merged")

        logger.info("inserting into database")
        for row in data:
            logger.info("generating query")
            query = DB_query(row)
            logger.debug("query is {}".format(query))
            logger.info("inserting into database")
            DB_connection(config, 'test',query)
            logger.info("all files inserted")

if __name__ == "__main__":
    main()