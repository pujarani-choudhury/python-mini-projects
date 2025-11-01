import random

def guess(x):
    random_number = random.randint(1,x)
    attempts = 0  # track number of tries
    guess = None

    print(f"\n🎯 Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and {x}.\n")

    while guess != random_number:
        try:
            guess = int(input("Enter your guess:"))
            attempts += 1

            if guess < random_number:
                print("Sorry, Too low! Try again.\n")

            elif guess > random_number:
                print("Sorry, Too high! Try again. \n")
        except ValueError:
            print("Please enter a valid number. \n")
            continue

    print(f"Yay, Congrats!. You have guessed the number {random_number} correctly in {attempts} tries!\n")

guess(10)