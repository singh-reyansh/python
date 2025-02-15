# negative Indexing 
bigString = "   Hello       Programmers!    "
#  -5  -4  -3 -2  -1
print(bigString[-1])
# print(bigString[3:6]) 
print(bigString[-5:-3])

print(type(bigString))

# Uppercase 
print(bigString.upper())


# Lowercase
print(bigString.lower())


# Removing Whitespaces 
print(bigString.strip())

print(len(bigString))

# bigString = "   Hello              Programmers!       "
# print(len(bigString))

# Reyansh Singh 

# replace
# print(bigString.replace("H","E"))

print(bigString.replace("Hello","E"))
address = "123 , England , Arvinder"

print(address.replace(" ,",""))

# Split()

# 123.255.255.255

x = "ARVINDER_PAL_ENGLAND"

print(x.split("_"))

x = "ARVINDER:PAL:ENGLAND"
print(x.split(":"))

# Concatenation - Concat --> When we add two strings 
# 
# Hello + World = HelloWorld

firstName = "Reyansh"
lastname = "Singh"

fullName = firstName + " " +lastname

print(fullName)


firstNum = "12"
# secondNum = "10"
secondNum = 10     #TypeError: can only concatenate str (not "int") to str
#1210
# num1 = 10
# num2 = 12
# print(num1+ num2)
print(firstNum+ str(secondNum))
#W During concatenation no extra space is added
# Int()  float()   str()   bool()

x ="Hello1324"
x = "1234"
print(int(x))

