import pymysql
import json
import logging


def create_connection():

    connection = None

    try:

        with open("utils/config.json", "r") as file:
            config = json.load(file)

        mysql_config = config["mysql"]

        connection = pymysql.connect(
            host=mysql_config["host"],
            user=mysql_config["user"],
            password=mysql_config["password"],
            database=mysql_config["database"]
        )

        logging.info("MySQL connected successfully")
        print("MySQL connected successfully")

        return connection

    except Exception as e:

        logging.error(
            "MySQL connection error: %s",
            e
        )

        print(
            "MySQL connection error:",e)

        return None