from sentence_parsing import sentences, average_length, ngrams
from help_functions import get_text, max_search


def main():
    text = get_text()

    try:
        amount_of_sentences, amount_of_nondec = sentences(text)
    except:
        print("Text is empty")
        return
    print(f"Amount of sentences: {amount_of_sentences}")
    print(f"Amount of non-declarative sentences: {amount_of_nondec}")

    if amount_of_sentences == 0:
        return
    words, average_sentence, average_word = average_length(text, amount_of_sentences)
    print(f"Average length of the sentence: {average_sentence}")
    print(f"Average length of the words: {average_word}")

    if len(words) != 0:
        ngrams_dict, k = ngrams(words)
        print(f"\n\tTop {k}:\n")
        max_search(ngrams_dict, k)


if __name__ == '__main__':
    main()
