import random
import string

try:
    import pyperclip
    clipboard_available = True
except ImportError:
    clipboard_available = False

def generate_password(length, use_letters, use_numbers, use_symbols):
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def handle_invalid_yes_no():
    print("❌ Invalid input! Please type 'yes' or 'no'.")

def yes_or_no(prompt):
    while True:
        answer = input(prompt + " (yes/no): ").strip().lower()
        if answer in ["yes", "y"]:
            return True
        elif answer in ["no", "n"]:
            return False
        else:
            handle_invalid_yes_no()

# Main loop
while True:
    user_input = input("🔐 Enter password length (number only, minimum 4): ")
    
    if not user_input.isdigit():
        print("❌ Invalid input! Please enter a number.")
        continue

    length = int(user_input)
    if length < 4:
        print("❌ Password must be at least 4 characters long.")
        continue

    # Ask what to include, repeat until at least one is yes
    while True:
        include_letters = yes_or_no("Include letters?")
        include_numbers = yes_or_no("Include numbers?")
        include_symbols = yes_or_no("Include symbols?")

        if include_letters or include_numbers or include_symbols:
            break  # valid selection
        else:
            print("❌ You must say 'yes' to at least one character type (letters, numbers, or symbols).")

    password = generate_password(length, include_letters, include_numbers, include_symbols)
    print("✅ Your Generated Password:", password)

    # Ask to copy
    if clipboard_available:
        if yes_or_no("📋 Do you want to copy this password to the clipboard?"):
            pyperclip.copy(password)
            print("✅ Password copied to clipboard!")
    else:
        print("ℹ️ Clipboard copy is not available because 'pyperclip' is not installed.")
        print("👉 To enable it, install pyperclip using: pip install pyperclip")
    
    break  # Exit after generating one password
