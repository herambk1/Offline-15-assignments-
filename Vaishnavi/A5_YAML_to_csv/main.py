from read_YML_file import read_file
from write_into_csv import write_file
from fetch_fieldname import fieldname

def main():

    data = read_file()
    data = data['students']
    fname = fieldname(data)
    write_file(data,fname)

if __name__=='__main__':
    main()