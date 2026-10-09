import logging
def get_logger_name(name):
    logging.basicConfig(level=10,force = True, filename='server.log',
                   format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                   datefmt='%d-%m-%Y %H:%M:%S %p')
    logger = logging.getLogger(name)
    return logger