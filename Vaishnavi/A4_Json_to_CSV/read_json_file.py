import json
def read_file():
    with open('empdata.json') as fp:
        data = json.load(fp)

    return data