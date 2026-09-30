import db.connection.conn_file as con
import db.txtToDb.read_txt as tf

def main():
    res = tf.read_txt_file(r"C:\Users\saksh\PycharmProjects\PythonProject\DBOperations\db\txtToDb\txtFiles\user.txt")
    lst = tf.create_insert_list(res)
    # print(lst)
    con.db_connect(lst)
    # print(res)

if __name__ == '__main__':
    main()
