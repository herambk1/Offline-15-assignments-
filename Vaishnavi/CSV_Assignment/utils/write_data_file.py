import csv
def write_file(unique_depts,fdata,header):
    for dept in unique_depts:
        dept_data = []

        for data in fdata[1:]:
            if dept == data[-1]:
                dept_data.append(data)

        with open('{}_data.csv'.format(dept),'w',newline = '') as fp:
            w = csv.writer(fp)
            w.writerow(header)
            w.writerows(dept_data)
