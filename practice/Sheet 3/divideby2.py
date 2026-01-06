num = int(input("Enter a number: "))
count = 0

while num % 2 == 0 and num > 0:
    num = num // 2
    count += 1

print("The number can be divided by 2", count, "times.")
