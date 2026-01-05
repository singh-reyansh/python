myDictionary = {
    "name":"Reyansh",
    "age":13,
    "Standard":6,
    "name2":"Reyansh",

}
MyList = [100,100,200, 100, 200 ,300]

# Which stores unique elements -- Collection of unique elements 

mySet = {1,2,3,4,4}
print(mySet)
print(len(mySet))

mySet2 = {1,4,2,3,3.10, "HELLO"}
print(mySet2)


Set3 = {True , False}
print(Set3)
Set4 = {True , 1 , False}
print(Set4)
Set5 = {1, True , False}
print(Set5)
Set6 = {True , 0,False}
print(Set6)
Set7 = {True ,False,0}
print(Set7)
Set8 = {1, True , 0,False}
print(Set8)
Set9 = {True ,1, 0,False}
print(Set9)


# Unorderd -- We can't predict the output order 

# No indexing --
mySet = {1,2,3,4,4,5,7,8,90}
print(mySet.pop())
print(mySet.pop())
print(mySet)


# remove -- 
mySet.remove(5)
# mySet.remove(-700)
print(mySet)

# Add 

mySet.add(600)
mySet.add(-400)
print(mySet)


# Update -- 

# mySet.update(300, 500,700)
# print(mySet)


# clear()
# mySet.clear()
# print(mySet)


# Union -- it combines two or more sets taking each and every element only once from all the sets 
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,89}

# 1,2,3,4,5,6,7,89 -- Union

print(set1.union(set2))
print(set1 | set2)
print(set2.union(set1))


# Intersection -- Common elements from both sets

print(set1.intersection(set2))
print(set1 & set2)
# Copy()

set3 = set1.copy()
print(set3)
