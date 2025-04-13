def user_guessing_game():
    print("Welcome to the Number Guessing Game (User Version)!")
    print("Think of a number between 1 and 100, and I'll try to guess it.")

    low = 1
    high = 100
    attempts = 0

    while low <= high:
        attempts += 1

        computer_guess = (low + high) // 2
        print(f"Is your number {computer_guess}?")


        feedback = input("Enter 'h' if it's too high, 'l' if it's too low, or 'c' if it's correct: ").strip().lower()

        if feedback == 'c':
            print(f"Yay! I guessed your number in {attempts} attempts!")
            return
        elif feedback == 'h':
            high = computer_guess - 1
        elif feedback == 'l':
            low = computer_guess + 1
        else:
            print("Invalid input! Please enter 'h', 'l', or 'c'.")

    print("Hmm, something went wrong. Did you think of a number outside the range?")

# Run the game
user_guessing_game()