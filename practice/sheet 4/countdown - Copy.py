def countdown(num):
    while num >= 0:
        print(num)
        num -= 1

number = int(input("Enter a number to start the countdown: "))
countdown(number)