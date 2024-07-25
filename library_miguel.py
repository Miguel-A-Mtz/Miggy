import random

# Miguel Martinez
# Lab 24: using Random


def random_simple():
    this_number = random.randint(1, 10)
    print(f'{this_number}')
    return


def random_choice():
    options = ["one", "two", "three", "four", "five"]
    for each in range(0, 5):
        print(f'Number {each + 1} is {random.choice(options)}')
    return


def random_float():
    this_list = list()
    this_float = 0.0
    while this_float < .5:
        this_float = random.random()
        if this_float < .5:
            this_list.append(this_float)
    return this_list


def random_dice():
    dice_rolls = list()
    user_input = '1'
    while user_input != '0':
        this_roll = random.randint(1, 6)
        dice_rolls.append(this_roll)
        user_input = input(f"This roll was {this_roll} Roll Again? Press 0 to exit")
    print(f'The set of rolls are: {dice_rolls}')
    return


def main():
    print(f'\nWelcome to The Random Lab #24')
    for each in range(0, 20):
        random_simple()
    random_choice()
    print(f'\nThe random number is {random_float()}')
    random_dice()
    return


main()
