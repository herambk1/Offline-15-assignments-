import json
import pymysql

from utils.logger import get_logger
logger = get_logger()
def read_config():

    try:
        with open("utils/config.json","r") as file:
            config = json.load(file)

        return config
    except Exception as e:

        logger.exception("Config file reading error")

        print("Config Error:",e)

        return None

def create_connection():
    try:
        config = read_config()

        if config is None:
            return None
        mysql_config = config["mysql"]

        connection = pymysql.connect(host=mysql_config["host"],
            user=mysql_config["user"],
            password=mysql_config["password"],
            database=mysql_config["database"])

        logger.info("MySQL connected successfully")

        print("MySQL connected successfully")

        return connection

    except Exception as e:

        logger.exception("MySQL connection error")

        print("MySQL Error:",e)

        return None
def insert_data(data):

    connection = None
    cursor = None

    try:
        config = read_config()
        if config is None:
            return

        table_name = config["mysql"]["table"]
        connection = create_connection()
        if connection is None:
            return

        cursor = connection.cursor()

        query = f"""
        INSERT INTO {table_name}
        (Customer_ID, Name, City, Salary)
        VALUES (%s, %s, %s, %s)"""

        for row in data:
            cursor.execute(query,row)

        connection.commit()
        logger.info("Data inserted successfully")

        logger.info("Total records inserted: %s",len(data))

        print("Data inserted successfully")

        print("Total records inserted:",len(data))

    except Exception as e:

        if connection:
            connection.rollback()

        logger.exception("Data insertion error")

        print("Data insertion Error:",e)

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()

        logger.info("MySQL connection closed")