def multiplication_table():
    n = int(input("Enter a number to print its multiplication table: "))

    for i in range (1,11):
        print(f"{n} x {i} = {n * i}")

multiplication_table()