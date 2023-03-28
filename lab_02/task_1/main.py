from sentence_parsing import sentences, average_length, ngrams
from help_functions import get_text


def main():
    text = get_text()

    try:
        amount_of_sentences = sentences(text)
    except:
        return
    if amount_of_sentences != 0:
        words = average_length(text, amount_of_sentences)
        if len(words) != 0:
            ngrams(text, words)


if __name__ == '__main__':
    main()
