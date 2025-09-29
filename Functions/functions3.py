# example 1

"""
def Greet():
    print("Hello")

Greet()
Greet()
Greet()
Greet()
Greet()
Greet()

"""

# example 2 

"""
def Greet(msg):
    print(msg)

# Greet()
Greet("Hello")
Greet("Second Message")
Greet("Good Morning")
Greet("This is another function call")
"""
# example 3
"""
def Greet(fname , lname):
    print(f"Fullname is : {fname} {lname}")

Greet("Reyansh","python")
Greet("Recky","Singh")

"""

#example 4
"""
def AddNumbers(num1,num2):
    result = num1 + num2 
    return result 

# print("Before")
# print(result)
result = AddNumbers(20,40)
# print(result)
# print("After")

print(AddNumbers(20,60))
print(result)
print(result)
"""


# examples 5 

# Write a program that accepts three numbers and prints the sum. 

"""
def Add3(a,b,c):
    print(a+b+c)

Add3(10,20,30)
"""

# Write a program that accepts three numbers and returns the sum. 
"""
def Add3(a,b,c):
    return a+b+c
    # print("hello")

print(Add3(10,20,30))
# print("hello")
"""

# Note : We can have multiple returns in a function.


# examples -6

# Write a function that takes list as input and returns the sum of its elements.

"""
def SumOfElem(li):
    result = 0 
    for i in li:
        result+=i 
    return result

l = [1,2,3,4,5,6]
# print(SumOfElem([1,2,3,4,5,6]))
print(SumOfElem(l))
"""

# example -7 
# Write a function that takes list as input and returns the product of its elements.
"""
def prod(li):
    result = 1
    for i in li:
        result*=i 
    
    return result 

l = [1,2,3,4,5,6]
print(prod(l))

"""

# example - 8
# Write a function that accepts the list and returns the difference between the sum and products of its elements.

"""
def Diff(li):
    result = 1
    sum = 0
    for i in li:
        result*=i 
        sum+=i
    
    return result - sum 

l = [1,2,3,4,5,6]
print(Diff(l))

"""
# example - 9
# Write a function that takes list as input and returns the sum of even elements.

def SumOfEven(li):
    result = 0 
    for i in li:
        if i%2==0:
            result+=i 
    return result

l = [1,2,3,4,5,6]
print(SumOfEven(l))
