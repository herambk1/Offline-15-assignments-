import os
def fetch_files(source):
    file_list = [file for file in os.listdir(source)]
    return file_list
