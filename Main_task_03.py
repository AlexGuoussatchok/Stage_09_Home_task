# Alex Goussatchok
# QA4822
# Stage 09
# Task: Bank deposit
# v 1.0

INITIAL_DEPOSIT = 1_000  # --> initial deposit


def user_input():
    percents = int(input("Enter the capitalization percent: "))
    return percents


def calculate_month_growth(percents):  # --> deposit growth per month
    if isinstance(percents, bool) or not isinstance(percents, int) or not (1 <= percents <= 25):
        return -1

    else:
        deposit = INITIAL_DEPOSIT + INITIAL_DEPOSIT * (percents / 100)
        return deposit


def calculate_time_required(deposit, percents):
    month = 1
    while deposit < 2_000:
        deposit += + deposit * (percents / 100)
        month += 1
    return month


def calculate_summ(deposit, percents, month):
    while month > 1:
        summ = deposit + deposit * (percents / 100)
        deposit = summ
        month -= 1
    return round(summ, 2)


def user_output(percents, month, summ):
    msg = f"If your initial deposit is {INITIAL_DEPOSIT} BYN, and the capitalisation percent is {percents}% " \
          f"you will need at least {month} month to get 2000 BYN. The sum you will get after {month} month will be" \
          f" {summ} BYN"
    return msg


def main():
    percents = user_input()
    deposit = calculate_month_growth(percents)
    month = calculate_time_required(deposit, percents)
    summ = calculate_summ(deposit, percents, month)
    msg = user_output(percents, month, summ)
    print(msg)


main()
