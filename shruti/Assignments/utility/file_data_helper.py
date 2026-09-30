import csv

from utility import config


def input_file(filename):
    with open(filename) as fp:
         data = fp.read()
    return data

def input_csv_file(filename):
    with open('{}'.format(filename)) as fp:
        r = csv.reader(fp)
        data = list(r)
    return data

def write_csv_file(unique_depts,data,header):
    for dept in unique_depts:
        dept_data = []

        for record in data:
            if dept == data[-1]:
                dept_data.append(record)

        with open('{}_data.csv'.format(dept),config.write_mode,newline = '') as fp:
            w = csv.writer(fp)
            w.writerow(header)
            w.writerows(dept_data)


def get_unique_dept(data):
    uniqueDept = []
    for record in data:
        uniqueDept.append(record[-1])
    return uniqueDept


def count_email_ids(filedata):
    valid_emails = 0
    invalid_emails = 0
    if filedata.lower() and filedata.endswith(".com"):
        valid_emails +=1
    else:
        invalid_emails +=1

    return valid_emails

def filter_email_ids(data):
    valid_emails = []
    invalid_emails= []
    for word in data.split():
        if word.lower() and word.endswith(".com"):
            valid_emails.append(word)
        else:
            invalid_emails.append(word)

    return valid_emails,invalid_emails


def count_mobile_num(filedata):
    valid_mobilenos = 0
    invalid_mobilenos= 0
    if filedata.isnumeric():
        if len(filedata)==10:
            if filedata.startswith('8') or filedata.startswith('9'):
                valid_mobilenos +=1
            else:
                invalid_mobilenos +=1
    return valid_mobilenos


def filter_mobile_num(data):
    valid_mobilenos = []
    invalid_mobilenos= []
    for word in data.split():
        if word.isnumeric():
            if len(word)==10:
                if word.startswith('8') or word.startswith('9'):
                    valid_mobilenos.append(word)
                else:
                    invalid_mobilenos.append(word)
    return valid_mobilenos,invalid_mobilenos

def count_special_char(data):
    count = 0
    for word in data:
        if not word.isnumeric() and not word.isalpha():
            count += 1

    return count

