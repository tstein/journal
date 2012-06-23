""" Provides methods implementing each invocation mode. """

from journal.date import parsedate
from journal.editor import openeditor
from journal.exception import ERR_COULD_NOT_PARSE, InvocationError
from journal.fs import getentrypath
from journal.templates import entry


_ERR_NOT_A_SINGLE_DATE = "write requires a single date"


def write(command):
    """ Edit an entry for an individual day. """
    if len(command) != 1:
        raise InvocationError(_ERR_NOT_A_SINGLE_DATE)
    date_token = command[0]
    try:
        date = parsedate(date_token)
        filename = getentrypath(date)
        template = entry(date)
    except ValueError:
        raise InvocationError(ERR_COULD_NOT_PARSE % date_token)
    openeditor(filename, template=template)


def cat(command):
    pass

