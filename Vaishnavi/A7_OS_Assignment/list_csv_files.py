import os
def list_csv_files(source):
    # dir = os.listdir(source)
    # csv_files=[]
    # for file in dir:
    #     if file.endswith(".csv"):
    #         csv_files.append(file)

    csv_files = [file for file in os.listdir(source) if file.endswith(".csv")]
    return csv_files
