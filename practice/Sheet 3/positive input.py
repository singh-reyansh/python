num = int(input("Enter a positive number: "))

while num <= 0:
    print("That's not positive. Try again.")
    num = int(input("Enter a positive number: "))

print("You entered:", num)
