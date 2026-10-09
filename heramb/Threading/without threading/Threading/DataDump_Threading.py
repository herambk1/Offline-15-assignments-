from utils.read import readFile
from utils.getDept import get_departments  # ,dept_wise_data
from utils.db_details import db_connection

import threading


def Dump_data(tablename, data):
    # conn = db_connection()
    # cursor = conn.cursor()
    for record in data:
        query = f"""insert into {tablename} (employee_id, first_name, last_name, email, department ,designation, salary, city ,joining_year) values({record[0]}, '{record[1]}', '{record[2]}', '{record[3]}', '{record[4]}', '{record[5]}', {record[6]}, '{record[7]}','{record[8]}');"""
        # cursor.execute(query)

        print(query)


    # conn.commit()
    # conn.close()


def extract_dept_data(file, deptname):
    dept_list = []
    for record in file:
        if record[4] == deptname:
            dept_list.append(record)
    Dump_data(deptname, dept_list)

    # print(dept_list)

    #
    # def create_table(distinct_departments):
    #     conn = db_connection()
    #     cursor = conn.cursor()
    #
    #         for department in distinct_departments:
    #             cursor.execute('''create table {} (employee_id int, first_name varchar(50),last_name varchar(50),
    #                        email varchar(50), department varchar(50), designation varchar(50),
    #                        salary int, city varchar(50), joining_year date)'''.format(department))
    #         conn.commit()
    #         cursor.close()
    #         conn.close()


def main():
    file = readFile()
    # print(temp)
    dept_name = get_departments(file)
    # create_table(dept_name)
    for dept in dept_name:
        extract_dept_data(file, dept)
    # dept_wise_data(file,dept_name)


if __name__ == "__main__":
    main()
