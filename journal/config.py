""" Implements a global configuration store. """

from os import path


_CONFIG = dict()

# FIXME: MAGIC
_CONFIG['config_dir'] = '~/.journal'
_CONFIG['entry_dir'] = path.join(_CONFIG['config_dir'], 'entries')


def getconf(key):
    """ Return the configuration value for the given key or None if no such
    value exists. """
    if key in _CONFIG:
        return _CONFIG[key]
    else:
        return None

