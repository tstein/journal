""" Provides functions for working with dates. """

from collections import namedtuple
from time import localtime, strftime, struct_time


Date = namedtuple('Date', ['year', 'month', 'day'])


def getcurrentdate():
    """ Return the current date as a Date namedtuple. """
    now = localtime()
    year = now.tm_year
    month = now.tm_mon
    day = now.tm_mday
    return Date(year, month, day)


def parsedate(date):
    """ Try to make sense of the user's date string. Raise a ValueError if we
    fail to do so. """
    pieces = date.split("-")
    if len(pieces) != 3:
        raise ValueError()
    year = int(pieces[0])
    month = int(pieces[1])
    day = int(pieces[2])
    return Date(year, month, day)

def renderdate(date):
    """ Return a pretty string representation of date. """
    # Fill this struct_time with garbage. strftime will never look at those
    # fields.
    tm = struct_time((date.year,
                      date.month,
                      date.day,
                      0, 0, 0, 0, 1, -1))
    return strftime("%A, %B %d, %Y", tm)

