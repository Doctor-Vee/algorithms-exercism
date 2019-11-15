def is_isogram(string):
    string = string.lower()
    for letter in string:
        if letter.isalpha() and string.count(letter) > 1: 
            return False
    return True

    
    # def is_isogram(string):
    # lower_alphabet_list = [c.lower() for c in string if c.isalpha()]
    # return len(set(lower_alphabet_list)) == len(lower_alphabet_list)