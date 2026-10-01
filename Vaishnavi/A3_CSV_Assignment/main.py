from utils.read_file import read_csv_file
from utils.write_data_file import write_file
from unique_dept_data import unique_dept


def main():
    file = 'empsal_part_buck.csv'
    fdata = read_csv_file(file)
    unique_depts = unique_dept(fdata)
    write_file(unique_depts,fdata,fdata[0])

if __name__=='__main__':
    main()