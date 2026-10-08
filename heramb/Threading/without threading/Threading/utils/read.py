import os
import csv

def readFile():
    with open(r'D:\Downloads\employee_records_part_1.csv', "r") as file:
        reader = csv.reader(file)
        return list(reader)


