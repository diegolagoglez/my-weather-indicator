#!/usr/bin/env python3

import datetime

COLOR_NORMAL = '\033[0m'
COLOR_DEBUG = ''
COLOR_INFO = '\033[94m'
COLOR_WARNING = '\033[33m'
COLOR_ERROR = '\033[91m'
COLOR_FATAL = '\033[1;37;41m'


def log(level_name, message):
    print("[{}] {}: {}".format(datetime.datetime.now()
                               .strftime('%Y-%m-%d %H:%M:%S'),
                               level_name, message))


def debug(message):
    log(COLOR_DEBUG + "DEBUG" + COLOR_NORMAL, message)


def info(message):
    log(COLOR_INFO + "INFO" + COLOR_NORMAL, message)


def warning(message):
    log(COLOR_WARNING + "WARNING" + COLOR_NORMAL, message)


def error(message):
    log(COLOR_ERROR + "ERROR" + COLOR_NORMAL, message)


def fatal(message):
    log(COLOR_FATAL + "FATAL" + COLOR_NORMAL, message)
