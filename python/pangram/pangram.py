def is_pangram(sentence):
    sentence = sentence.upper()
    for i in range(26):
        x = chr(65+i)    
        if x not in sentence:
             return False
    return True
