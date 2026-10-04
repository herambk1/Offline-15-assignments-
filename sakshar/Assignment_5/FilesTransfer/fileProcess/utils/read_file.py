import os
import csv
import utils.write_file as wf

def process_file(files, s_dir, t_dir):
    # data = []
    for file in files:
        os.chdir(s_dir)
        with open(file) as fp:
            data = list(csv.reader(fp))
        rmv_path = os.path.join(s_dir, file)
        os.remove(rmv_path)
        wf.write_taget_csv(data, file, t_dir)
