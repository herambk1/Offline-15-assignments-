import csv
def read_data_from_source_csv(fname):
    with open('{}'.format(fname)) as fp:
        r = csv.reader(fp)
        data = list(r)
    return data

def filter_data(filedata):
    finance_list = []
    for row in filedata:
        if row[-1] == 'Finance':
            finance_list.append(row)
    return finance_list

def write_data_into_csv(finrecords,header):
    with open("finance_records.csv","w",newline='') as fp:
        w = csv.writer(fp)
        w.writerow(header)
        w.writerows(finrecords)


def main():
    filename ='empsal_part_buck.csv'
    fdata = read_data_from_source_csv(filename)
    finance_records = filter_data(fdata)
    write_data_into_csv(finance_records,fdata[0])

if __name__ == '__main__':
    main()
