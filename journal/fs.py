""" Manipulate paths and files. """

from os import path

from journal.config import getconf


def getentrypath(date):
    """ Create the absolute path where the entry for date should go. """
    base = path.expanduser(getconf('entry_dir'))
    yearstr = str(date.year)
    monthstr = "%02d" % date.month
    daystr = "%02d" % date.day
    basename = "%s.txt" % daystr
    return path.join(base, yearstr, monthstr, basename)

