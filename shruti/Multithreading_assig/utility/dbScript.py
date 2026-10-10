
import pymysql

from utility.merge_csv_helper import read_config
from utility.logger import logger
logger = logger(__name__)

def db_script(dept,rows):

    try:
        config = read_config(r"D:\AINexusIT\Git\Offline-15-assignments-\shruti\without_threading_assig\utility\config.json")
        dbconfig = config["database"]

        conn = pymysql.connect(
            host=dbconfig["host"],
            user=dbconfig["user"],
            password=dbconfig["password"],
            database=dbconfig["database"],
            port=dbconfig["port"]
        )

        cursor = conn.cursor()
        logger.info("DB connection successful")

        dept_table = {
            "IT": "ITdept",
            "HR": "HRdept",
            "Finance": "Financedept",
            "Sales": "Salesdept",
            "Marketing": "Marketingdept"
        }

        table_name = dept_table[dept]

        query = f"""
            INSERT INTO {table_name}
            (empid, empname, city, sal, age, dob, dept)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        rowsUpdated = cursor.executemany(query, rows)

        logger.info(
            "{} records inserted into {}".format(
                rowsUpdated,
                table_name
            )
        )

        conn.commit()
        cursor.close()
        conn.close()
        logger.info("All department data inserted successfully")

    except Exception as e:

        logger.error(
            "DB connection failed: {}".format(e)
        )
