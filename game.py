"""A number-guessing game."""

# Put your code here
import random
name = input("Howdy, what's your name?\n(type in your name)")
print(f"{name}, I'm thinking of a number between 1 and 100")
secret_num = random.randint(1, 100)
guess = None
tries = 0

while guess != secret_num:
    guess = int(input("Your guess?"))
    if guess < secret_num:
        print("Your guess is too low, try again.")
        tries += 1
    else:
        print("Your guess is too high, try again.")
        tries += 1

print(f'Well done, {name}! You found my number in {tries} tries!')
