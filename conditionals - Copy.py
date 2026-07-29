# Conditionals (Selection):
# print("Hello First Line ")
# print("Hello Second Line ")
# print("Hello THird Line ")

# print("Hello First Line ")
# if True:
#   print("Hello Second Line ")
# else: 
#   print("Hello THird Line ")

# print("Hello First Line ")
# if False:
#   print("Hello Second Line ")
# else: 
#   print("Hello THird Line ")

# if condition:
#   if condition is true exceute this if block 
# else:
#  if condition is False exceute this else block

# x = 40
# if x < 30:
#   print("X is greater than 30 ")
# else:
#   print("X is smaller than 30 ")

#  if elif . . . . else
day =4 

if day==1:
  print("Sunday")
elif day==2:
  print("Monday")
elif day==3:
  print("Tuesday")
elif day==4:
  print("Wednesday")
elif day==5:
  print("Thursday")
elif day==6:
  print("Friday")
elif day==7:
  print("Saturday")
else:
  print("Invalid condition")
  
# if day==1:
#   print("Sunday")
# if day==2:
#   print("Monday")
# if day==3:
#   print("Tuesday")
# if day==4:
#   print("Wednesday")
# if day==5:
#   print("Thursday")
# if day==6:
#   print("Friday")
# if day==7:
#   print("Saturday")
# else:
#   print("Invalid condition")

x = 40

# if x < 40:
#   print("X is positive number")
# else:
#   print("X is a negative number")  

# if x ==0:
#   print("X is zero")
# else:
#   print("X is not zero") 
  
# if x < 0:
#   print("X is a negative number")
# else:
#   print("X is a positive number")

# if x < 0:
#   print("X is a negative number")
# elif x>0:
#   print("X is a positive number")
# else:
#   print("x is zero")

# Printing Whether a number is odd or even
# 40%2 == 0
# 13%2 ==1 

# x =41
# if x%2==0:
#   print("Number is even")
# else:
#   print("Number is odd")
  

# What all can be treated as True -- Any number +ve , -ve (except 0),any string (except empty string),True
#  False -- 0, False , EMpty String

# if False:
#   print("True")
# else:
#   print("False")

# if 0:
#   print("True")
# else:
#   print("False")

# if "":
#   print("True")
# else:
#   print("False")

# if True:
#   print("True")
# else:
#   print("False")


# if 100:
#   print("True")
# else:
#   print("False")

# if "Helo":
#   print("True")
# else:
#   print("False")
  
# Given an integer n, for every positive integer i <= n, the task is to print,
# “FizzBuzz” if i is divisible by 3 and 5,
# “Fizz” if i is divisible by 3,
# “Buzz” if i is divisible by 5
# “i” as a string, if none of the conditions are true.

# n= 7
# if n%3==0 and n%5==0:
#   print("FizzBuzz")
# elif n%3==0:
#   print("Fizz")
# elif n%5==0:
#   print("Buzz")
# else:
#   print(str(n))


day =4 
day =10
match day:
  case 1:
    print("Sunday")
  case 2:
    print("Monday")
  case 3:
    print("Tuesday")
  case 4:
    print("Wednesday")
  case 5:
    print("Thursday")
  case 6:
    print("Friday")
  case 7:
    print("Saturday")
  case _:
    print("Invalid input")

# day ="Monday"

# match day:
#   case "Sunday":
#     print(1)
#   case "Monday":
#     print(2)

  
# day =7
# match day:
#   case 1 | 2 | 3 | 4 | 5:
#     print("Working days")
#   case 6 | 7:
#     print("Weekends")
#   case _:
#     print("Invalid input")

# We can match a tuple also using the match case --
# Write a program which check the position of a point on a 2d plane :
#  print -- If number is in xy plane , on x -axis , on y axis or at origin
#  3,2 --> 3,0 --> 0,5 ---> 0,0
