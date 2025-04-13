import random
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def print_colored(text, color):
    """Prints text in the specified color."""
    print(color + text + Style.RESET_ALL)

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0
    rounds = 0
    max_rounds = 5  # Set the number of rounds

    print_colored("Welcome to Rock, Paper, Scissors!", Fore.CYAN)
    print_colored(f"You will play {max_rounds} rounds against the computer. Let's see who wins!", Fore.LIGHTYELLOW_EX)

    while rounds < max_rounds:
        rounds += 1
        print_colored(f"\n--- Round {rounds} ---", Fore.LIGHTMAGENTA_EX)

        # User's choice
        user_choice = input("Enter your choice (rock, paper, scissors) or 'q' to quit: ").strip().lower()
        if user_choice == 'q':
            print_colored("Thanks for playing! Exiting the game...", Fore.LIGHTMAGENTA_EX)
            break

        if user_choice not in choices:
            print_colored("Invalid choice! Please enter 'rock', 'paper', or 'scissors'.", Fore.RED)
            rounds -= 1  # Don't count invalid rounds
            continue

        # Computer's choice
        computer_choice = random.choice(choices)
        print_colored(f"\nYou chose: {user_choice}", Fore.LIGHTBLUE_EX)
        print_colored(f"Computer chose: {computer_choice}", Fore.LIGHTBLUE_EX)

        # Determine the winner
        if user_choice == computer_choice:
            print_colored("It's a tie!", Fore.YELLOW)
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print_colored("You win this round!", Fore.GREEN)
            user_score += 1
        else:
            print_colored("Computer wins this round!", Fore.RED)
            computer_score += 1

        # Display scores
        print_colored(f"Scores -> You: {user_score}  |  Computer: {computer_score}", Fore.LIGHTMAGENTA_EX)

    # Final result after all rounds
    if rounds == max_rounds:
        print_colored("\n--- Game Over ---", Fore.LIGHTMAGENTA_EX)
        if user_score > computer_score:
            print_colored("Congratulations! You won the game!", Fore.GREEN)
        elif user_score < computer_score:
            print_colored("Oops! Computer won the game. Better luck next time!", Fore.RED)
        else:
            print_colored("It's a tie! No one wins.", Fore.YELLOW)
        print_colored(f"Final Scores -> You: {user_score}  |  Computer: {computer_score}", Fore.LIGHTGREEN_EX)

    # Ask if the user wants to play again
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        rock_paper_scissors()
    else:
        print_colored("Thanks for playing! Goodbye!", Fore.LIGHTMAGENTA_EX)

# Run the game
rock_paper_scissors()