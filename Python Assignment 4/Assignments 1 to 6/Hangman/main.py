import random
import sys
WORDS = {
    "easy": ["moon", "book", "fish", "cake", "rain"],
    "medium": ["guitar", "flower", "planet", "coffee", "rocket"],
    "hard": ["adventure", "universe", "algorithm", "chocolate", "astronomy"]
}

HINTS = {
    "easy": ["It's in the sky", "You read it", "Swims in water", "Sweet dessert", "Falls from clouds"],
    "medium": ["Musical instrument", "Blooms in spring", "Orbits the sun", "Morning drink", "Goes to space"],
    "hard": ["Exciting journey", "Everything that exists", "Coding logic", "Sweet treat", "Study of stars"]
}

def choose_word(difficulty):
    index = random.randint(0, 4)
    return WORDS[difficulty][index], HINTS[difficulty][index]

def display_word(word, guessed):
    return " ".join([letter if letter in guessed else "_" for letter in word])

def play_round(round_num, difficulty):
    word, hint = choose_word(difficulty)
    guessed = set()
    attempts = 6
    hint_used = False

    print(f"\n--- Round {round_num} ({difficulty.capitalize()}) ---")
    print(f"Word: {display_word(word, guessed)}")
    print(f"Attempts left: {attempts} | Type 'hint' for a clue")

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if guess == "hint":
            if not hint_used:
                print(f"\n💡 **Clue**: {hint}")  # Clue dikhao
                hint_letter = random.choice([c for c in word if c not in guessed])
                guessed.add(hint_letter)
                print(f"Revealed letter: '{hint_letter}'\n")
                hint_used = True
            else:
                print("You already used your hint!")
        elif guess in guessed:
            print("Already guessed!")
        elif guess in word:
            guessed.add(guess)
            print("Correct! ✅")
        else:
            attempts -= 1
            print(f"Wrong! ❌ Attempts left: {attempts}")

        print(display_word(word, guessed))

        if all(c in guessed for c in word):
            print("You won this round! 🎉")
            return 1

    print(f"You lost this round. 😞 The word was: {word}")
    return -1

def main_game():
    print("🔥 Welcome to Ultimate Hangman! 🔥")
    difficulty = input("Choose difficulty (easy/medium/hard): ").lower()
    while difficulty not in ["easy", "medium", "hard"]:
        print("Invalid! Choose easy/medium/hard.")
        difficulty = input("Choose difficulty: ").lower()

    total_score = 0
    for round_num in range(1, 6):
        round_result = play_round(round_num, difficulty)
        total_score += round_result
        print(f"Current Score: {total_score}\n")

    print("--- Game Over ---")
    if total_score >= 3:
        print(f"🏆 Champion! Final Score: {total_score}")
    elif total_score >= 0:
        print(f"😊 Good Try! Final Score: {total_score}")
    else:
        print(f"💪 Keep Practicing! Final Score: {total_score}")

 # Play Again Option
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again not in ["yes", "y"]:
            print("Thanks for playing! 👋")
            sys.exit()  # Exit the program gracefully
        else:
            print("Restarting the game...\n")
# Start the game
main_game()