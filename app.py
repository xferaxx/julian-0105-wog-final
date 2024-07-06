# imports
from guess_game import generate_number, get_guess_from_user, compare_results
from currency_roulette_game import get_money_interval
from memory_game import generate_sequence, get_list_from_user, is_list_equal
from utils import screen_cleaner
from score import add_score, write_score


# a function to take username and Welcome message
def welcome():
    username = input("Enter username: ")
    print(f"hi {username} and welcome to the World of Games: The Epic Journey\n")


# a function to start the game and choose what game and what level
def start_play():
    num = 0
    while num != 1 or num != 2 or num != 3:
        print("Please choose a game to play:")
        print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.")
        print("2. Guess Game - guess a number and see if you chose like the computer.")
        print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n")
        num = input("choose a game number between 1-3\n")
        if num == str(1):
            title = "Memory Game"
            n = hello_level(title)
            game, level = int(num), n
            check_game(game, level)
            return
        elif num == str(2):
            title = "Guess Game"
            n = hello_level(title)
            game, level = int(num), n
            check_game(game, level)
            return
        elif num == str(3):
            title = "Currency Roulette Game"
            n = hello_level(title)
            game, level = int(num), n
            check_game(game, level)
            return


# a function I used to reduce the code to get the welcome of the chosen game and level
def hello_level(title):
    print(f"Welcome to {title}")
    l_d = level_difficulty()
    print(f"Welcome to level {l_d}")
    return l_d


# a function to choose the level
def level_difficulty():
    num = 0
    while not 1 <= num <= 5:
        num = int(input("please choose level difficulty between  1 - 5\n"))
        if num == 1 or num == 2 or num == 3 or num == 4 or num == 5:
            return int(num)


def check_game(game, level):
    if game == 1:
        play1(level)
    elif game == 2:
        play2(level)
    elif game == 3:
        play3(level)


def play1(level):
    pc_list = generate_sequence(level)
    user_list = get_list_from_user(level)
    a = is_list_equal(user_list, pc_list)
    if a:
        add_score(level)
    else:
        write_score(0)
    screen_cleaner()


# a function to start the second game ( guess game).
def play2(level):
    gn = generate_number(level)
    ug = get_guess_from_user(level)
    a = compare_results(gn, ug)
    if a:
        add_score(level)
    else:
        write_score(0)
    screen_cleaner()


# a function to start the third game ( currency roulette game ).
def play3(level):
    a = get_money_interval(level)
    if a:
        add_score(level)
    else:
        write_score(0)
    screen_cleaner()
