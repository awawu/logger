#! /usr/bin python3
# -*- coding: utf-8 -*-

import logging
import logcolorer
import os

class Logger:
    def __init__(self, path, console_level = logging.WARNING, file_level = logging.DEBUG):
        self.logger = logging.getLogger(path)
        self.logger.setLevel(logging.DEBUG)

        fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')

        # log to console
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(fmt)
        console_handler.setLevel(console_level)

        # log to file
        file_handler = logging.FileHandler(path)
        file_handler.setFormatter(fmt)
        file_handler.setLevel(file_level)

        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warn(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)

if __name__ == '__main__':
    log = Logger('test.log', console_level = logging.DEBUG)
    log.debug('a debug')
    log.info('an info')
    log.warning('a warning')
    log.error('an error')
    log.critical('a critical that make you die')

