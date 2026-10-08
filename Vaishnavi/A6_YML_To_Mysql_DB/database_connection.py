import pymysql
def db_connection(con,dbname,query):
    conn = pymysql.connect(host=con['host'],port=con['port'],user =con['user'],password = con['password'],database = dbname)
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    conn.close()
