ADD = "add"
SUB = "sub"
MULT = "mult"
DIV = "div"
def calc(first_num, second_num, operation):
    if (operation == ADD):
        return first_num + second_num
    elif (operation == SUB):
        return first_num - second_num
    elif (operation == MULT):
        return first_num * second_num
    elif (operation == DIV):
        return first_num / second_num