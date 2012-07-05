""" Provides an entry point. """

from argparse import ArgumentParser
from sys import exit
from traceback import print_exc

from journal import mode
from journal.exception import InvocationError, JournalError


_DESCRIPTION = 'Modify and review a journal of your activities.'
_ERR_UNCAUGHT_EXC = 'main: uncaught exception'

_WRITE_CMD = 'write'
_READ_CMD = 'read'
_CMD_FUNCS = {
    _WRITE_CMD: mode.write,
    _READ_CMD:  mode.read
}


def main():
    parser = _makeparser()
    args = parser.parse_args()
    mode = args.mode
    mode_args = args.mode_args
    try:
        if not mode:
            raise InvocationError("no command given")
        mode = mode[0]
        if mode not in _CMD_FUNCS:
            raise InvocationError("invalid mode: %s" % mode)
        # Hand off to something in journal.mode.
        _CMD_FUNCS[mode](mode_args)
    except JournalError as e:
        _exit(1, e.message)
    except:
        print_exc()
        _exit(127, _ERR_UNCAUGHT_EXC)
    _exit(0)


def _makeparser():
    """ Initialize an argument parser. """
    parser = ArgumentParser(description=_DESCRIPTION)
    parser.add_argument('mode', action='store', nargs=1,
                        help='The mode of operation.')
    parser.add_argument('mode_args', metavar='args', action='store', nargs='*',
                        help='Mode-specific arguments.')
    return parser


def _exit(code, msg=None):
    """ Exit point. """
    if msg is not None:
        print('journal: ' + msg)
        exit(code)


if __name__ == '__main__':
    main()

