crate1 = ["Mango","Apple","Banana"]
crate2 = ["Banana","Orange","kiwi"]
all_fruits = set(crate1 + crate2)
all_fruits.add("Lemon")
final_fruit_list = list(all_fruits)
print("Fruits available for sale",final_fruit_list)