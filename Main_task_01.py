# Alex Goussatchok
# QA4822
# Stage 09
# Task: Palindrome check
# v 1.0

def user_input():
    number = int(input("Please enter a number: "))
    return number


def check_ascending_order(number):
    if isinstance(number, bool) or not isinstance(number, int):
        return -1

    while number > 10:
        if number % 10 <= number // 10 % 10:
            return False
        number //= 10

    return True


def check_descending_order(number):
    if isinstance(number, bool) or not isinstance(number, int):
        return -1

    while number > 10:
        if number % 10 >= number // 10 % 10:
            return False
        number //= 10

    return True


def user_output(result, number):
    msg = f"The number you've entered ({number}) is {result} sequence"
    return msg


def main():
    number = user_input()

    if number < 10:
        print(f"The number you've entered ({number}) is too short for a sequence. "
        f"Please enter a number of 2 digits minimum")

    else:
        if number % 10 > number // 10 % 10:
            if check_ascending_order(number) == True:
                result = "in ascendant"
            else:
                result = "not a"


        elif number % 10 < number // 10 % 10:
            if check_descending_order(number) == True:
                result = "in descendant"
            else:
                result = "not a"

        msg = user_output(result, number)
        print(msg)


main()
