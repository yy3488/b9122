import doctest
import numpy

def sum_numpy(a, b):
    """
    Sum two numbers.

    >>> import numpy
    >>> a = numpy.uint8(1)
    >>> b = numpy.uint8(2)
    >>> bool(sum_numpy(a, b) == 3)
    True
    >>> a = numpy.uint8(250)
    >>> b = numpy.uint8(250)
    >>> bool(sum_numpy(a, b) == 500)
    True
    """

    return a + b


if '__main__' == __name__:
    doctests = doctest.testmod(optionflags=doctest.ELLIPSIS)
    assert 0 == doctests.failed, 'Some doc-tests failed, exiting...'

    print("Your doc-tests pass, congratulations!")

