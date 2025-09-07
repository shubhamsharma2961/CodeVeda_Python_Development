import random

number = random.randint(1, 100)

print("Welcome to Number Guessing Game!")
print("I have picked a number between 1 and 100.")
print("You have 7 chances to guess it correctly.")

max_attempts = 7
attempts = 0

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == number:
        print("Congratulations! You guessed it right in", attempts, "tries.")
        break
    elif guess < number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

if attempts == max_attempts and guess != number:
    print("Sorry, you've used all your chances. The number was:", number)
