import re

def count_specific_word(text, search_word):
    if text == "":
        return 0

    words = re.findall(r'\b\w+\b', text.lower())

    count = 0

    for word in words:
        if word == search_word.lower():
            count += 1

    return count