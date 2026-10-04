import logging

from utils.csv_utils import read_csv_files
from utils.mysql_connection import create_connection


SOURCE_FOLDER = "source"

def insert_data(data):

    connection = create_connection()
    if connection is None:
        logging.error("Database connection failed")
        return
    cursor = None

    try:
        cursor = connection.cursor()

        query ="""INSERT IGNORE INTO employee
        (Customer_ID, Name, Age, City, Department, Salary)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        for row in data:
            cursor.execute(query, row)
        connection.commit()
        print("Data inserted successfully")

        logging.info("CSV data inserted into MySQL successfully")

    except Exception as e:
        connection.rollback()
        print("Data insertion error:", e)
        logging.error("Data insertion error: %s",e)

    finally:
        if cursor is not None:
            cursor.close()
        connection.close()
        logging.info("MySQL connection closed")


def main():

    try:
        print("Starting Assignment No. 10")
        logging.info("Assignment started")

        # Read and merge CSV files
        header, data = read_csv_files(SOURCE_FOLDER)

        if header is None:
            print("CSV reading failed")
            logging.error("CSV reading failed")
            return

        print("Header:", header)
        print("Total records:", len(data))

        logging.info(
            "Total records read: %s",
            len(data))

        # Insert merged data into MySQL
        insert_data(data)
        logging.info("Assignment completed")

    except Exception as e:
        print("Unexpected error:", e)
        logging.exception("Unexpected error occurred")

if __name__ == "__main__":
    main()