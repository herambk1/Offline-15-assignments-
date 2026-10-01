from log_utils.log_config import log_confing
logger = log_confing(str(__file__).split("\\")[-1])

def read_file(source,file):
    try:
        logger.info("Reading file: %s", file)
        with open("{}\{}".format(source,file),'rb') as fp:
            data = fp.read()
        logger.info("File read successfully: %s", file)
        return data

    except Exception as e:
        logger.error("Error reading file %s: %s", file, e)
        print(e)

