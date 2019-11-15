def score(word):
    word = word.upper()
    dictionary = dict.fromkeys(['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'], 1)
    dictionary.update(dict.fromkeys(['D', 'G'], 2))
    dictionary.update(dict.fromkeys(['B', 'C', 'M', 'P'], 3))
    dictionary.update(dict.fromkeys(['F', 'H', 'V', 'W', 'Y'], 4))
    dictionary.update(dict.fromkeys(['K'], 5))
    dictionary.update(dict.fromkeys(['J', 'X'], 8))
    dictionary.update(dict.fromkeys(['Q', 'Z'], 10))
    
    value = 0
    for letter in word:
        value += dictionary[letter]

    return value