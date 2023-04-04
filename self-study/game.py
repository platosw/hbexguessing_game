"""guessing number game"""
import random
name = input('Howdy, what\'s your name?\n(type in your name) ')
choose_role = input(
    f'{name}, will you a player(type = 1)? or presenter(type = 2)? ').lower()

if choose_role == '1':
    min_range = int(
        input(f'{name}, please set the secret number\'s minimum number '))
    max_range = int(
        input(f'{name}, please set the secret number\'s maximum number '))
    limit_num = int(input(f'{name}, please set the playing limit number '))

    best_score = float('inf')

    while True:
        secret_num = random.randint(min_range, max_range)
        tries = 0
        while True:
            if limit_num == tries:
                print('Too many tries!')
                break

            guess = int(input('Try to guess the secret number. '))
            if guess != secret_num:
                if guess < secret_num:
                    tries += 1
                    print('Your guess is too low, try again.')
                elif guess > secret_num:
                    tries += 1
                    print('Your guess is too high, try again.')
            else:
                tries += 1
                if best_score > tries:
                    best_score = tries
                print(
                    f'Well done, {name}! You found The secret number in {tries} tries!')
                print(f'Your best score is {best_score}.')
                break

        multiple_rounds = input('Do you want to play again? (Y/N)').lower()
        if multiple_rounds == 'n' or multiple_rounds == 'no':
            break
        else:
            continue
elif choose_role == '2':
    com_min_num = int(input('What\'s computer\'s minimum range number? '))
    com_max_num = int(input('What\'s computer\'s maximum range number? '))
    player = int(input('What is your secret number? '))
    com = None
    guesses = 0
    while True:
        com = (com_min_num + com_max_num) // 2
        if com != player:
            print(f'I guess your number is {com}.')
            respond = input(
                'Give a hint to me("too low" or "too high".)').lower()
            if respond == 'too low':
                guesses += 1
                com_min_num = com
            elif respond == 'too high':
                guesses += 1
                com_max_num = com
        else:
            guesses += 1
            print(f'I guess your number is {com}.')
            print(f'I guessed your number in {guesses} guesses.')
            break
else:
    print('wrong syntax')
