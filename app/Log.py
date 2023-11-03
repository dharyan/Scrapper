#
# Log v1.0.0
# Autor Diogo Hidalgo Daia
#

# Importes
import datetime
import logging
import time

project_name = f'crawler'

def get_logger(logger_name):
    """
    :param logger_name: str , defines logger name
    :return: logging.logger object
    """
    path_file_log = f'../log/log_{project_name}_{datetime.datetime.now().strftime("%d_%m_%Y")}.log'
    logging.basicConfig(
        filename=path_file_log,
        level=logging.INFO,
        datefmt="%d-%m-%Y %H:%M:%S",
        format="'%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s'"
    )
    logger = logging.getLogger(logger_name)
    
    Stream_Handler = logging.StreamHandler()
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    Stream_Handler.setFormatter(formatter)
    
    logger.addHandler(Stream_Handler)

    return logger

def time_now():
    time_now = time.perf_counter()
    return time_now

def execution_time(start_time):
    execution_time = time_now() - start_time
    return execution_time
