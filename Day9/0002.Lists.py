#REYANSH
secondList = ["Hello",100,100.5,300,300,100]

secondList.insert(4,"Five")
print(secondList)

# append , insert -- These are for individual items / for lists only

# extend -- Need to discussed 

# Delete -- 

secondList.remove(100)

# Incase of multiple occurences it will remove the first element
secondList.remove(300)
print(secondList)

# secondList.pop(3)
# Default last item will be removed 
# secondList.pop()
# secondList.pop()
# secondList.pop()
# secondList.pop()
# secondList.pop()
print(secondList)

# del secondList
# print(secondList)

# clear -- emptying the list
# secondList.clear()
# print(secondList)

# Hello - 0 True - 1 100.5 -2 Five - 3 300 -4 100 - 5
# [start:end]. -- 2 ,3 ,4 
print(secondList[2:5])
print(secondList[-2])
print(secondList[-4:-2])

# Sorting --- Arranging items -- Ascending Order or Descending Order 

# smaller to larger - Ascending 
# larger to smaller - Descending

# 34 , 56, 12, 10, 37, 49

# 10,12,34,37,49,56
# 56, 49,37,34,12,10
newList = [100,-20,30,12,27,-500,345]
newList.sort()
print(newList)

anotherList = ["Hello","You","We","Python"]

anotherList.sort(reverse= True)
print(anotherList)

# secondList.sort()
# print(secondList)

# Copy the anotherList to newList

newList = [100,-20,30,12,27,-500,345]

print(len(newList))
print(len(anotherList))
# newList.append(anotherList)
# anotherList=newList.copy()
print(anotherList)
print(len(anotherList))

# Joininig two lists
print(newList + anotherList)
newList.extend(anotherList)
print(newList)




