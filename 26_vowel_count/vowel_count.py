def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels = "aeiouAEIOU"
    count_map = {}

    for char in phrase:
        if char.lower() in vowels:
            count_map[char.lower()] = count_map.get(char.lower(), 0) + 1

    return count_map