from csv_utilty.csv_helper import  input_csv_file,write_csv_files,get_unique_depts

def main():
    file = "empsal_part_buck.csv"
    data = input_csv_file(file)
    unique_depts = get_unique_depts(data)
    write_csv_files(unique_depts,data,data[0])

if __name__=='__main__':
    main()