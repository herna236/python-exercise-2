def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    letter_count = {}

    for letter in phrase:
        # default to 0 (start with 0 for the letter count)
        current_count = letter_count.get(letter, 0)

        letter_count[letter] = current_count + 1

    return letter_count