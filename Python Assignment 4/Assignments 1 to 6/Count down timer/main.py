import time
import sys
from colorama import Fore, Style, init
init()
def countdown_timer(seconds):
    try:
        while seconds:
            mins, secs = divmod(seconds, 60)
            timer = f"{mins:02}:{secs:02}"
            progress = (1 - (seconds / total_time)) * 20
            progress_bar = "[" + "=" * int(progress) + " " * (20 - int(progress)) + "]"
            print(Fore.GREEN + f"Time Left: {timer} " + Fore.YELLOW + progress_bar + Style.RESET_ALL, end="\r")
            time.sleep(1)
            seconds -= 1
            if seconds == total_time // 2:
                print(Fore.CYAN + "\nHalfway there! Keep going! 💪" + Style.RESET_ALL)
            elif seconds == 10:
                print(Fore.MAGENTA + "\nAlmost there! Just 10 seconds left! 🚀" + Style.RESET_ALL)

        print(Fore.RED + "\nTime's up! 🎉" + Style.RESET_ALL)
    except KeyboardInterrupt:
        print(Fore.RED + "\nCountdown interrupted by user. Exiting..." + Style.RESET_ALL)

if __name__ == "__main__":
    try:
        user_input = input("Enter the number of seconds for the countdown: ")
        total_time = int(user_input)
        print(Fore.BLUE + f"Starting countdown for {total_time} seconds..." + Style.RESET_ALL)
        countdown_timer(total_time)
    except ValueError:
        print(Fore.RED + "Invalid input! Please enter a valid number." + Style.RESET_ALL)