# imports
import random
import time
import sys


# ################# MemoryGame ##################

# a function to begin the countdown to remember the list
def begin():
    for remaining in range(5, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} seconds remaining to begin, ".format(remaining))
        sys.stdout.write("Remember the list before disappear.".format(remaining))
        sys.stdout.flush()
        time.sleep(1)
    return


# a function to show the user the list for duration 0.7
def show(text):
    begin()
    print(f'\r{text}', end='')
    time.sleep(0.7)
    print('\r', end='')


# a function to generate the list
def generate_sequence(level):
    random_list = []
    for i in range(level):
        n = random.randint(1, 101)
        random_list.append(n)
    show(str(random_list))
    return random_list


# a function to the user to guess the list
def get_list_from_user(level):
    random_list_user = []
    for i in range(1, level + 1):
        z = 0
        while not 1 <= z <= 101:
            z = int(input(f"please choose your {i}st number from 1 - 101 ONLY: "))
        random_list_user.append(z)
    print(f'your guess {random_list_user}')
    return random_list_user


# a function to check if the generated list and the user guess list is Equals
def is_list_equal(user_list, pc_list):
    flag = 0
    for i in range(len(user_list)):
        if user_list[i] != pc_list[i]:
            flag = 1
    if flag == 0:
        print("YES YOU WON YOUR MEMORY IS AWESOME ")
        return True
    else:
        print(f"OPS WRONG it was {pc_list} you lost")
        return False
