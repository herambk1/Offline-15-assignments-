import threading
import pymysql
from log_utils.log_config import custom_log
logger = custom_log(str(__file__).split("\\")[-1])
def DB_connection(con,db_name,data,dept):

    try:
        logger.info(
            "{} started for department: {}".format(
                threading.current_thread().name, dept
            )
        )

        con =pymysql.connect(
            host=con['host'],
            user=con['username'],
            password=con['password'],
            database=db_name
        )

        logger.info(
            "{} database connection successful".format(
                threading.current_thread().name
            )
        )

        cur = con.cursor()

        print(threading.current_thread().name,
              "creating table")

        table_name = dept.lower().replace(" ","_")

        logger.info(
            "{} creating table: {}".format(
                threading.current_thread().name,
                table_name
            )
        )

        cur.execute(f"""CREATE TABLE IF NOT EXISTS {table_name} (EmpID INT ,
            Name varchar(30),Age int,Gender Varchar(30),
            Dept Varchar(30),Salary int,City varchar(30))

""")

        logger.info(
            "{} table created/exists: {}".format(
                threading.current_thread().name,
                table_name
            )
        )

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

        logger.info(
            "{} data inserted successfully into {}".format(
                threading.current_thread().name,
                table_name
            )
        )

        print(threading.current_thread().name,
              "completed:", table_name)

        con.close()

        logger.info(
            "{} connection closed for {}".format(
                threading.current_thread().name,
                table_name
            )
        )

    except Exception as e:
        logger.error(
            "{} Error: {}".format(
                threading.current_thread().name,
                e
            )
        )

        print(threading.current_thread().name,
              "Error:", e)