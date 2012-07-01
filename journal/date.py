""" Provides functions for working with dates. """

from collections import namedtuple
from time import localtime, strftime, strptime, time

from journal.config import getconf


Date = namedtuple('Date', ['year', 'month', 'day'])
_OFFSETS = {
        'yesterday': -1 * (60 * 60 * 24)
        }


def getcurrentdate():
    """ Return the current date as a string that parsedate will understand.

    See getdate for a note on why a Unix time value of 2012-04-08 04:00 may
    produce "2012-04-07".
    """

    return getdate(time())


def getdate(when_secs):
    """ Return the time given as a string that parsedate will understand.

    Each day lasts until the hour reaches getconf('end_of_day'). e.g., If the
    day ends at 5 and it is 04:00 on 2012-04-08, this function will return
    2012-04-07. """
    end_of_day = getconf('end_of_day')
    when = localtime(when_secs - (60 * 60 * end_of_day))
    year = when.tm_year
    month = when.tm_mon
    day = when.tm_mday
    return "%04d-%02d-%02d" % (year, month, day)


def parsedate(date):
    """ Try to make sense of the user's date string. Raise a ValueError if we
    fail to do so. """
    # If date gives a relative time in words (e.g., "yesterday"), apply the
    # corresponding numerical offset to the current time and use that instead.
    if date in _OFFSETS:
        date = getdate(time() + _OFFSETS[date])
    pieces = date.split("-")
    if len(pieces) != 3:
        raise ValueError()
    year = int(pieces[0])
    month = int(pieces[1])
    day = int(pieces[2])
    return Date(year, month, day)


def datetostruct_time(date):
    """ Convert a date to seconds since the epoch. """
    # This, sadly, is the simplest way to get the day of the week right.
    datestr = "%d %d %d" % date
    return strptime(datestr, "%Y %m %d")


def renderdate(date):
    """ Return a pretty string representation of date. """
    tm = datetostruct_time(date)
    return strftime("%A, %B %d, %Y", tm)

