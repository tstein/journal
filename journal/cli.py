""" Provides an entry point. """

from argparse import ArgumentParser
from sys import exit
from traceback import print_exc

from journal import mode
from journal.date import getcurrentdate
from journal.exception import InvocationError


_DESCRIPTION = 'Modify and review a journal of your activities.'
_ERR_UNCAUGHT_EXC = 'main: uncaught exception'

_WRITE_CMD = 'write'
_CAT_CMD = 'read'
_CMD_FUNCS = {
    _WRITE_CMD: mode.write,
    _CAT_CMD:   mode.cat
}


def main():
    parser = _makeparser()
    args = parser.parse_args()
    command = args.command
    if command:
        if command[0] in _CMD_FUNCS:
            mode = command[0]
            command = command[1:]
        else:
            # Default to editing and let mode.write validate the rest.
            mode = _WRITE_CMD
    else:
        # Default to editing the entry for the current day.
        mode = _WRITE_CMD
        command = [getcurrentdate()]
    # Hand off to something in journal.mode.
    try:
        _CMD_FUNCS[mode](command)
    except InvocationError as invoc_e:
        _exit(1, invoc_e.message)
    except:
       print_exc()
       _exit(127, _ERR_UNCAUGHT_EXC)
    _exit(0)


def _makeparser():
    """ Initialize an argument parser. """
    parser = ArgumentParser(description=_DESCRIPTION)
    parser.add_argument('command', action='store', nargs='*',
                        help='The date to modify or view.')
    return parser


def _exit(code, msg=None):
    """ Exit point. """
    if msg is not None:
        print('journal: ' + msg)
        exit(code)


if __name__ == '__main__':
    main()

