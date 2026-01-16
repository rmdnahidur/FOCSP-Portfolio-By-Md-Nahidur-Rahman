# Task 2: Password Security Verification
# Author: Md Nahidur
# This program asks the user to enter a password and verifies it
# by requesting three letters from random positions for security.

import sys
import random

# ANSI color codes for terminal
COLOR_RESET = "\033[0m"
COLOR_RED = "\033[91m"
COLOR_GREEN = "\033[92m"
COLOR_YELLOW = "\033[93m"
COLOR_CYAN = "\033[96m"
COLOR_MAGENTA = "\033[95m"

# -------------------------------------------------
# Function to read a password from a file
# -------------------------------------------------
def read_password_from_file(filename):
    try:
        with open(filename, 'r') as file:
            password = file.readline().strip()
            return password
    except FileNotFoundError:
        print(f"{COLOR_YELLOW}File '{filename}' not found. Switching to manual input.{COLOR_RESET}")
        return None

# -------------------------------------------------
# Function to prompt the user to enter a password
# -------------------------------------------------
def get_password():
    password = input(f"{COLOR_CYAN}Enter your password: {COLOR_RESET}").strip()
    return password

# -------------------------------------------------
# Function to check if password meets minimum length
# -------------------------------------------------
def check_length(password):
    if len(password) < 9:
        print(f"{COLOR_RED}\nPassword too short! Must be at least 9 characters.{COLOR_RESET}")
        return False
    return True

# -------------------------------------------------
# Function to perform random position security check
# -------------------------------------------------
def security_check(password):
    length = len(password)
    # Pick 3 random positions (1-based indexing)
    positions = random.sample(range(1, length + 1), 3)
    
    for pos in positions:
        letter = input(f"{COLOR_MAGENTA}Enter the character at position {pos}: {COLOR_RESET}").strip()
        # Validate input
        if len(letter) != 1:
            print(f"{COLOR_RED}Invalid input! Enter only one character.{COLOR_RESET}")
            return False
        if letter == password[pos - 1]:
            print(f"{COLOR_GREEN}Correct!{COLOR_RESET}")
        else:
            print(f"{COLOR_RED}Security check failed.{COLOR_RESET}")
            return False
    return True

# -------------------------------------------------
# Main program
# -------------------------------------------------
def main():
    print(f"{COLOR_CYAN}Password Security Verification{COLOR_RESET}")
    print(f"{COLOR_CYAN}=============================={COLOR_RESET}\n")

    # Check if a password file is provided via command-line
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        password = read_password_from_file(filename)
        if not password:
            password = get_password()
    else:
        password = get_password()

    # Check password length
    if not check_length(password):
        return

    # Perform security check
    if security_check(password):
        print(f"\n{COLOR_GREEN}Security check passed! ✅{COLOR_RESET}")

# -------------------------------------------------
# Run the program
# -------------------------------------------------
if __name__ == "__main__":
    main()
