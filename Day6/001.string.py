# String - a sequence of charatcers / letters 


name = "Arvinder"
std = "$st567_1fhkloi"

# If any value is enclosed in double or single qiotes that means it is a string data type.
print(type(name))        #<class 'str'>
print(type(std))         # <class 'str'>
print(type("Hello"))     #<class 'str'>

myName = """This is my first line
This is my second line 
I am in third line"""

myNewname= '''Hello thi is line number 1 
I can go to second line
Third line'''


# Selection of triple double or single quotes 
greet = 'My name is ,"Arvinder Pal"'
greet = "My name is , 'Reyansh'"


# Escape Symbols 

greet3 = "My Name is , \"Arvinder Pal\"."

# Strings are indexed data types.

'''
name = "Hello"
H e l l o
0 1 2 3 4   -- Index

In programming , indexing (numbering) starts from 0. 
'''
example = "Reyansh"    # 6, 7 
print(example[5])  #s

print(example[0])  #R

# print(example[10])    #IndexError: string index out of range

# 0 1 2 3 4 5 6 7 8 9

# Length of the string 
example = "This is good"
x = len(example)
print(x)

# To print the last element
print(example[x-1])

# print(example[len(example)-1])

# in operator -- to check if any substring is a part of the bigger string

text = "This is my code and I write code daily. I like coding in Python."

print("for" in text)   # Not present - False
print("code" in text)   # Present - True

print("for" not in text)   # Not Present - True
print("code" not in text)   # Present - False 

# Slicing a string 
bigString = "Reyansh Singh"

print(len(bigString))

# [start:end]
print(bigString[:])
print(bigString)

# End is always excluded
print(bigString[:7])

# Start is included

print(bigString[3:6])    # 3 4 5


print(bigString[3:])


# negative Indexing 

#  -5  -4  -3 -2  -1
print(bigString[-1])