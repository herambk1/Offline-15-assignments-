import threading
import logging
from utils.dbDetails import db_connection
from utils.readFile import readfile
from utils.getDept import getdept

logging.basicConfig(filename='log.txt', level=logging.INFO,
                    format='%(asctime)s - %(threadName)s - %(message)s')


def push(dept, dept_rows):
    try:
        conn = db_connection()
        cursor = conn.cursor()

        col_count = len(dept_rows[0])
        placeholders = ",".join("?" * col_count)
        col_names = ",".join(f"Col{i} VARCHAR(100)" for i in range(col_count))

        cursor.execute(f"IF OBJECT_ID('{dept}') IS NULL CREATE TABLE [{dept}] ({col_names})")

        for row in dept_rows:
            cursor.execute(f"insert into[{dept}] values ({placeholders})", row)

        conn.commit()
        conn.close()
        logging.info(f"{dept}: {len(dept_rows)} rows inserted")
    except Exception as e:
        logging.error(f"{dept}: failed - {e}")


path = input("Enter the path of the csv file: ").strip('"')
file = readfile(path)
departments = getdept(file)

threads = []
for dept in departments:
    dept_rows = [row for row in file if row[4] == dept]
    t = threading.Thread(target=push, args=(dept, dept_rows), name=dept)
    t.start()
    threads.append(t)

for t in threads:
    t.join()


if __name__ == "__push__":
    push()
