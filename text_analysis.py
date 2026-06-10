import re
from collections import Counter


def count_specific_word(text, search_word):
    words = re.findall(r'\b\w+\b', text.lower())
    return words.count(search_word.lower())


def identify_most_common_word(text):
    words = re.findall(r'\b\w+\b', text.lower())

    if not words:
        return None

    counter = Counter(words)
    return counter.most_common(1)[0][0]


def calculate_average_word_length(text):
    words = re.findall(r'\b\w+\b', text)

    if not words:
        return 0.0

    total_length = 0

    # Explicit for loop
    for word in words:
        total_length += len(word)

    return total_length / len(words)


def count_paragraphs(text):
    paragraphs = [p for p in text.split("\n\n") if p.strip()]
    return len(paragraphs)


def count_sentences(text):
    sentences = re.split(r'[.!?]+', text)
    sentences = [s for s in sentences if s.strip()]
    return len(sentences)