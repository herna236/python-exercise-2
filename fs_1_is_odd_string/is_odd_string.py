def is_odd_string(word):
    """Is the sum of the character-positions odd?

    Word is a simple word of uppercase/lowercase letters without punctuation.

    For each character, find it's "character position" ("a"=1, "b"=2, etc).
    Return True/False, depending on whether sum of those numbers is odd.

    For example, these sum to 1, which is odd:
    
        >>> is_odd_string('a')
        True

        >>> is_odd_string('A')
        True

    These sum to 4, which is not odd:
    
        >>> is_odd_string('aaaa')
        False

        >>> is_odd_string('AAaa')
        False

    Longer example:
    
        >>> is_odd_string('amazing')
        True
    """
    # Define a function to get the character position
    def char_position(char):
        return ord(char.lower()) - ord('a') + 1

    # Calculate the sum of character positions for each character in the word
    total_position = sum(char_position(char) for char in word)

    # Return True if the sum is odd, False otherwise
    return total_position % 2 == 1