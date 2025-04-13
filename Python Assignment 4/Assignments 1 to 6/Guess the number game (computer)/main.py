import random

def computer_guessing_game():
    # Computer thinks of a number between 1 and 100
    number_to_guess = random.randint(1, 100)
    max_attempts = 7
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100. You have {max_attempts} attempts to guess it.")

    while attempts < max_attempts:
        try:
            # Get the user's guess
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            # Check if the guess is correct
            if user_guess < number_to_guess:
                print(f"Too low! You have {max_attempts - attempts} guesses left.")
            elif user_guess > number_to_guess:
                print(f"Too high! You have {max_attempts - attempts} guesses left.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts!")
                return

        except ValueError:
            print("Invalid input! Please enter a valid number.")

    # If the user runs out of guesses
    print(f"Sorry, you've run out of guesses. The number was {number_to_guess}.")

# Run the game
computer_guessing_game()