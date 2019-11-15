import re

def count_words(sentence):
    sentence = sentence.lower()

    words = re.findall(r"[a-zA-Z0-9]+[']{0,1}[a-zA-Z0-9]|[a-zA-Z0-9]", sentence)
    wordCount = {}
    for word in words:
        wordCount[word] = words.count(word)

    return wordCount