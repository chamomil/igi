from re import findall


def get_text() -> str:
    # text = input("Enter text: ")

    file = open('text.txt', 'r')
    text = file.read()
    print(f"\tText from file\n{text}")
    file.close()
    return text


def name_search(text: str):
    names_list = findall(r'\b\w[.]\s\b\w[.]\s', text)
    return len(names_list) * 2


def lowercase_search(sentence_list, amount_of_sentence, amount_of_nondec):
    for sentence in sentence_list:  # checking if next letter is upper
        if sentence[-1].islower():
            amount_of_sentence -= 1
            if nondec_search(sentence):
                amount_of_nondec -= 1
    return amount_of_sentence, amount_of_nondec


def quotes_search(quotes_list, amount_of_sentence, amount_of_nondec):
    for quotes in quotes_list:
        if quotes[-1].isupper():
            amount_of_sentence += 1
            if nondec_search(quotes):
                amount_of_nondec -= 1
    return amount_of_sentence, amount_of_nondec


def nondec_search(sentence):
    if sentence[0] == '?' or sentence[0] == '!':
        return True
    return False


def count_nondec(sentence_list):
    num = 0
    for sentence in sentence_list:
        if nondec_search(sentence):
            num += 1
    return num


def check_numbers(sentence_list):
    for sentence in sentence_list:
        if sentence.isdigit():
            sentence_list.remove(sentence)
    return sentence_list


def max_search(ngrams: dict, k: int):
    _k = k + 1
    print(f"\n\tTop {k}:\n")
    while k > 0:
        max_k = [key for key, value in ngrams.items() if value == max(ngrams.values())]
        for element in max_k:
            if k > 0 :
                print(f"\t{_k - k}.{element} - {ngrams[element]}")
                k -= 1
                ngrams.pop(element)
            else:
                return
