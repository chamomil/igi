from sentence_parsing import sentences, average_length, ngrams
from help_functions import get_text


def main():
    text = get_text()
    amount_of_sentences = sentences(text)
    words = average_length(text, amount_of_sentences)
    ngrams(text, words)


if __name__ == '__main__':
    main()
