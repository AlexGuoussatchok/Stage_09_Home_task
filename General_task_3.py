# Alex Goussatchok
# QA4822
# Stage 09
# Task: count a number
# v 1.0

def user_input():  # --> a number where we will look for a value
    num = int(input("Please, enter a number: "))
    return num


def user_val_input():  # --> value we will look for in entered number
    val = int(input("Please, enter a value: "))
    if val > 9:
        print(f"Oops... this version looks for one digit values only")
    else:
        return val


def list_create(num):  # --> crate iterable object
    ls = []
    while num // 10 > 0:
        ls.append(num % 10)
        num //= 10
    else:
        ls.append(num)
    return ls


def find_a_digit(val, ls):
    count = 0
    for item in ls:
        if item == val:
            count += 1
    return count


def main():
    num = user_input()
    val = user_val_input()
    ls = list_create(num)
    count = find_a_digit(val, ls)
    msg = f"{val} is met in the entered number (\"{num}\") {count} times"
    print(msg)


main()
