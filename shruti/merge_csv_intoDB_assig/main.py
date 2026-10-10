from utility.logger import logger
from utility.merge_csv_helper import get_all_csv_files,merge_csv_files,write_merged_csv
from utility.db_script import db_script
logger = logger(__name__)

def main():
    input_dir = r"/\input_files"
    filename = "merged.csv"
    all_files = get_all_csv_files(input_dir)
    header,data =merge_csv_files(all_files)
    write_merged_csv(filename,header,data)
    db_script(data)


if __name__ == "__main__":
    main()