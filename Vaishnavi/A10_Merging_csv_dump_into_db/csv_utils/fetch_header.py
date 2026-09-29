from log_utils.log_config_data import log_config

logger = log_config(str(__file__).split("\\")[-1])

def fetch_header(data):
    logger.info("Fetching CSV header")
    header = []
    for key, values in data.items():
        if key not in header:
            header.append(key)
    logger.info("Header fetched successfully")
    return header