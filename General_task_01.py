# Alex Goussatchok
# QA4822
# Stage 09
# Task: Compare digits in a number
# V 1.0 (using 'while')

def user_input():
    num = int(input("Please, enter a number: "))
    num *= -1 if num < 0 else 1  # if a number < 0 entered - we still will be able to compare digits
    return num


def digits_compare(num):
    result = "equal"  # value by default
    while num // 10 > 0:
        if num % 10 != num // 10 % 10:  # if compared digits are not equal --> default value will be changed
            result = "not equal"
            break  # --> if one couple of compared digits is not equal - there's no need in further compare
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
        msg = f"Digits in number you've entered ({num}) are {result}"
        print(msg)


main()
