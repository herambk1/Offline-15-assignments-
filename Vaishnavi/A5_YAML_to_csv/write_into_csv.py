import csv
def write_file(data,fname):
    with open('student.csv','w',newline='') as fp:
        writer = csv.DictWriter(fp,fieldnames=fname)
        writer.writeheader()
        writer.writerows(data)