import doctest
import datetime

def compute_interest(balance, rate, day, month):
    """
    Compute whether a customer should be paid interest, only on
    January 2nd of a year.

    Args:
      balance:
        A number for the balance on the account.

      rate:
        A number for the current interest rate.

      day:
        An integer for the day of the month under consideration (not 0-indexed)

      month:
        An integer for the month (not 0-indexed)

    Returns:
      A number with the interest to be paid.
    
    >>> today = datetime.datetime.today()
    >>> i = compute_interest(1000, 0.05, 27, 9)
    The customer ...
    >>> i
    0
    >>> i = compute_interest(1000, 0.05, 2, 1)
    The customer ...
    >>> i
    50.0

    """

    # Note: in this exercise, days and months are NOT zero-indexed.
    if 2 == day & 1 == month:
        interest = balance * rate
        msg = ("The customer should be paid this interest on day"
               " %s and month %s: %3.1f") % (interest, day, month)
        
    else:
        interest = 0
        msg = ("The customer should not be paid interest on day %s and" +
               " month %s") % (day, month)
        
    print(msg)
    return interest


if '__main__' == __name__:
    doctests = doctest.testmod(optionflags=doctest.ELLIPSIS)
    assert 0 == doctests.failed, 'Some doc-tests failed, exiting...'

    print("Your doc-tests pass, congratulations!")

    today = datetime.datetime.today()
    compute_interest(1000, 0.04, today.day, today.month)

    compute_interest(1000, 0.04, 2, 1)
