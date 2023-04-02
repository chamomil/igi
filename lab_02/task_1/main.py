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

    if len(words) == 0:
        return

    try:
        n = int(input("Enter n: "))
    except:
        n = 4
    if n <= 0:
        n = 4
    if n > len(words):
        print("n is bigger that the amount of words, number of words will be used instead of it.")
        n = len(words)

    ngrams_dict = ngrams(words, n)

    try:
        k = int(input("Enter k: "))
    except:
        k = 10
    if k <= 0:
        k = 10
    if k > len(ngrams_dict):
        print("k is bigger that the amount of ngrams, number of ngrams will be used instead of it.")
        k = len(ngrams_dict)

    print(f"\n\tTop {k}:\n")
    max_search(ngrams_dict, k)


if __name__ == '__main__':
    main()
