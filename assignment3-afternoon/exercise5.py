import os
DELIMITER = ","


def parse_csv_imperative(s):
    """
    >>> parse_csv_imperative("county,state,income")
    ["county", "state", "income"]
    >>> parse_csv_imperative("Kings,NY,1234")
    ["Kings", "NY", "1234"]
    """
    if not isinstance(s, str):
        raise ValueError("Input must be a string.")
    if s.strip() == "":
        return []
    return s.strip().split(DELIMITER)


def parse_csv_recursive(s):

    # Note: this function should have no doc-tests.

    # TODO: complete this function.
    return None


def parse_csv_recursive_wrapper(s):
    """
    # TODO: add doc-tests.
    """

    # TODO: complete this function.
    return None


def read_csv(filepath):
    """
    # TODO: add a single doc-test to check if the file exists.
    """

    # TODO: complete this function.
    return None
