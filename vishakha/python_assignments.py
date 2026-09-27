

import  csv
import yaml


def read_to_yml(filename):
    with open("{}.yaml".format(filename), "r") as fp:
        return yaml.safe_load(fp)

def get_columns(file):
    columns = {}

    for record in file:
        for key in record:
            columns[key]=1
    return list(columns.keys())

def yml_to_csv(keys,file):
    filename="{}.csv".format("bank_output")

    with open(filename,"w",newline="") as fp:
        writer=csv.DictWriter(fp, fieldnames=keys)
        writer.writeheader()
        writer.writerows(file)



def main():
    file=read_to_yml(r"C:\Users\VISHAKHA MANE\PycharmProjects\databaseconn\bank")
    keys=get_columns(file)
    yml_to_csv(keys,file)
    print(keys)


if __name__ == "__main__":
    main()
