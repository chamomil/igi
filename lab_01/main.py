from hello_print import hello_print
from calculator import calc
from evens import evens


def main():
    hello_print()  # first task

    calc_result = calc(2, 3, 'add')
    print(f"Sum of 2 and 3 is {calc_result}")  # second task

    list_of_numbers = [3, 19, 24, 7, 8, 2, 5]  # third task
    evens_result = evens(list_of_numbers)
    print(f"Evens from the giving list: {evens_result}")


if __name__ == '__main__':
    main()
