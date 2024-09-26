def calculate_interest(balance, rate, transactions):
    """
    Calculate the compound interest paid monthly on the balance of a bank account.

    Args:
      balance: Current balance of the account at the start of the calculation.
      rate: Annual interest rate (as a decimal, e.g., 0.05 for 5%).
      transactions: A list of tuples representing transactions (day, amount).
          Positive amounts are deposits, negative are withdrawals.

    Returns:
      The interest rate to be paid at the end of the month.

    >>> transactions = [(5, 500), (10, -200), (20, 100)]
    >>> interest = calculate_interest(1000, 0.05, transactions)
    >>> print("%.2f" % interest)
    5.29
    """
    
    days_in_month = 30  # Assume a 30-day month.
    days_in_year = 365  # Assume a normal year.

    # Daily interest rate, that compounds to the annual rate.
    daily_rate = (1 + rate) ** (1 / days_in_year) - 1



if '__main__' == __name__:
    # Doc-tests
    doctests = doctest.testmod(optionflags=doctest.ELLIPSIS)
    assert 0 == doctests.failed, 'Some doc-tests failed, exiting...'

    # Example usage:
    initial_balance = 1000
    annual_rate = 0.05

    # Transactions: day 5 deposit 500, day 10 withdraw 200, day 20 deposit 100.
    transactions = [(5, 500), (10, -200), (20, 100)]

    interest = calculate_interest(initial_balance, annual_rate, transactions)

    print(f"Interest to be paid at the end of the month: ${interest:.2f}")

