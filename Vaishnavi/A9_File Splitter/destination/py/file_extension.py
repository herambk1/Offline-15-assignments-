import os
def file_ext(source, file):
    extension_file = os.path.join(source, file)
    extension = extension_file.split("\\")[-1].split(".")[-1]
    return extension