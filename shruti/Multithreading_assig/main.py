import threading
import time

from utility.logger import logger
from utility.helper import input_csv_file,get_unique_depts,split_data_by_dept
from utility.dbScript import db_script

logger = logger(__name__)

def main():
    try:
        csvfile = input_csv_file(r"D:\AINexusIT\Git\Offline-15-assignments-\shruti\Multithreading_assig\utility\employee_1_million_records_updated.csv")
        get_unique_depts(csvfile)
        dept_data = split_data_by_dept(csvfile)

        start_time = time.time()
        threads = []
        for dept,rows in dept_data.items():
            thread = threading.Thread(target= db_script,args=(dept,rows))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

        end_time = time.time()
        total_time = end_time - start_time

        print("total time {}:".format(total_time))

    except Exception as e:
        logger.error("seperation of deptwise data faild : {} ".format(e))



if __name__ == "__main__":
    main()
