import os
from utils.read_file import read_file
from utils.write_into_destination import write_into_destination
from list_csv_files import list_csv_files
from delete_csv_from_source import delete_from_source


def main():
    source =r"C:\Users\vaish\OneDrive\Documents\documents"
    destination = r"C:\Users\vaish\OneDrive\Documents\Destination"
    csv_files = list_csv_files(source)
    print(csv_files)
    for file in csv_files:
        fdata = read_file(source,file)
        write_into_destination(destination,file,fdata)
        delete_from_source(source,file)


if __name__=="__main__":
    main()