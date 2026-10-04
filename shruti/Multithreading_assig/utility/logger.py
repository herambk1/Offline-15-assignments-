import logging

def logger(name):
    logging.basicConfig(level=10, filename= "server.log",
                    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')

    logger = logging.getLogger(name)
    return logger