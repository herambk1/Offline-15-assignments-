from read_file import read_file
from fetch_dept import fetch_dept
from db_utils.read_dbConfig import read_dbConfig
from DB_Connection_Thread import  DB_Connection_Thread
import time

from log_utils.log_config import custom_log
logger = custom_log(str(__file__).split("\\")[-1])

def main():

    logger = custom_log("main")

    start = time.time()

    logger.info("Program started")

    filename = "empdata.csv"
    config = 'config.json'

    data = read_file(filename)

    unique_dept = fetch_dept(data)

    print(unique_dept)

    con_data = read_dbConfig(config)

    print(con_data)

    DB_Connection_Thread(
        con_data,
        'test',
        data,
        unique_dept
    )

    end = time.time()

    print("total Time: ",end-start)

    logger.info(
        "Program completed. Total Time: {}".format(end-start)
    )


if __name__=="__main__":
    main()

