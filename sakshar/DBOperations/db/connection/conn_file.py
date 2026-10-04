import pymysql as mysql

def db_connect(lst):
    con = mysql.connect(
        host = "localhost",
        port = 3306,
        user = "sakshar",
        password = "sakshar",
        database = "file_data"
    )
    cursor = con.cursor()
    for i in lst:
        print(i)
        cursor.execute(i)
    # data = cursor.fetchall()
    con.commit()
    con.close()
    # return data
