def numm_def():
    numm = list(input("Please input a number for a sequence check: "))
    if len(numm) < 2:
        print("Not enough digits for sequence, input a number of at least 2 digits")
    else:
        return numm



numm = numm_def()
print(numm)
# for index in numm:
#     print(f"for index in numm: переменной index поочереди присваивается значение индекса из списка - {numm} - {index}")
#
# for index in range(len(numm)):
#     print(f"for index in range(len(numm)) переменной index присваивается значение индекса - {numm} - {index}")
#
# for index in range(len(numm)):
#     print(f"{index} - {range(len(numm))}")
#
# for index in numm:
#     print(numm[0])
#
# for index in range(len(numm)):
#     print(numm[0])
result = "not ok"

for index in numm:
    s = 0
    print(index[s])
    s += 1
    print(index[s])
    # if index[s] > index[s + 1]:
    #     result = "ok"
    #     print(result)
    # print(index(numm[1]))
    # if index[0] > index[1]:
    #     print(result)

# for index in numm:
#     if index < index