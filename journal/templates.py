""" Provides functions that create text templates. """

from journal.date import renderdate


def entry(date):
    """ Return the template for new entries. """
    datestr = "journal for " + renderdate(date)
    numstars = len(datestr) + 8
    tmplt  = '*' * numstars + '\n'
    tmplt += '*   ' + datestr + '   *\n'
    tmplt += '*' * numstars + '\n\n\n'
    return tmplt

