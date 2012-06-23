""" Provides various exception types and common error messages. """


ERR_COULD_NOT_PARSE = "couldn't understand %s"


class InvocationError(Exception):
    """ Indicates an invalid command-line invocation. """
    pass

