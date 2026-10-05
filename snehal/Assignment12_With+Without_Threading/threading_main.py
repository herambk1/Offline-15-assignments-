import logging
import threading
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


def process_department(department, records):

    connection = None
    cursor = None

    try:

        print(
            "Thread started:",
            department
        )

        # Each thread gets its own connection
        connection = create_connection()

        if connection is None:
            return

        cursor = connection.cursor()

        table_name = department.lower().replace(" ", "_")

        # Create table
        create_query = f"""
        CREATE TABLE IF NOT EXISTS `{table_name}` (
            Employee_ID INT,
            Name VARCHAR(100),
            Age INT,
            City VARCHAR(100),
            Department VARCHAR(100),
            Salary INT
        )
        """

        cursor.execute(create_query)

        # Insert data
        insert_query = f"""
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

            cursor.execute(
                insert_query,
                values
            )

        connection.commit()

        print(
            department,
            "completed"
        )

        logging.info(
            "%s completed successfully",
            department
        )

    except Exception as e:

        if connection:
            connection.rollback()

        logging.error(
            "%s processing error: %s",
            department,
            e
        )

        print(
            department,
            "error:",
            e
        )

    finally:

        if cursor:
            cursor.close()

        if connection:
            connection.close()


def main():

    get_logger()

    # Start time
    start = time.time()

    print("Starting Assignment 12 - With Threading")

    logging.info(
        "Assignment 12 started - With Threading"
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

    threads = []

    # Create threads
    for department, records in departments.items():

        thread = threading.Thread(
            target=process_department,
            args=(department, records)
        )

        threads.append(thread)

        thread.start()

    # Wait for all threads
    for thread in threads:

        thread.join()

    # End time
    end = time.time()

    print()
    print("All threads completed")

    print(
        "Time required:",
        end - start,
        "seconds"
    )

    print("Assignment 12 completed")

    logging.info("All threads completed")

    logging.info(
        "Time required: %s seconds",
        end - start
    )

    logging.info(
        "Assignment 12 completed"
    )


if __name__ == "__main__":
    main()