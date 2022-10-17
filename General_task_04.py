# Alex Goussatchok
# QA4822
# Stage 09
# Task: forever dice
# v 1.0

import random


def dice_def():
    dice_1 = random.randrange(1, 7)
    dice_2 = random.randrange(1, 7)
    return dice_1, dice_2


def result_def(dice_1, dice_2):
    result = dice_1 + dice_2
    return result


def user_output(msg):
    print(msg)


def one_more_time():
    val = input("Hit \"Enter\" (you may also input any other key)"
                "or input \"q\" to exit")
    if val == "q":
        exit()
    else:
        main()


def main():
    dice_1, dice_2 = dice_def()
    result = result_def(dice_1, dice_2)
    msg = f"You threw {dice_1} and {dice_2}, that in total gives {result}."
    user_output(msg)
    one_more_time()


main()