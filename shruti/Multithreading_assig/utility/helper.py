import json
import csv
from utility.logger import logger

logger = logger(__name__)

def read_config(filename):
    try:
        with open(filename) as f:
            config = json.load(f)
        return config
    except Exception as e:
        logger("{} file not found ".format(filename,e))


def input_csv_file(filename):
    try:

     with open('{}'.format(filename)) as fp:
        r = csv.reader(fp)
        data = list(r)
     return data
    except Exception as e:
        logger.error("{} file not found ".format(filename,e))

def get_unique_depts(fdata):
    try:
        uniqueDept = set()
        for data in fdata[1:]:
            uniqueDept.add(data[-1])
        return sorted(uniqueDept)
    except Exception as e:
        logger.error("faild to find unique dept ".format(fdata,e))

def split_data_by_dept(fdata):
    try:
        dept_data = {
            "IT" : [],
            "HR" : [],
            "Finance" : [],
            "Sales": [],
            "Marketing": []
        }
        for row in fdata[1:]:
            dept = row[-1]
            if dept in dept_data:
                dept_data[dept].append(row)
        return dept_data

    except Exception as e:
        logger.error("data of seperation faild ".format(fdata,e))