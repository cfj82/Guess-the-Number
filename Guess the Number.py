#  Guess the Number
#  Program generate random number and user will guess. After each guess a hint will be given

#  tofix combine evaluate functions into a single

import random

def set_up():
    ran_num = random.randint(0, 10)  # random number generated
    print('random number is ' + str(ran_num))  # show random number as a check
    user = input('Please guess a number from 0 to 10: ')  # user input guess
    check(user, ran_num)  # def check()

def check_win(ran_num, user):
    count = 1  # count amount of guesses start at 1
    while True:
        if evaluate_high(ran_num, int(user)):
            print("Guess is too high, please guess again.")
            # num_check(user)  # check that input is a number not letter
            user = input('Guess a number from 0 to 10:')
            count = count + 1
            print('You have made ' + str(count) + ' guesses.')

        elif evaluate_low(ran_num, int(user)):
            print("Guess is too low, please guess again.")
            # num_check(user)  # check that input is a number not letter
            user = input('Guess a number from 0 to 10:')
            count = count + 1
            print('You have made ' + str(count) + ' guesses.')

        elif int(user) == ran_num:  # user guessed correct number
            print('Good guess! The number is ' + str(ran_num))
            print('It took you ' + str(count) + ' guesses')
            break


def evaluate_high(ran_num, user):
    if (int(user) > ran_num) and (user != ran_num):
        print(ran_num)
        return True


def evaluate_low(ran_num, user):  # i should be able to place this in other def evaluate_high
    if (int(user) < ran_num) and (user != ran_num):
        print(ran_num)
        return True

def check(user, ran_num):
    while True:  # check that input is a number not letter
        if user.isdigit():
            return check_win(ran_num, user)  # user input guess
        else:
            user = input('You entered a letter, please guess again ')  # user input guess



print(set_up())  # run program
