STOPWORDS = ["of", "a", "and", "the"]

def convert_to_title_case(s):
    """
    >>> convert_to_title_case("a tale of two cities")
    'A Tale of Two Cities'

    """

    if not isinstance(s, str):
        raise ValueError("s should be a string.")

    s = s.lower()
    title_cased = []
    words = s.split()
    for i, word in enumerate(words):
        if i == 0 or not word in STOPWORDS:
            title_cased.append(word.capitalize())
        else:
            title_cased.append(word)

    return " ".join(title_cased)


