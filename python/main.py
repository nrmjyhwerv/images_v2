import os
import time
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Clear console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_console()

# Print message in color
print(Fore.CYAN + Style.BRIGHT + "Thanks for using Cryptalis Panel")

