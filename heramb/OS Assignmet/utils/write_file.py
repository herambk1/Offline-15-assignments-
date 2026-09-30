import os
def write_file(filename, data):
    try:
        with open(filename,"wb") as file:
            file.write(data)

    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filename}")

    except OSError:
        raise OSError(f"Unabble to write file: {filename}")
    