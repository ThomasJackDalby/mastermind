from itertools import permutations
import time

def check(guess, answer):
    incorrect_locations = [i for i in range(len(answer)) if guess[i] != answer[i]]
    num_right_places = len(answer) - len(incorrect_locations)
    num_right_colours = sum(min(sum(1 for i in (guess[i] for i in incorrect_locations) if i == c), sum(1 for i in (answer[i] for i in incorrect_locations) if i == c)) for c in set(answer))
    return num_right_colours, num_right_places

def solve_random_even_even_better(answer, num_colours):
    import random
    random.seed(0)
    number_of_guesses = 0
    options = list(set(permutations(list(range(num_colours)) * len(answer), len(answer))))
    while len(options) > 0:
        value = None
        guess = None
        processed_results = set()
        for potential_guess in options:
            for potential_answer in options:
                result = check(potential_guess, potential_answer)
                if result not in processed_results:
                    processed_results.add(result)
                    amount = sum(1 for option in options if check(potential_guess, option) == result)
                    if value is None or amount < value:
                        value = amount
                        guess = potential_guess

        number_of_guesses += 1
        result = check(guess, answer)
        if result[1] == len(answer):
            return number_of_guesses

        options = [option for option in options if check(guess, option) == result]

NUM_COLOURS = 6
NUM_PEGS = 4

total = 0
runs = 0
for p in set(permutations(list(range(NUM_COLOURS)) * NUM_PEGS, NUM_PEGS)):
    start_time = time.perf_counter()
    guesses = solve_random_even_even_better(p, NUM_COLOURS)
    total += guesses
    runs += 1
    end_time = time.perf_counter()
    duration = end_time - start_time
    print(guesses, duration)

print(f"{total=}")
print(f"{runs=}")
print(f"{total/runs=}")


