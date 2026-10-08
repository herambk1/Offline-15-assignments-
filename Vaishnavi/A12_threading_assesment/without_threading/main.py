import csv
import json
import pymysql
import time

def read_file(filename):
    try:
        with open("{}".format(filename))as fp:
            reader = csv.DictReader(fp)
            data = list(reader)

        return data
    except Exception as e:
        print(e)

def fetch_dept(data):
    dept = []
    for row in data:
        if row['Dept'] not in dept:
            dept.append(row['Dept'])

    return dept

def read_dbConfig(filename):
    try:
        with open("{}".format(filename)) as fp:
            data = json.load(fp)

        return data
    except Exception as e:
        print(e)

def DB_connection(con,db_name,data,unique_dept):

    try:
        con =pymysql.connect(host=con['host'],user = con['username'],password = con['password'],database=db_name)
        cur = con.cursor()
        for dept in unique_dept:
            table_name = dept.lower().replace(" ","_")
            cur.execute(f"""
            CREATE TABLE IF NOT EXISTS {table_name} (EmpID INT ,
            Name varchar(30),Age int,Gender Varchar(30),
            Dept Varchar(30),Salary int,City varchar(30))

""")

            for row in data:
                if dept == row['Dept']:
                    query = "insert into {} values({},'{}',{},'{}','{}',{},'{}')".format(table_name,
                                                                                                row['EmpID'],
                                                                                                row['Name'], row['Age'],
                                                                                                row['Gender'],
                                                                                                row['Dept'],
                                                                                                row['Salary'],
                                                                                                row['City'])

                    cur.execute(query)
        con.commit()
        con.close()
    except Exception as e:
        print(e)

def main():
    start = time.time()
    filename = "empdata.csv"
    config = 'config.json'
    data = read_file(filename)
    unique_dept = fetch_dept(data)
    print(unique_dept)

    con_data = read_dbConfig(config)
    print(con_data)
    DB_connection(con_data,'test',data,unique_dept)
    end = time.time()
    print("total Time: ",end-start)


if __name__=="__main__":
    main()