import csv
import pymysql


def insert_data():

    connection = None

    try:

        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="root",
            database="assignment2"
        )

        cursor = connection.cursor()

        with open(
            "source/emp.csv",
            "r",
            encoding="utf-8-sig"
        ) as file:

            reader = csv.DictReader(file)

            print("CSV columns:", reader.fieldnames)

            for row in reader:

                print("Row:", row)

                query = """
                INSERT INTO employees
                (empid, empname,salary,city)
                VALUES (%s, %s, %s,%s)
                """

                values = (
                    row["empid"],
                    row["empname"],
                    row["salary"],
                    row["city"]
                )

                cursor.execute(query, values)

        connection.commit()

        print("Data inserted successfully")

    except Exception as e:

        print("Database Error:", e)

        if connection:
            connection.rollback()

    finally:

        if connection:
            connection.close()