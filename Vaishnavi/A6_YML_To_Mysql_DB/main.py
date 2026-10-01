
from utils.read_file import read_file
from database_connection import db_connection
from YML_To_Mysql_DB.utils.config_data import fetch_config_data

def main():
    file = 'student.yml'
    config_file = 'config.json'
    fdata = read_file(file)
    print(fdata)
    config = fetch_config_data(config_file)

    for fdata in fdata:
        query = "insert into newstudent values({},'{}',{},'{}','{}',{},'{}','{}')".format(fdata['student_id'],fdata['name'],fdata['age'],fdata['city'],fdata['course'],fdata['marks'],fdata['skills'],fdata['address'])
        db_connection(config,'test',query)

if __name__ == '__main__':
    main()