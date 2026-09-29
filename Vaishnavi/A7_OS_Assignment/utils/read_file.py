def read_file(source,filename):
    with open("{}/{}".format(source,filename)) as fp:
        data = fp.read()
    return data