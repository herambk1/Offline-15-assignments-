def fetch_key(data):
    keys = []
    for key, values in data[0].items():
        if key not in keys:
            keys.append(key)
    return keys