"""custom logging module"""


import sys
import logging
from os import path, remove

# def main():
class ClassLog(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def get_logger(self, logname):
        self.logname = logname
        # If applicable, delete the existing log file as it is overwritten each time
        if path.isfile(self.logname):
            remove(self.logname)

        # Create the Logger
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        # Create the Handler for logging data to a file
        logger_handler = logging.FileHandler(path.basename(sys.argv[0][:-3]) + '.log', 'w', 'utf-8')
        logger_handler.setLevel(logging.DEBUG)

        # Create a Formatter for formatting the log messages
        logger_formatter = logging.Formatter('%(asctime)s %(name)s - %(levelname)s - %(message)s')

        # Add the Formatter to the Handler
        logger_handler.setFormatter(logger_formatter)

        # Add the Handler to the Logger
        self.logger.addHandler(logger_handler)
        self.logger.info('logger configuration_complete!')


# Python program to execute main directly
# print("Always executed")
#
# if __name__ == "__main__":
#     pass
# else:
#     print("Executed when imported")