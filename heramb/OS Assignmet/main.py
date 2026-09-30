import os

from utils import read_file as rf
from utils import write_file as wr
from move_file import movefile as mv


def main():

    source_dir = input("Enter the source directory: ").strip()

    target_dir = input("Enter the target directory: ").strip()

    try:
        files = mv.extract_file_names(source_dir)

        if not files:
            print("No files found")
            return

        print("\nAvailable files:\n")

        for file in files:
            print(file)

        file_input = input("\nEnter filename or filenames with ',': ")

        input_files = file_input.split(",")

        filenames = []
        invalid_files = []

        for file in input_files:
            file = file.strip()
            found = False

            for available_file in files:
                if file.lower() == available_file.lower():
                    filenames.append(available_file)
                    found = True
                    break

            if not found:
                invalid_files.append(file)

        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        if not os.path.isdir(target_dir):
            raise NotADirectoryError(f"{target_dir} is not a directory")

        moved_files = []
        failed_files = []

        for filename in filenames:

            try:
                os.chdir(source_dir)

                data = rf.read_file(filename)

                os.chdir(target_dir)

                wr.write_file(filename, data)

                os.chdir(source_dir)

                os.remove(filename)

                moved_files.append(filename)

            except Exception as e:
                failed_files.append(
                    f"{filename} -> {e}"
                )

        if moved_files:
            print("\nMoved files:")

            for filename in moved_files:
                print(filename)

        if invalid_files:
            print("\nFile not found:")

            for filename in invalid_files:
                print(filename)

        if failed_files:
            print("\nFailed files:")

            for error in failed_files:
                print(error)

    except Exception as e:
        print("Error: ",e)


if __name__ == "__main__":
    main()
