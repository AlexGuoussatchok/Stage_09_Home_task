# Alex Goussatchok
# QA4822
# Stage 09
# Task: max number
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

def get_max_number(ls):
    max = ls[0]
    for element in ls:
        if element > max:
            max = element
    return max


def main():
    num = num_def()
    ls = list_create(num)
    max = get_max_number(ls)
    msg = f"{max} is the maximum digit in number {num}"
    print(msg)

main()
