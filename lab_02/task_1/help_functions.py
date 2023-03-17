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
