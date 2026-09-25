import os

def extract_csv_file_names(s_dir):
    os.chdir(s_dir)
    file_list = os.listdir(os.getcwd())
    csv_files = []
    for name in file_list:
       if name.endswith(".csv"):
           csv_files.append(name)
    return csv_files