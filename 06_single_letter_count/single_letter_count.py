def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """
    word_lowercased = word.lower()
    letter_lowercased = letter.lower()

    count = word_lowercased.count(letter_lowercased)

    return count

single_letter_count('aaron', 'a')
