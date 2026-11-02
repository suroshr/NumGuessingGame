import random

def get_random_number():
    return random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Keep asking until the user types a valid difficulty
while True:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").strip().lower()

    if difficulty == "easy":
        attempts = 10
        break
    elif difficulty == "hard":
        attempts = 5
        break
    else:
        print("Invalid difficulty. Please type 'easy' or 'hard'.")

answer = get_random_number()

while attempts > 0:
    # Use "attempt" when only 1 is left
    if attempts == 1:
        print("You have 1 attempt remaining to guess the number.")
    else:
        print(f"You have {attempts} attempts remaining to guess the number.")

    # Bad input doesn't crash the game or cost an attempt
    try:
        guess = int(input("Make a guess: "))
    except ValueError:
        print("Please enter a whole number.")
        print()
        continue

    # Guesses outside 1-100 don't cost an attempt
    if guess < 1 or guess > 100:
        print("Pick a number between 1 and 100.")
        print()
        continue

    if guess == answer:
        print(f"You got it! The answer was {answer}.")
        break
    elif guess < answer:
        print("Too low.")
        print()
    else:
        print("Too high.")
        print()
    attempts -= 1
else:
    print(f"You've run out of attempts. The answer was {answer}.")
