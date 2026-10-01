import json
import csv

def input_json_file(filename):
    with open(filename, newline= "") as fp:
        r = json.load(fp)
    return r

def write_jsontocsv_file(data):
    with open("output.csv", "w", newline="") as csv_file:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
