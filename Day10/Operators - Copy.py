# Operators -- 

# Arithmetic Operators 
a = 50
b = 40

# + -- Addtition 
print(a+b)
# - Subtraction
print(a-b)
# * -- Multiplication 
print(a*b)
# /  --  Division.   5/3 == 
print(10/3)
print(10/5)
# //  -- Integer Division
print(10//3)
print(10//5)
# print(int(10/3))

# % Modulus operator -- Remainder Operator 
print(10%3)
print(11%3)
print(12%3)

# BODMAS -- PEMDAS
# () -- {} , []
print(3+(4*5))

print("---------Comparision Operator----------")
# Comparision Operator -- Comapares two values and return the result in true or false
# a = 50
# b = 40
# > greater than 
print(a>b) 

# < less than 
print(a<b)

# greater than equal to >=
# greater or eqaul to 
print(a>=b)
# print(12>=12)
# <= less than eqaul to 
print(a<=b)

# equal to ==
print(a==b)

print("---------Assignment Operator----------")
# Asignment OPerator --
x = 30

# x+=5 -> x = x+5
x+=5    #x = 30+5
print(x)

x-=10
print(x)

x*=3
print(x)

x/=5
print(x)

# 2^3
# There is no exponent operator in python we have to use math module
# import math
# print(int(math.pow(2,3)))


print("---------Logical Operator----------")

# and or not
# When we want to combine two or more conditions together

# and -- Operator 
# It works only if both of the conditions return true 

# True and True == True
# True and False == False
# False and True == False
# False and False == False
age = 18
isGoodDriver = False
# print(age>18 and isGoodDriver==True)
# print(age>18 and isGoodDriver==True)

# or -- Operator 
# It works only if one of the conditions return true 

# True or True == True
# True or false == True
# False or True == True
# False or False == False
# 18+
# print(age>=18 or isGoodDriver==True)

# not operator

print(3>5)
print(not(3>5))


# Bitwise operator -- 

# Binary -- 0 1 0 1 1 1 0 0 0 0

# and-- & or--| xor-- ^  << >>  Not -- ~

# 3 -- 11

# 1     1      1 
# 2^2   2^1  2^0 == 4+2+1 = 7


# 1     0       0       1       1       0 
# 2^5   2^4.    2^3     2^2     2^1     2^0  

# 32+4+2 = 38

# 1     0       1       0
# 2^3   2^2     2^1     2^0
# 10

# 15 -- 
# 2^3   2^2     2^1     2^0
# 1     1       1      1

# 15 = 8 + 4+ 2 +1

# 23 --
# 1 0 1 1 1
# 16 + 4 + 2+1