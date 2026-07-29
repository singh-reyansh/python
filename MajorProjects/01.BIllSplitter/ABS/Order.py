import Validate
import Menu
from typing import Dict, List, Tuple, Optional

def order_common_items(
    customers: List[str]
) -> List[Dict]:

    orders = []

    print("\nCOMMON ORDERING MODE")

    while True:
        item_choice = Validate.validate_intigers(
            "Enter item number (0 to finish): ",
            0,
            len(Menu.FOOD_MENU)
        )

        if item_choice == 0:
            if not orders:
                print("Please add at least one item. ")
                continue
            break
        if item_choice not in Menu.FOOD_MENU:
            print("Invalid items. ")
            continue

        quantity = Validate.validate_intigers(
            "Enter quantity: ",
            1,
            100
        ) 

        item_name, item_price = Menu.FOOD_MENU[item_choice]

        while True:
            shared_input = input(
                "Shared by (comma names or 'all'): "
            ).strip()

            shared_by = Validate.validate_sharing_input(
                shared_input,
                customers
            )

            if shared_by is not None:
                break

        for _ in range(quantity):
            orders.append({
                "name": item_name,
                "price": item_price,
                "shared_by": shared_by
            })

        print(
            f"Added {quantity} x {item_name}"
        )

    return orders

def order_separate_items(
        customers: List[str]
) -> List[Dict]:
    
    orders = []

    print("\nINDIVIDUAL ORDERING MODE")

    for person in customers:
        print(f"{person}'s Order")

        while True:
            item_choice = Validate.validate_intigers(
                "Enter item number (0 to finish): ",
                0,
                len(Menu.FOOD_MENU)
            )

            if item_choice == 0:
                break

            quantity = Validate.validate_intigers(
                "Enter quantity: ",
                1,
                100
            )

            item_name, item_price = Menu.FOOD_MENU[item_choice]

            for _ in range(quantity):
                orders.append({
                "name": item_name,
                "price": item_price,
                "shared_by": [person]
                })

                print(
                    f"Added {quantity} X {item_name}"
                )

    return orders

def get_orders(
    customers: List[str]
) -> List[Dict]:
    
    Menu.display_menu()

    print("\nOrdering Modes")
    print("1. Common Orders")
    print("2. Individual Orders")
    print("3. Mixed Orders")

    mode = Validate.validate_intigers(
        "Choose option: ",
        1,
        3
    )

    all_orders = []

    if mode == 1:
        all_orders = order_common_items(customers)

    elif mode == 2:
        all_orders = order_separate_items(customers)

    elif mode == 3:
        print("\nAdding common orders...")
        common_orders = order_common_items(customers)
        all_orders.extend(common_orders)

        print("\nAdding individual orders...")
        individual_orders = order_separate_items(customers)
        all_orders.extend(individual_orders)
    
    return all_orders