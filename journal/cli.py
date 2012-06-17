""" Provides an entry point. """

from argparse import ArgumentParser

from journal.date import getcurrentdate, parsedate
from journal.editor import openeditor
from journal.fs import getentrypath
from journal.templates import entry


_DESCRIPTION = 'Modify and review a journal of your activities.'

def main():
    parser = _makeparser()
    args = parser.parse_args()
    if args.date is None:
        date = getcurrentdate()
    else:
        date = parsedate(args.date)
    filename = getentrypath(date)
    tmplt = entry(date)
    openeditor(filename, template=tmplt)


def _makeparser():
    """ Initialize an argument parser. """
    parser = ArgumentParser(description=_DESCRIPTION)
    parser.add_argument('date', action='store', nargs='?',
                        help='The date to modify or view.')
    return parser


if __name__ == '__main__':
    main()

