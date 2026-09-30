import os


def extract_file_names(source_dir):
    try:
        if not os.path.exists(source_dir):
            raise FileNotFoundError(f"{source_dir} does not exist")

        if not os.path.isdir(source_dir):
            raise NotaDirectoryError(f"{source_dir} is not a directory")

        os.chdir(source_dir)

        files=[]
        for filename in os.listdir():
            if os.path.isfile(filename):
                files.append(filename)
        return files

    except errors as e:
        return e

