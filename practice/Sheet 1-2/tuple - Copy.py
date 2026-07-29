# tuple -- 

myTuple = ("apple","Hello","Banana")
print(myTuple)

# Ordered -- tuples are ordered.

# Unchangebale -- We can not modify a tuple 

# ONce created we can not add or remove any element from tuple.

# tuples are indexed. 
print(myTuple[0])
print(type(myTuple))
# Slicing -- listname[start:end]
myList = [12,34,56,78,90,13,46,79]
#                               -1
print(myList)
print(myList[-4])
print(len(myList))

print(myList[2:7])

# If we want to change it -- We have to convert a tuple into list /dictionary / set 

# tuples allow duplicate values

# Negative Indexing -- 

myTuple2 = ("apple",)
print(myTuple2)
print(myTuple)

# It can have different types of data.

# Updating -- 
myList2 = list(myTuple2)
myList2.append("New Item")
myTuple3 = tuple(myList2)
print(myTuple3)

print(myTuple2+ myTuple3)
# Delete a tuple 
# del myTuple3
# print(myTuple3)
