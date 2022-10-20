# Alex Goussatchok
# QA4822
# Stage 09
# Task: Palindrome check
# v 1.0


def user_input():
    num = list(input("Please enter a number for palindrome check: "))
    return num


def check_palindrome(num):
    if isinstance(num, bool) or not isinstance(num, list):
        return -1
    else:
        result = "a palindrome"
        num_2 = num
        i = 0
        while i < len(num) - 1:
            if num[i] == num_2[(i + 1) * -1]:
                i += 1
            else:
                result = "not a palindrome"
                break

                print(result)
        return result


def user_output(result):
    msg = f"The number you've entered is {result}"
    return msg
def main():
    num = user_input()
    result = check_palindrome(num)
    msg = user_output(result)
    print(msg)


main()