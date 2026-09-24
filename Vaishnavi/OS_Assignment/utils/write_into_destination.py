
def write_into_destination(destination,csv_files,data):
    with open("{}/{}".format(destination,csv_files),"w") as fp:
        fp.write(data)
