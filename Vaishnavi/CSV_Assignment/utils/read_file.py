import csv

def read_csv_file(filename):
    with open('{}'.format(filename)) as fp:
        r = csv.reader(fp)
        data = list(r)
    return data
