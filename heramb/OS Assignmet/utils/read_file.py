import os

def read_file(filename):
    try:
        with open(filename, 'rb') as file:
            return file.read()

    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filename}")

    except Fileerror as e:
        raise Fileerror(f"unable to read file: {e}{filename}")


