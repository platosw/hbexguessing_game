"""A number-guessing game."""

# Put your code here
import random
name = input("Howdy, what's your name?\n(type in your name): ")
range_min = int(input("Howdy, please add minimum range number:  "))
range_max = int(input("Howdy, please add maximum range number:  "))
limit_num = int(input("Please set the max number of guesses? ")) - 1
print(f"{name}, I'm thinking of a number between {range_min} and {range_max}: ")
best_score = float('inf')


def guess_game(best, limit, min, max):
    guess = None
    secret_num = random.randint(min, max)
    tries = 0
    while guess != secret_num:
        guess = int(input("Your guess?"))
        if limit != tries:
            if guess < secret_num:
                print("Your guess is too low, try again.")
                tries += 1
            elif guess > secret_num:
                print("Your guess is too high, try again.")
                tries += 1
            else:
                tries += 1
                if tries < best:
                    best = tries
                print(
                    f'Well done, {name}! You found my number in {tries} tries! and your best score is {best}!')
                play_multi = input(
                    f'Play again? or end the game?(Y/N)').lower()
                if play_multi == 'y':
                    guess_game(best, limit, min, max)
                else:
                    print('Goodbye!!')
                    break
        else:
            print('too many tries!')
            play_multi = input(
                f'Play again? or end the game?(Y/N)').lower()
            if play_multi == 'y':
                guess_game(best, limit, min, max)
            else:
                print('Goodbye!!')
                break


guess_game(best_score, limit_num, range_min, range_max)
