import logging
from logging import Logger, StreamHandler, FileHandler
from functools import wraps


# A decorator function for logging.
def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called.")  # TODO
        return func(*args, **kwargs)
    return with_logging


class Log4P():

    def __init__(self):
        self.log = Logger('Log4P', logging.DEBUG)
        self.log.addHandler(StreamHandler())
        self.log.addHandler(FileHandler('../ifee.log'))

    def show_log(self):
        self.log.debug('The showLog method that call Logger.info method!')




def main():
    log = Log4P()
    log.show_log()


if __name__ == '__main__':
    main()
