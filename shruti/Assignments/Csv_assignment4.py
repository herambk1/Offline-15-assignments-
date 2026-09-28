from utility.file_data_helper import  input_csv_file,write_csv_file,get_unique_dept
from utility import config


def main():
        file = config.csv_file
        data = input_csv_file(file)
        unique_depts = get_unique_dept(data)
        write_csv_file(unique_depts, data, data[0])


if __name__ == '__main__':
    main()