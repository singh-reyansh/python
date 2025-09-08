# Function - is a block of code. 

# {}

"""
package main
import "fmt"
func main() {
    fmt.Println("hello world")
}

"""
# print("Hello World")

# Indentation 

# if True:
#     print(1)
#     print(3)
#     if True:
#         print("Hello")
# print("Outside Block")


# Two types of function -- System Defined Function / Language Defined FUnctions , User Defined FUnctions

# def Name()
# System Defined Function -- We don't write code for these functions. It is already provided by lanagauge.
# print("Hello World")
# type()
# input()
# int()
# print("Hello Print")

# User Defined -- 
"""
def MyFunction():
    print("Hello")

MyFunction()
"""

# Reusable 
# MyFunction()
# MyFunction()
# MyFunction()
# MyFunction()
# MyFunction()
# MyFunction()
# MyFunction()
# print("Hello")

"""
def MyFunction(fname):
    print("Hello", fname)

MyFunction("Reyansh")
MyFunction("Arvinder")

"""
# DRY -- Do Not repeat yourself

"""
def AddNumbers(a,b):
    print("Sum of numbers is :",a+b)

AddNumbers(23,45)
AddNumbers(223,45)
AddNumbers(23,475)
AddNumbers(203,45)

"""



def AddNumbers(a,b):
    result = a + b 
    print("Sum of numbers is :",result)
    return result
    # print("Hello")

# print(result)
x = AddNumbers(23,45)

print(x+100)

# Return -- 1. It returns a copy of the local variables   2. It marks the ending of the program.


def Fullname(fname , lname):
    return fname + lname 

# fullname = Fullname("Python", "Language")
# print(fullname)

# or 
# print(Fullname("Python", "Coder"))

"""

"""
def First():
    print("Hello I am in First")
    Second()
    print("Finished")

def Second():
    print("Hello I am in Second")

First()
# def First():
#     print("Hello I am in First")
#     Second()
#     print("Hello I am after Second")

# def Second():
#     print("Hello I am in Second")

# First()


# def Hello():
#     x = 40 
#     y = 6
#     print(x+y)
# Hello()
# print("Hello")
# Hello()
# Hello()
# Hello()
# Hello()
