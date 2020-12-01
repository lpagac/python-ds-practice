def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """

    # O(n^2) solution currently, can implement freq counter for O(n) answer
    return {letter: phrase.count(letter) for letter in phrase}

    # Considered looping over a set (improvement for runtime?)
    # return {letter: phrase.count(letter) for letter in set(phrase)}
