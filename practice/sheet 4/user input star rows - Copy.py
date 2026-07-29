def star_pattern():
    rows = int(input("Enter the number of rows you want the star pattern to be: "))
    for i in range(1, rows + 1):
        print("*" * i)

star_pattern()