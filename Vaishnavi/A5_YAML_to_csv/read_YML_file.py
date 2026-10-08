import pyaml
def read_file():
    with open('student.yml') as fp:
        data = pyaml.yaml.safe_load(fp)
    return data
