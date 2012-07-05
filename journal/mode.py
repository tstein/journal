""" Provides methods implementing each invocation mode. """

from time import time

from journal.date import getcurrentdate, getdate, parsedate
from journal.editor import openeditor
from journal.exception import ERR_COULD_NOT_PARSE, ERR_NOT_A_SINGLE_DATE
from journal.exception import FilesystemError, InvocationError
from journal.fs import cat, getentrypath, readable
from journal.templates import entry


def write(command):
    """ Edit an entry for an individual day. """
    if len(command) > 1:
        raise InvocationError(ERR_NOT_A_SINGLE_DATE % "write")
    if len(command) == 0:
        command = [getcurrentdate()]
    date_token = command[0]
    try:
        date = parsedate(date_token)
        filename = getentrypath(date)
        template = entry(date)
    except ValueError:
        raise InvocationError(ERR_COULD_NOT_PARSE % date_token)
    openeditor(filename, template=template)


def read(command):
    """ Write an entry for an individual day to stdout. """
    if len(command) > 1:
        raise InvocationError(ERR_NOT_A_SINGLE_DATE % "read")
    if len(command) == 0:
        command = [getdate(time() - 60 * 60 * 24)]
    date_token = command[0]
    try:
        date = parsedate(date_token)
        filename = getentrypath(date)
    except ValueError:
        raise InvocationError(ERR_COULD_NOT_PARSE % date_token)
    if not readable(filename):
        raise FilesystemError("no entry for given datespec")
    cat(filename)

