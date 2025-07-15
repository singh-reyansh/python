print("Currency converter 💵")
GBP = .74
INR = 85.86
Euro = .86
while True:
    print("press 1 for GBP \npress 2 for INR\npress 3 for Euro \n press 4 to end the program")
    choice = int(input("Enter your choice = "))
    USD= float(input("Enter USD amount = "))
    if choice==1:
        USD_GBP= USD*GBP
        print(f"{USD} USD= {USD_GBP} GBP")
    elif choice == 2:
        USD_INR= USD*INR
        print(f"{USD} USD = {USD_INR} INR")
    elif choice== 3:
        USD_Euro= USD*Euro
        print(f"{USD} USD= {USD_Euro} Euro")