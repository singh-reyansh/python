# x = 30 
x = 40
# 40 variables 
# List a data structure which can store mulitple values under one name 

firstList = [30,40,50,10,343,56,78,400,37,300]

# List is dynamic --- We can store as many as values in lists
# We can remove , update , add new elements to list
# 

print(len(firstList))       #size of the list

# we can add items of different types in a single list
# x = 50 
# x = "Hello"
secondList = ["Hello",True,100,100.5,300]

x = 40
print(x)

#printing the complete list
print(secondList)

# Indexing -- List are indexed -- These are ordered
"""
    SecondList ==    "hello" True  100   100.5
                        0     1     2      3
"""
# Printing any element from the list 
print(secondList[1])

# TO print last element
print(secondList[-1])
print(secondList[len(secondList)-1])

# first element
print(secondList[0])
secondList = ["Hello",True,100,100.5,300,300,100]
# List is -- Duplicates are allowed
# Sets , tuple , Dictionary , List

print(type(secondList))


# CRUD - Create -- Write (Adding) 
# append -- inserts items at the end of the list
print(len(secondList))
newList =["World",400,10000]
secondList.append(newList)
secondList.append("Final")
print(len(secondList))
print(secondList[7])
# Read -- just printing  
print(secondList[0])
# Update -- Modifying the existing one 
secondList[2] = 200

print(secondList)
# Delete -- Removing the element

