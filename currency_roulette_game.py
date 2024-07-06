# imports
import random
import requests


# ################# Currency Roulette Game ##################

# a function to get the USD in shekel from real api
def get_money_interval(level):
    url = "https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_T6vzCLn8CRQtp5bgxcj3jH0o05MWxxrrn01VAN7g"
    resp = requests.get(url)
    data = resp.json()
    usd = random.randint(1, 100)
    usd_ils = (data["data"]["ILS"]) * usd
    a = get_guess_from_user(usd, usd_ils, level)
    return a


# a function for the use to guess what is the value of the USD in shekel
def get_guess_from_user(usd, usd_ils, level):
    inp = int(input(f"how much is {usd}$ in shekel(ILS)? "))
    a = compare_results(inp, usd_ils, level)
    return a


# a function the check if the user guessed the right value in shekel
def compare_results(inp, usd_ils, level):
    dev = 10 - level
    diff = abs(usd_ils - inp)
    if diff <= dev:
        print(f"YES its almost {inp}$")
        print(f"ITS {usd_ils}$ Exactly")
        return True
    else:
        print(f"WRONG answer (THE ANSWER IS {usd_ils})")
        return False
