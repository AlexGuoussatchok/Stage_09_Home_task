# Alex Goussatchok
# QA4822
# Stage 09
# Task: number of even numbers
# v 1.0

def num_def():
    num = int(input("Please input a number: "))
    return num

def list_create(num):  # --> crate iterable object with ints in list
    ls = []
    while num // 10 > 0:
        ls.append(num % 10)
        num //= 10
    else:
        ls.append(num)
    return ls

def even_check(ls):
    count = 0
    for element in ls:
        if element % 2 == 0:
            count += 1
    return count


def main():
    num = num_def()
    ls = list_create(num)
    count = even_check(ls)
    msg = f"even numbers are met in the number {num} {count} times"
    print(msg)

main()