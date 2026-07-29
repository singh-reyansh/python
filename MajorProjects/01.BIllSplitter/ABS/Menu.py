import Menu
FOOD_MENU = {
    1: ["Burger",8.99],
    2: ["Pizza",11.50],
    3: ["Fries",3.99],
    4: ["Soda",2.50],
    5: ["Tenders",7.50],
}

def display_menu():



    print(f"{'Item No':<10}{'Item Name':<25}{'Price'}")

    for item_num, (name, price) in Menu.FOOD_MENU.items():
        print(
            f"{item_num:<10}"
            f"{name:<25}"
            f"${price:.2f}"
        )