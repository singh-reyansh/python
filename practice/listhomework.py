#Manage a grocery shopping list by adding, removing, updating items, and viewing the most important items using basic list operations in Python.
Grocery_list = ["milk", "eggs", "bread", "butter", "cheese"]
Grocery_list.extend(["apples", "bananas", "orange juice"])
Grocery_list.remove('cheese')
Grocery_list.remove('orange juice')
Grocery_list[0] = "milk(cheaper)"
Grocery_list[2]= "bread(cheaper)"
print(Grocery_list)
print("This is the new grocery list!")