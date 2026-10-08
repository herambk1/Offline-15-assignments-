import csv
def write_file(data,keys):
    with open('empdata.csv','w',newline='') as fp:
        writer = csv.DictWriter(fp,fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)