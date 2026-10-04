import csv

def read_file(file):
    with open(file,"r") as fp:
        data = list(csv.DictReader(fp))
    return data

def extract_department(data):
    list_of_dept = []
    for i in data:
        if i["Department"] not in list_of_dept:
            list_of_dept.append(i["Department"])
    return list_of_dept

def prepare_filename_with_data(dept_list, data):
    for deptName in dept_list:
        pd = process_file(deptName,data)
        write_file(deptName, pd)

def process_file(dept, data):
    sorted_list = []
    for item in data:
        if item["Department"] == dept:
            sorted_list.append(item)
    return sorted_list

def write_file(dept_name, dept_data):
    filename = r"C:\Users\saksh\PycharmProjects\PythonProject\File_Handeling\DepartmentWiseCsvData\{}_Records.csv".format(dept_name)
    # print(filename)
    with open(filename,"w", newline='') as fp:
        header = dept_data[0].keys()
        w = csv.DictWriter(fp, fieldnames=header)
        w.writeheader()
        w.writerows(dept_data)


def main():
    filename = r"/CsvFileOperations/employee.csv"
    res = read_file(filename)
    l = extract_department(res)
    prepare_filename_with_data(l, res)
    # department = "HR"
    # pd = process_file(department, res)
    # write_file(department, pd)

if __name__ == "__main__":
    main()