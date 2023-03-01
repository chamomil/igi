import random


def evens():
    list_of_nums = []
    list_of_even = []

    for i in range(10):
        num = random.randint(1, 100)
        list_of_nums.append(num)

        if num % 2 == 0:
            list_of_even.append(num)

    return list_of_even
