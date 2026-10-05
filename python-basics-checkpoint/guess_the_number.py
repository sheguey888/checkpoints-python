import random

secret_number = random.randint(1, 100)
guess = None

print("Welcome to the Guess the Number game!")
print("I'm thinking of a number between 1 and 100. Can you guess what it is?")

while guess != secret_number:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a whole number.")
        continue

    if guess > secret_number:
        print("Your guess is too high. Guess again.")
    elif guess < secret_number:
        print("Your guess is too low. Guess again.")
    else:
        print("Congratulations! You guessed the number correctly!")
