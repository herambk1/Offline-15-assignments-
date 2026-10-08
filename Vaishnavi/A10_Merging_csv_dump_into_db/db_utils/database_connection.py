import pymysql
from log_utils.log_config_data import log_config

logger = log_config(str(__file__).split("\\")[-1])


def DB_connection(config, db_name, query):
    logger.info("Connecting to database: {}".format(db_name))
    conn = pymysql.connect(host=config["host"], port=config["port"], user=config["user"], password=config["password"],
                           database=db_name)
    logger.info("Database connection successful")

    cur = conn.cursor()
    logger.info("Executing query")
    print(query)

    result = cur.execute(query)
    conn.commit()
    logger.info("Query executed and committed successfully")

    conn.close()
    logger.info("Database connection closed")