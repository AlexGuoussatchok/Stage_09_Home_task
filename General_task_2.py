# Alex Goussatchok
# QA4822
# Stage 09
# Task: No equal digits in a number
# (using 'while'). There're 2 ways to read the task: 1. (v. 1.0) the same as task 1 (the programm tells Yes or no
# 2. (v 1.2) if the number includes any equal digits

# V 1.0

# def user_input():
#     num = int(input("Please, enter a number: "))
#     num *= -1 if num < 0 else 1  # if a number < 0 entered - we still will be able to compare digits
#     return num
#
#
# def digits_compare(num):
#     result = "Yes"  # value by default
#     while num // 10 > 0:
#         if num % 10 == num // 10 % 10:  # if compared digits are not equal --> default value will be changed
#             result = "No"
#             break
#         else:
#             num //= 10
#     return result
#
#
# def main():
#     num = user_input()
#     if 0 >= num // 10 < 1:
#         print(f"The number you've entered ({num}) consists of 1 digit, so there is nothing to compare. "
#               f"Please enter a number of 2 digits minimum.")  # if a number with only one digit is entered -
#         # there's nothing to compare
#     else:
#         result = digits_compare(num)
#         msg = f"Are all number digits in (\"{num}\") are equal? - {result}"
#         print(msg)
#
#
# main()

# -------------------------------------------------------------------------------------------------------------------

# v 2.0

def user_input():
    num = int(input("Please, enter a number: "))
    num *= -1 if num < 0 else 1  # if a number < 0 entered - we still will be able to compare digits
    return num


def list_1_creat(num):  # --> crate iterable object
    ls = []
    while num // 10 > 0:
        ls.append(num % 10)
        num //= 10
    else:
        ls.append(num)
    return ls


def find_equals(ls, equal_values):
    answer = False
    while len(ls) > 0:
        value = ls.pop(0)  # -->  we pick up a digit & compare it to other digits in the list
        if value in ls:
            if value not in equal_values:
                equal_values.append(value)  # --> we add equal values to the list
            answer = True

    return answer, equal_values


def main():
    num = user_input()
    if 0 >= num // 10 < 1:
        print(f"The number you've entered ({num}) consists of 1 digit, so there is nothing to compare. "
              f"Please enter a number of 2 digits minimum.")  # if a number with only one digit is entered -
        # there's nothing to compare
    else:
        ls = list_1_creat(num)
        equal_values = []  # --> we create a list of equal values
        answer, equal_values = find_equals(ls, equal_values)
        if answer == False:
            msg = f"There are NO equal digits in number \"{num}\""
        else:
            msg = f"There are equal digits in number \"{num}\": digits that have equals are: {equal_values}"
        print(msg)


main()
