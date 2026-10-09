import logging


def get_logger():

    logging.basicConfig(level=10,force=True,filename="app.log",
                        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                        datefmt="%d-%m-%Y %H:%M:%S %p")

    return logging.getLogger(__name__)