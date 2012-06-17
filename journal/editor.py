""" Open an external editor in the terminal. """

from os import makedirs, path, system
from subprocess import PIPE, Popen


def openeditor(filename, template=""):
    """ Open an editor. That editor is vim. """
    # If this file hasn't yet been created, make all necessary directories and
    # start with a template.
    if not path.exists(filename):
        try:
            makedirs(path.dirname(filename))
        except OSError:
            pass
        with open(filename, 'wb') as f:
            catproc = Popen("cat", stdin=PIPE, stdout=f)
            catproc.communicate(input=template)
    # envoy is far more comfortable, but doesn't automatically hand off the tty
    # correctly. system() does.
    system("vim + %s" % filename)

