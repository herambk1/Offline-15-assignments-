import json
def fetch_config_data(filename):
    with open(filename) as fp:
        config = json.load(fp)
    return config