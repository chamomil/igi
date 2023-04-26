import re
from help_functions import lowercase_search, name_search, quotes_search, count_nondec, check_numbers, max_search
from constants import EXCEPTIONS


def sentences(text: str):
    sentence_list = re.findall(r'[.?!]+\s"?\w', text)
    amount_of_sentence = len(sentence_list)
    amount_of_nondec: int = count_nondec(sentence_list)

    amount_of_sentence, amount_of_nondec = lowercase_search(sentence_list, amount_of_sentence, amount_of_nondec)
    amount_of_sentence -= name_search(text)  # checking if the text contains name for example A. A. Adams

    for exception in EXCEPTIONS:  # checking all other words which can have upper letter after or/and cannot
        reg_ex = r'\b' + exception + r'\s\w'  # be placed in the end
        found_abbreviations = re.findall(reg_ex, text)
        for abbreviation in found_abbreviations:
            if abbreviation[-1].isupper():
                amount_of_sentence -= 1

    quotes_list = re.findall(r'[?!]+"\s\w', text)
    amount_of_sentence, amount_of_nondec = quotes_search(quotes_list, amount_of_sentence, amount_of_nondec)

    try:
        if text[-1] == '.':
            amount_of_sentence += 1
        if text[-1] == '?' or text[-1] == '!':
            amount_of_nondec += 1
            amount_of_sentence += 1
    except:
        raise Exception

    return amount_of_sentence, amount_of_nondec


def average_length(text: str, amount_of_sentences):
    words = re.findall(r'\b\w+\b', text)
    check_numbers(words)
    amount_of_words = len(words)
    length = 0

    for word in words:
        length += len(word)

    average_sentence = length / amount_of_sentences

    average_word: float = 0.0
    try:
        average_word = length / amount_of_words
    except ZeroDivisionError:
        print("No words were found")

    return words, average_sentence, average_word


def ngrams(words, n):
    ngrams_dict = {}
    ngram = ""

    for i in range(0, len(words) - n + 1):
        for j in range(i, i + n):
            ngram += words[j] + ' '
        try:
            val = ngrams_dict[ngram]
            ngrams_dict[ngram] = val + 1
        except:
            ngrams_dict.__setitem__(ngram, 1)
        ngram = ""

    return ngrams_dict
