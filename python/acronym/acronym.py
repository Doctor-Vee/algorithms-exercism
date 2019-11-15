import re

def abbreviate(words):
    words = words.upper()
    wordArray = re.findall(r"[a-zA-Z0-9]+[']{0,1}[a-zA-Z0-9]|[a-zA-Z0-9]", words)
    abbreviation = ""
    for word in wordArray:
        abbreviation+=word[0]

    return abbreviation