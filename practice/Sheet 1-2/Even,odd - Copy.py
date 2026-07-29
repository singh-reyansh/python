try:
    # Ask the user to enter a number
    num = float(input("Enter a number: "))

    # Check if the number is an integer
    if num.is_integer():
        num = int(num)  # Convert to integer
        # Check if the number is divisible by 2
        if num % 2 == 0:
            print("The number is even.")
        else:
            print("The number is odd.")
    else:
        # If the user entered a decimal
        print("Please enter a whole number (no decimals).")

except ValueError:
    # If the user entered something that is not a number
    print("Invalid input! Please enter a number.")