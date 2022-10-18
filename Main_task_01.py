def num_def():
    num = int(input("Please input a number for a sequence check: "))
    if num < 10:
        print("Not enough digits for sequence, input a number of at least 2 digits")
    else:
        return num

def list_1_creat(num):  # --> crate iterable object
    ls = []
    while num > 10:
        ls.append(num % 10)
        num = num // 10
    else:
        ls.append(num)
    return ls

def main():
    num = num_def()
    ls = list_1_creat(num)
    print(ls)
    i = len(ls)
    print(i)
    if ls[i - 1] > ls[i-1 - 1]:
        print(ls[i - 1], ls[i - 1- 1])
        while i >= 0:
            while ls[i - 1] > ls[i - 1 - 1]:
                result = "ok"
                i -= 1
                print(i)
                print(result)
    elif ls[i - 1] < ls[i-1 - 1]:
        print(ls[i - 1], ls[i - 1- 1])
        while i >= 0:
            while ls[i - 1] < ls[i - 1 - 1]:
                result = "ok"
                i -= 1
                print(i)
                print(result)
    else:
        result = "not ok"
        print(result)


main()
