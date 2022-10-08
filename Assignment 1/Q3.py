# Name: Ahmad Alqattan      ID:2192131011

import random

def keep_guessing():
    number = random.randint(1,11)
    guess = int(input("Enter your guess: "))
    score = 10
    while guess != number:
        if guess < number:
            print("Too low :(")
        if guess > number:
            print("Too high :<")
        guess = int(input("Enter your guess: "))
        score -= 2
    else:
        print(f"Hooray, you guessed the number!\nYour score is: {score}")

keep_guessing()


# Enter your guess: 1
# Too low :(
# Enter your guess: 1
# Too low :(
# Enter your guess: 1
# Too low :(
# Enter your guess: 1
# Too low :(
# Enter your guess: 1
# Too low :(
# Enter your guess: 1
# Too low :(
# Enter your guess: 1
# Too low :(
# Enter your guess: 1
# Too low :(
# Enter your guess: 1
# Too low :(
# Enter your guess: 2
# Too low :(
# Enter your guess: 3
# Too low :(
# Enter your guess: 4
# Too low :(
# Enter your guess: 5
# Too low :(
# Enter your guess: 6
# Hooray, you guessed the number!
# Your score is: -16