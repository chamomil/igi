import re
from help_functions import lowercase_search, name_search, quotes_search, get_text, count_nondec

EXCEPTIONS = ['Mr\.', 'Mrs\.', 'Dr\.', 'ca?\.', 'et al\.', 'Lt\.', 'Rep\.', 'B\.A\.',
              'Ph\.D\.', 'M\.D\.', 'Jan\.', 'Feb\.', 'Mar\.', 'Apr\.', 'Jun\.', 'Jul\.', 'Aug\.', 'Sept\.', 'Oct\.',
              'Nov\.', 'Dec\.', 'Mon\.', 'Tue?s?\.', 'Thu?r?\.', 'Sat\.', 'Sun\.', 'in\.', 'lbs\.', 'sec\.', 'min\.',
              'hr?\.', 'wk\.', 'a\.m\.', 'p\.m\.', 'mo\.', 'yr\.', 'y\.o\.', 'cent\.', 'B\.C\.', 'A\.D\.']


def sentences(text: str):
    sentence_list = re.findall(r'[.?!]+\s"?\w', text)
    amount_of_sentence = len(sentence_list)
    amount_of_nondec = count_nondec(sentence_list)

    amount_of_sentence, amount_of_nondec = lowercase_search(sentence_list, amount_of_sentence, amount_of_nondec)
    amount_of_sentence -= name_search(text)  # checking if the text contains name for example A. A. Adams

    for exception in EXCEPTIONS:  # checking all other words which can have upper letter after or/and cannot
        reg_ex = r'\b' + exception + r'\s\w' # be placed in the end
        found_abbreviations = re.findall(reg_ex, text)
        for abbreviation in found_abbreviations:
            if abbreviation[-1].isupper():
                amount_of_sentence -= 1

    quotes_list = re.findall(r'[?!]+"\s\w', text)
    amount_of_sentence, amount_of_nondec = quotes_search(quotes_list, amount_of_sentence, amount_of_nondec)

    amount_of_sentence += 1
    print(f"Amount of sentences: {amount_of_sentence}")
    print(f"Amount of non-declarative sentences: {amount_of_nondec}")
    return amount_of_sentence


def average_length(text: str, amount_of_sentences):
    words = re.findall(r'\b\w+\b', text)
    amount_of_words = len(words)
    length = 0

    for word in words:
        length += len(word)

    average_sentence = length / amount_of_sentences
    print(f"Average length of the sentence: {average_sentence}")

    average_word = length / amount_of_words
    print(f"Average length of the sentence: {average_word}")


def main():
    text = get_text()
    amount_of_sentences = sentences(text)
    average_length(text, amount_of_sentences)


if __name__ == '__main__':
    main()
