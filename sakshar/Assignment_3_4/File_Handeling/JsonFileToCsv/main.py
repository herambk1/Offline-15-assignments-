import json
import csv

def read_json_file(file_name):
    with open(file_name) as fp:
        data = json.load(fp)
        return data

def write_csv_file(data):
    file_name = r"C:\Users\saksh\PycharmProjects\PythonProject\File_Handeling\JsonFileToCsv\DataFiles\employee.csv"
    with open(file_name, "w", newline="") as fp:
        headers = data[0].keys()
        w = csv.DictWriter(fp, fieldnames=headers)
        w.writeheader()
        w.writerows(data)

def main():
    file = r"C:\Users\saksh\PycharmProjects\PythonProject\File_Handeling\JsonFileToCsv\DataFiles\employee.json"
    res = read_json_file(file)
    write_csv_file(res)


if __name__ == "__main__":
    main()