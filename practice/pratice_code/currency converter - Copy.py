print("Currency converter 💵")

# Conversion rates
GBP = 0.74
INR = 85.86
Euro = 0.86

# Function to handle invalid choices
def handle_invalid_choice():
    print("❌ Invalid choice! Please pick 1, 2, 3, or 4 only.")

while True:
    print("\nCurrency Options:")
    print("Press 1 for GBP")
    print("Press 2 for INR")
    print("Press 3 for Euro")
    print("Press 4 to end the program")

    try:
        choice = int(input("Enter your choice = "))
    except ValueError:
        handle_invalid_choice()
        continue

    if choice == 4:
        print("👋 Exiting the program. Goodbye!")
        break
    elif choice not in [1, 2, 3]:
        handle_invalid_choice()
        continue

    try:
        USD = float(input("Enter USD amount = "))
    except ValueError:
        print("❌ Please enter a valid number for USD amount.")
        continue

    if choice == 1:
        USD_GBP = USD * GBP
        print(f"{USD:.2f} USD = {USD_GBP:.2f} GBP")
    elif choice == 2:
        USD_INR = USD * INR
        print(f"{USD:.2f} USD = {USD_INR:.2f} INR")
    elif choice == 3:
        USD_Euro = USD * Euro
        print(f"{USD:.2f} USD = {USD_Euro:.2f} Euro")
