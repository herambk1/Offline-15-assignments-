import csv

def input_csv_file(filename):
    with open('{}'.format(filename)) as fp:
        r = csv.reader(fp)
        data = list(r)
    return data

def get_unique_depts(fdata):
    uniqueDept = set()
    for data in fdata[1:]:
        uniqueDept.add(data[-1])
    return uniqueDept

def write_csv_files(unique_depts,fdata,header):
    for dept in unique_depts:
        dept_data = []

        for data in fdata:
            if dept == data[-1]:
                dept_data.append(data)

        with open('{}.csv'.format(dept),'w',newline = '') as fp:
            w = csv.writer(fp)
            w.writerow(header)
            w.writerows(dept_data)