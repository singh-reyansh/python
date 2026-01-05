rows = 5 # You can change this number to make the Z bigger or smaller

for i in range(rows):
    if i == 0 or i == rows - 1:
        print("*"*rows)     #top and bottem rows
    else:
        print(" "*(rows - i - 1) + "*") #Diagonal