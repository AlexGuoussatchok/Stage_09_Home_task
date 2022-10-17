# Alex Goussatchok
# QA4822
# Stage 09
# Task: Compare digits in a number
# V 1.0 (using 'while') May be not the exact solution to a task, cause probably the task was to make the programme
# tell "Yes" or "No" to the question if all of the digits are equal

# def user_input():
#     num = int(input("Please, enter a number: "))
#     num *= -1 if num < 0 else 1  # if a number < 0 entered - we still will be able to compare digits
#     return num
#
#
# def digits_compare(num):
#     result = "equal"  # value by default
#     while num // 10 > 0:
#         if num % 10 != num // 10 % 10:  # if compared digits are not equal --> default value will be changed
#             result = "not equal"
#             break  # --> if one couple of compared digits is not equal - there's no need in further comparison
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
#         msg = f"Digits in number you've entered ({num}) are {result}"
#         print(msg)
#
#
# main()

#--------------------------------------------------------------------------------------------------------------------
# v 1.1 - If all of number digits are equal - the programme will return "Yes", if not equal - will return "No"

def user_input():
    num = int(input("Please, enter a number: "))
    num *= -1 if num < 0 else 1  # if a number < 0 entered - we still will be able to compare digits
    return num


def digits_compare(num):
    result = "Yes"  # value by default
    while num // 10 > 0:
        if num % 10 != num // 10 % 10:  # if compared digits are not equal --> default value will be changed
            result = "No"
            break  # --> if one couple of compared digits is not equal - there's no need in further comparison
        else:
            num //= 10
    return result


def main():
    num = user_input()
    if 0 >= num // 10 < 1:
        print(f"The number you've entered ({num}) consists of 1 digit, so there is nothing to compare. "
              f"Please enter a number of 2 digits minimum.")  # if a number with only one digit is entered -
        # there's nothing to compare
    else:
        result = digits_compare(num)
        msg = f"Are all number digits in (\"{num}\") are equal? - {result}"
        print(msg)


main()