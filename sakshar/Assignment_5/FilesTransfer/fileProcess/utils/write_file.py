import csv
import os

def write_taget_csv(data,file_name,t_dir):
    os.chdir(t_dir)
    with open(file_name, "w", newline="") as fp:
        w = csv.writer(fp)
        w.writerows(data)