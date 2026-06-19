import random

secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 10

print("Guess a number between 1 and 100")

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too Low!")
    elif guess > secret_number:
        print("Too High!")
    else:
        print("Congratulations! You guessed correctly.")
        break

if guess != secret_number:
    print("Game Over!")
    print("The number was:", secret_number)
