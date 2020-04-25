import time
import logging

def log(func):
    logging.basicConfig(filename='machine.log', level=logging.INFO, format='(tde-roqu)%(message)s')

    def inner1(*args, **kwargs):
        begin = time.time()
        returned_value = func(*args, **kwargs)
        end = time.time()

        logging.info("Running: {:16}[ exec-time = {:.3f} ms ]".format(func.__name__, end - begin))

        return returned_value  
    return inner1