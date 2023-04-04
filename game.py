"""A number-guessing game."""

# Put your code here
import random
name = input("Howdy, what's your name?\n(type in your name): ")
range_min = int(input("Howdy, please add minimum range number:  "))
range_max = int(input("Howdy, please add maximum range number:  "))
limit_num = int(input("Please set the max number of guesses? "))
print(f"{name}, I'm thinking of a number between {range_min} and {range_max}: ")
best_score = float('inf')


def guess_game(min, max):
    guess = None
    secret_num = random.randint(min, max)
    tries = 0
    print(secret_num)
    while guess != secret_num or tries < limit_num:
        guess = int(input('Your guess? '))
        if guess < secret_num:
            tries += 1
            print('Your guess is too low, try again.')
        elif guess > secret_num:
            tries += 1
            print('Your guess is too high, try again.')
    tries += 1
    global best_score
    if tries < best_score:
        best_score = tries
    print(
        f'Well done, {name}! You found my number in {tries} tries! and your best score is {best_score}')


guess_game(range_min, range_max)

play_again = input('Do you want to play again?(Y/N) ').lower()
while play_again != 'n':
    guess_game(range_min, range_max)
    play_again = input('Do you want to play again?(Y/N) ').lower()
