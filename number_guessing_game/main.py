# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
import art

print(art.logo)

print("Welcome to the number guessing game!\nI'm thinking about a number between 1 and 100")

number = random.randint(1, 100)
# print(f"Test code: {number}")


level = input("Choose a difficulty. Type 'Easy' or 'Hard': ").lower()

if level == "easy":
    total_attempts = 10
    print(f"You have {total_attempts} attempts to guess the number")
elif level == 'hard':
    total_attempts = 5
    print(f"You have {total_attempts} attempts to guess the number")


def guess():
    return int(input("Make a guess: "))


def compare(guessed_number, random_number, attempts):
    if guessed_number == random_number:
        # print("You've won")
        return "won"
    elif guessed_number != random_number:
        if guessed_number > random_number:
            print("Too high.")
        elif guessed_number < random_number:
            print("Too low.")
        attempts -= 1
        return attempts


game_over = False

while not game_over:
    players_guess = guess()
    total_attempts = compare(players_guess, number, total_attempts)
    if total_attempts == 0:
        print("You've lost")
        print(f"The random number was {number}")
        game_over = True
    elif total_attempts == "won":
        print("You've won")
        game_over = True
    elif total_attempts > 0:
        print(f"You have {total_attempts} attempts remaining to guess the number.")




