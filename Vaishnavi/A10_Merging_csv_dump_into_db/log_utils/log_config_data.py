import logging
def log_config(name):
    logging.basicConfig(
        level=10,
        filename='server.log',
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt='%d-%b-%y %I:%M:%S %p'
    )
    logger = logging.getLogger(name)
    return logger