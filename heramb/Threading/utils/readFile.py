import csv
import os

def readfile(path):
    rows=[]
    with open(path, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            rows.append(row)
        return rows





