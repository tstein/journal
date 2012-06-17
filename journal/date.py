""" Provides functions for working with dates. """

from collections import namedtuple
from time import localtime, strftime, struct_time, time

from journal.config import getconf


Date = namedtuple('Date', ['year', 'month', 'day'])


def getcurrentdate():
    """ Return the current date as a Date namedtuple.

    The current day lasts until the hour reaches getconf('end_of_day'). e.g.,
    If the day ends at 5 and it is 04:00 on 2012-04-08, this function will
    return 2012-04-07."""
    end_of_day = getconf('end_of_day')
    now = localtime(time() - (60 * 60 * end_of_day))
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

