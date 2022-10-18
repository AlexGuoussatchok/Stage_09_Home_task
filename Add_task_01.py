# Alex Goussatchok
# QA4822
# Stage 09
# Task: all numbers are even
# v 1.0

def num_def():
    num = int(input("Please input a number: "))
    return num

def list_create(num):  # --> crate iterable object
    ls = []
    while num // 10 > 0:
        ls.append(num % 10)
        num //= 10
    else:
        ls.append(num)
    return ls

def even_check(ls):
    result = "all numbers are even"
    for element in ls:
        if element % 2 != 0:
            result = "not all numbers are even"
    return result


def main():
    num = num_def()
    ls = list_create(num)
    result = even_check(ls)
    msg = f"{result} in number {num}"
    print(msg)

main()