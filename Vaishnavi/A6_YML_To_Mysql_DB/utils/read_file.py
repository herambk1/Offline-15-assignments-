def read_file(filename):
    with open(filename) as fp:
        data = pyaml.yaml.safe_load(fp)
    return data['students']