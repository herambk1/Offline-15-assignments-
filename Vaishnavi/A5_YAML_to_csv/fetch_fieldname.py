def fieldname(data):
    fname = []
    for key, values in data[0].items():
        if key not in fname:
            fname.append(key)
    return fname