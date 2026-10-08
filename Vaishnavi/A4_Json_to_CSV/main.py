from read_json_file import read_file
from write_into_csv import write_file
from fetch_keys import fetch_keys
def main():
    data = read_file()
    keys = fetch_keys(data)
    write_file(data,keys)

if __name__=='__main__':
    main()