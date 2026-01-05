angle1 = int(input("Enter the first angle: "))
angle2 = int(input("Enter the second angle: "))
angle3 = int(input("Enter the third angle: "))

if angle1 + angle2 + angle3 == 180:
    print("This is a valid triangle.")
else:
    print("This is not a valid triangle.")