import pymysql

from utility.merge_csv_helper import read_config
from utility.logger import logger

logger = logger(__name__)


def db_script(data):
    try:

        # Read database configuration
        config = read_config(r"/\utility\config.json")
        dbconfig = config["database"]
        conn = pymysql.connect(
            host=dbconfig["host"],
            user=dbconfig["username"],
            password=dbconfig["password"],
            database=dbconfig["database_name"],
            port=dbconfig["port"]
        )

        cursor = conn.cursor()

        logger.info("DB connection successful")

        # Insert data
        for row in data:
            cursor.execute(
                "INSERT INTO employee VALUES (%s, %s, %s, %s, %s, %s, %s)",
                row
            )

        # Commit changes
        conn.commit()

        cursor.close()
        conn.close()

        logger.info("Data inserted successfully")

    except Exception as e:
        logger.error("DB connection failed: {}".format(e))