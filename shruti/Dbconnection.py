import pymysql

conn = pymysql.connect(host='127.0.0.1',port=3306,user='shrutikhandare',password='root',
                       db='ainexus2026')
cur = conn.cursor()
cur.execute("insert into emp values (104,'deva','mum')")
conn.commit()
conn.close()
conn = pymysql.connect(host='127.0.0.1',port=3306,user='shrutikhandare',
                       password='root',db='ainexus2026')
cur = conn.cursor()
cur.execute("select * from emp")
data = cur.fetchall()
print(data)
conn.close()



