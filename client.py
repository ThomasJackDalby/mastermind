import requests
import random
from itertools import permutations

USER_NAME = "tom"
SECRET = "0cd5ace5-f198-451f-9734-5f40d719f475"
API_URL = "https://fnc-mastermind.azurewebsites.net/"
LETTERS = "abcdef"

def check(guess, answer):
    incorrect_locations = [i for i in range(len(answer)) if guess[i] != answer[i]]
    return sum(min(sum(1 for i in [guess[i] for i in incorrect_locations] if i == c), sum(1 for i in [answer[i] for i in incorrect_locations] if i == c))for c in set(answer)), len(answer) - len(incorrect_locations)

def api_check(game_id, guess):
    url = f"{API_URL}/guess/{game_id}/"+"/".join((LETTERS[i] for i in guess))
    print(url)
    res = requests.get(url).json()
    return res["num_right_colour"], res["num_right_place"]

def solve_random_even_even_better(answer, num_colours, num_pegs):
    random.seed(0)
    number_of_guesses = 0
    options = list(set(permutations(list(range(num_colours)) * num_pegs, num_pegs)))
    while len(options) > 0:
        number_of_guesses += 1

        # value = None
        # guess = None
        # processed_results = set()
        # for potential_guess in options:
        #     for potential_answer in options:
        #         result = check(potential_guess, potential_answer)
        #         if result not in processed_results:
        #             processed_results.add(result)
        #             amount = sum(1 for o in options if check(potential_guess, o) == result)
        #             if value is None or amount < value:
        #                 value = amount
        #                 guess = potential_guess

        guess = random.choice(options)

        result = api_check(game_id, guess)
        if result[1] == num_pegs:
            return number_of_guesses

        options = [option for option in options if check(guess, option) == result]

if __name__ == "__main__":
    import sys
    user_name = sys.argv[1]
    requests.get(f"{API_URL}/newuser/{user_name}/{SECRET}")

    while True:
        game_id = requests.get(f"{API_URL}/newgame/{user_name}/{SECRET}").json()["game"]
        print(f"Solving: {game_id}")
        number_of_guesses = solve_random_even_even_better(game_id, 6, 4)
        print(f"Solved in {number_of_guesses}")