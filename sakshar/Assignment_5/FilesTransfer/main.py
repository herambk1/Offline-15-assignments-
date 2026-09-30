import fileProcess.utils.read_file as utl
import fileProcess.transform.trans_file as trns

def main():
    source_dir = r"C:\Users\saksh\PycharmProjects\PythonProject\FilesTransfer\SourceDir"
    target_dir = r"C:\Users\saksh\PycharmProjects\PythonProject\FilesTransfer\TargetDir"
    extracted_csv_files = trns.extract_csv_file_names(source_dir)
    utl.process_file(extracted_csv_files, source_dir, target_dir)

if __name__ == "__main__":
    main()