import pymysql
import json
import logging


def create_connection():

    connection = None

    try:

        logging.info("Reading config.json")

        # Read config.json
        with open("utils/config.json", "r") as file:
            config = json.load(file)
        db_config = config["mysql"]
        logging.info("Connecting to MySQL database")

        # Connect to existing database
        connection = pymysql.connect(host=db_config["host"],
            user=db_config["user"],
            password=db_config["password"],
            database=db_config["database"])

        print("MySQL connected successfully")
        logging.info("MySQL connected successfully")

        # Create cursor
        cursor = connection.cursor()

        logging.info("Creating employee table if not exists")

        # Create table automatically
        create_table_query = """ CREATE TABLE IF NOT EXISTS employee ( Customer_ID INT PRIMARY KEY, 
        Name VARCHAR(100), Age INT, City VARCHAR(100), Department VARCHAR(100), Salary INT ) """
        cursor.execute(create_table_query)
        connection.commit()
        cursor.close()

        print("Table checked successfully")

        logging.info("Employee table checked successfully")

        return connection

    except Exception as e:

        print("MySQL error:", e)
        logging.error("MySQL error: %s", e)

        if connection is not None:
            connection.close()
            logging.info("MySQL connection closed")
        return None