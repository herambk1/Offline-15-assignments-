import logging

def log_confing(name):
    logging.basicConfig(level=10, filename ='server.log', filemode='a',format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        datefmt='%d-%b-%Y %I:%M:%S %p')

    logger = logging.getLogger(name)
    return logger

