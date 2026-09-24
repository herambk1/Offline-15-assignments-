import os
def delete_from_source(source,csv_files):
    os.remove("{}/{}".format(source,csv_files))