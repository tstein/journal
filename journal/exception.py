""" Provides various exception types and common error messages. """


ERR_COULD_NOT_PARSE = "couldn't understand %s"
ERR_NOT_A_SINGLE_DATE = "%s requires a single date"


class JournalError(Exception):
    """ Base class for program exceptions. """
    pass


class InvocationError(JournalError):
    """ Indicates an invalid command-line invocation. """
    pass

