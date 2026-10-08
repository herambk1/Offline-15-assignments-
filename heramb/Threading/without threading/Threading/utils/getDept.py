import csv

def get_departments(deptname):
    deptname.pop(0)
    departments = set()
    for row in deptname:
        departments.add(row[4])
    return departments

# def dept_wise_data(file,deptname):
#     empdetails={}
#     for dept in deptname:
#         empdetails[dept]=[]
#
#     for record in file:
#         for dept in deptname:
#             if record[4]== dept:
#                 empdetails[dept].append(record)
#     # print(empdetails.keys())

    print(empdetails)






