import random
import time  

print("🎲 Welcome to the Dice Rolling Game!")

while True:
    input("Press Enter to roll the die...")
    roll = random.randint(1, 6)
    print(f"You rolled a {roll}!")

    valid_input = False

    while not valid_input:
        again = input("Roll again? (y/n): ").lower()

        if again == 'y':
            valid_input = True
        elif again == 'n':
            print("Thanks for playing!")
            valid_input = True
            break
        else:
            print("❌ Invalid input. Please type 'y' or 'n'.")

    if again == 'n':
        break

print("\n🔒 The game has ended.")


input("The game is over. Type anything to continue if you DARE... ")

print("\n⚠️ WARNING: Unauthorized input detected!")
time.sleep(1)
print("🔍 Scanning system files...")
time.sleep(1)
print("💥 VIRUS FOUND: 'dice_roller_worm.exe'")
time.sleep(1.5)
print("🧨 Initiating self-destruct in:")
for i in range(5, 0, -1):
    print(f"{i}...")
    time.sleep(1)
print("💻 BOOM! Just kidding 😂😂😂.")
time.sleep(1)
print("You're safe. Game really is over now. Goodbye! 👋")

exit()
