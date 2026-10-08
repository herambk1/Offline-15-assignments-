import threading
from log_utils.log_config import custom_log
from db_utils.DB_connection import DB_connection

logger = custom_log(str(__file__).split("\\")[-1])

def DB_Connection_Thread(con,db_name,data,unique_dept):

    threads = []

    logger.info("Starting department threads")

    for dept in unique_dept:
        thread = threading.Thread(
            target=DB_connection,
            args=(con,db_name,data,dept)
        )

        threads.append(thread)
        thread.start()

        logger.info(
            "{} started for department: {}".format(
                thread.name,
                dept
            )
        )

    for thread in threads:
        thread.join()

        print("All department Threads completed")

        logger.info(
            "{} completed".format(thread.name)
        )
