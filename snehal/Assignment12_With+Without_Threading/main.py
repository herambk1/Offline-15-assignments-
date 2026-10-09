import logging
import time

from utils.csv_utils import read_csv_file
from utils.mysql_connection import create_connection
from utils.logger import get_logger


SOURCE_FILE = "source/employee.csv"


def separate_department(data):

    departments = {}

    try:

        for row in data:

            department = row["Department"]

            if department not in departments:
                departments[department] = []

            departments[department].append(row)

        logging.info("Data separated department wise")
        print("Data separated department wise")

    except Exception as e:

        logging.error(
            "Department separation error: %s",
            e
        )

        print(
            "Department separation error:",
            e
        )

    return departments


def create_table(connection, department):

    cursor = None

    try:

        cursor = connection.cursor()

        table_name = department.lower().replace(" ", "_")

        query = f"""
        CREATE TABLE IF NOT EXISTS `{table_name}` (
            Employee_ID INT,
            Name VARCHAR(100),
            Age INT,
            City VARCHAR(100),
            Department VARCHAR(100),
            Salary INT
        )
        """

        cursor.execute(query)

        connection.commit()

        logging.info(
            "Table created successfully: %s",
            table_name
        )

        print(
            "Table created:",
            table_name
        )

    except Exception as e:

        logging.error(
            "Table creation error: %s",
            e
        )

        print(
            "Table creation error:",
            e
        )

    finally:

        if cursor:
            cursor.close()


def insert_data(connection, department, records):

    cursor = None

    try:

        cursor = connection.cursor()

        table_name = department.lower().replace(" ", "_")

        query = f"""
        INSERT INTO `{table_name}`
        (
            Employee_ID,
            Name,
            Age,
            City,
            Department,
            Salary
        )
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        for row in records:

            values = (
                row["Employee_ID"],
                row["Name"],
                row["Age"],
                row["City"],
                row["Department"],
                row["Salary"]
            )

            cursor.execute(query, values)

        connection.commit()

        logging.info(
            "Data inserted successfully into %s",
            table_name
        )

        print(
            "Data inserted successfully into",
            table_name
        )

    except Exception as e:

        connection.rollback()

        logging.error(
            "Data insertion error: %s",
            e
        )

        print(
            "Data insertion error:",
            e
        )

    finally:

        if cursor:
            cursor.close()


def main():

    get_logger()

    # Start time
    start = time.time()

    print("Starting Assignment 12 - Without Threading")

    logging.info(
        "Assignment 12 started - Without Threading"
    )

    # Read CSV
    data = read_csv_file(SOURCE_FILE)

    if not data:

        print("No data found")
        return

    print(
        "Total records:",
        len(data)
    )

    # Separate department wise
    departments = separate_department(data)

    # Connect to existing database
    connection = create_connection()

    if connection is None:
        return

    # Process departments one by one
    for department, records in departments.items():

        print()
        print(
            "Processing Department:",
            department
        )

        create_table(
            connection,
            department
        )

        insert_data(
            connection,
            department,
            records
        )

    connection.close()

    print()
    print("Database connection closed")

    # End time
    end = time.time()

    print(
        "Time required:",
        end - start,
        "seconds"
    )

    print("Assignment 12 completed")

    logging.info(
        "Time required: %s seconds",
        end - start
    )

    logging.info(
        "Assignment 12 completed"
    )


if __name__ == "__main__":
    main()