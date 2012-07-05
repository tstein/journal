""" Manipulate paths and files. """

import stat as stat_mod
from os import path, stat, system

from journal.config import getconf


def getentrypath(date):
    """ Create the absolute path where the entry for date should go. """
    base = path.expanduser(getconf('entry_dir'))
    yearstr = str(date.year)
    monthstr = "%02d" % date.month
    daystr = "%02d" % date.day
    basename = "%s.txt" % daystr
    return path.join(base, yearstr, monthstr, basename)


def cat(filename):
    """ Write a file to stdout. """
    system("cat \"%s\"" % filename)


def exists(filename):
    """ Returns whether a file exists. """
    return path.exists(filename)


def check_exists(func):
    """ Decorator that wraps a function to check if its first argument
    exists. """
    def wrapped(*args):
        if len(args) != 1:
            raise ValueError("check_exists used on non-unary function")
        if not exists(args[0]):
            return False
        else:
            return func(*args)
    return wrapped

@check_exists
def readable(filename):
    """ Returns whether a file exists and is readable. """
    mode = stat(filename).st_mode
    return not stat_mod.S_ISDIR(mode) and (mode & stat_mod.S_IRUSR != 0)


@check_exists
def writable(filename):
    """ Return whether a file exists and is writable. """
    mode = stat(filename).st_mode
    return not stat_mod.S_ISDIR(mode) and (mode & stat_mod.S_IWUSR != 0)

