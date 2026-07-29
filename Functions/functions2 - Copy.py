def One():
    print("Hello I am One")
    Two()
    print("Done")

def Two():
    Three()
    print("I am in Two function")

def Three():
    print("Three Function")


One()


# Hello I am in One
# Three Function
# I am in Two function
# Done