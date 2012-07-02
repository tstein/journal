""" Provides an entry point. """

from argparse import ArgumentParser
from sys import exit
from traceback import print_exc

from journal import mode
from journal.exception import InvocationError


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
    command = args.command
    try:
        if not command:
            raise InvocationError("no command given")
        if command[0] not in _CMD_FUNCS:
            raise InvocationError("invalid mode: %s" % command[0])
        mode = command[0]
        command = command[1:]
        # Hand off to something in journal.mode.
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

