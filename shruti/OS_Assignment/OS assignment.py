
import os
from OS_utilty.logger import logger
from OS_utilty.Os_helper import  destination_folder,file_ext,read_then_write

logger = logger(__name__)

def main():
    source_path = r"D:\AINexusIT\Git\Offline-15-assignments-\shruti\OS_Assignment\source"
    dest_path = r"D:\AINexusIT\Git\Offline-15-assignments-\shruti\OS_Assignment\targetdir"
    destination_folder(dest_path)
    files = os.listdir(source_path)
    for file in files:
        source_file = os.path.join(source_path, file)
        file_type = file_ext(file)
        dest_folder = os.path.join(dest_path, file_type)
        destination_file = os.path.join(dest_folder, file)
        read_then_write(source_file, destination_file)



if __name__=="__main__":
    main()