import json
from datetime import datetime
from typing import Dict, List, Tuple, Optional


# -----------------------------------
# Project Constants
# -----------------------------------
MAX_PEOPLE = 10
MIN_PEOPLE = 2
TAX_RATE = 15.0
MAX_TIP_RATE = 30.0

FOOD_MENU = {
    1: ["Pizza Margherita", 35.99],
    2: ["Soda", 2.99],
    3: ["Pepperoni Pizza", 37.99],
    4: ["Veggie Pizza", 40.99],
    5: ["Meat Lover's Pizza", 42.99]
}

LINE_WIDTH = 60
HASHED_LINE = "#" * LINE_WIDTH
SINGLE_LINE = "-" * LINE_WIDTH
DOTTED_LINE = "_" * LINE_WIDTH


# -----------------------------------
# Validation Functions
# -----------------------------------
def validate_integer(prompt: str, min_val: int, max_val: int) -> int:
    while True:
        try:
            value = int(input(prompt))

            if value < min_val or value > max_val:
                print(
                    f"Error: Value must be between {min_val} and {max_val}"
                )
                print(DOTTED_LINE)
                continue

            return value

        except ValueError:
            print("Error: Please enter valid integer.")
            print(DOTTED_LINE)


def validate_name(
    prompt: str,
    existing_names: List[str]
) -> str:
    while True:
        name = input(prompt).strip()

        if not name:
            print("Name cannot be empty.")
            continue

        if name.lower() in [
            existing.lower()
            for existing in existing_names
        ]:
            print("Name already exists.")
            continue

        return name


def validate_sharing_input(
    shared_by: str,
    customers: List[str]
) -> Optional[List[str]]:

    if shared_by.lower() == "all":
        return customers

    names = [
        name.strip()
        for name in shared_by.split(",")
    ]

    valid_names = [
        customer.lower()
        for customer in customers
    ]

    for name in names:
        if name.lower() not in valid_names:
            print(f"{name} is not part of group.")
            return None

    return names


# -----------------------------------
# Customer Setup
# -----------------------------------
def get_customers() -> List[str]:
    print(HASHED_LINE)
    print("GROUP SETUP")
    print(HASHED_LINE)

    num_people = validate_integer(
        f"Enter number of people ({MIN_PEOPLE}-{MAX_PEOPLE}): ",
        MIN_PEOPLE,
        MAX_PEOPLE
    )

    customers = []

    print("\nEnter names:")

    for i in range(num_people):
        name = validate_name(
            f"Person {i+1}: ",
            customers
        )
        customers.append(name)

    print(f"\nGroup created for {len(customers)} people")
    print(SINGLE_LINE)

    return customers


# -----------------------------------
# Menu
# -----------------------------------
def display_menu():
    print(HASHED_LINE)
    print("RESTAURANT MENU")
    print(HASHED_LINE)

    print(f"{'Item No':<10}{'Item Name':<25}{'Price'}")

    for item_num, (name, price) in FOOD_MENU.items():
        print(
            f"{item_num:<10}"
            f"{name:<25}"
            f"${price:.2f}"
        )

    print(SINGLE_LINE)


# -----------------------------------
# Common Orders
# -----------------------------------
def order_common_items(
    customers: List[str]
) -> List[Dict]:

    orders = []

    print("\nCOMMON ORDERING MODE")

    while True:
        item_choice = validate_integer(
            "Enter item number (0 to finish): ",
            0,
            len(FOOD_MENU)
        )

        if item_choice == 0:
            if not orders:
                print("Please add at least one item.")
                continue
            break

        if item_choice not in FOOD_MENU:
            print("Invalid item.")
            continue

        quantity = validate_integer(
            "Enter quantity: ",
            1,
            100
        )

        item_name, item_price = FOOD_MENU[item_choice]

        while True:
            shared_input = input(
                "Shared by (comma names or 'all'): "
            ).strip()

            shared_by = validate_sharing_input(
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


# -----------------------------------
# Individual Orders
# -----------------------------------
def order_separate_items(
    customers: List[str]
) -> List[Dict]:

    orders = []

    print("\nINDIVIDUAL ORDERING MODE")

    for person in customers:
        print(SINGLE_LINE)
        print(f"{person}'s Order")

        while True:
            item_choice = validate_integer(
                "Enter item number (0 to finish): ",
                0,
                len(FOOD_MENU)
            )

            if item_choice == 0:
                break

            quantity = validate_integer(
                "Enter quantity: ",
                1,
                100
            )

            item_name, item_price = FOOD_MENU[item_choice]

            for _ in range(quantity):
                orders.append({
                    "name": item_name,
                    "price": item_price,
                    "shared_by": [person]
                })

            print(
                f"Added {quantity} x {item_name}"
            )

    return orders


# -----------------------------------
# Get Orders
# -----------------------------------
def get_orders(
    customers: List[str]
) -> List[Dict]:

    display_menu()

    print("\nOrdering Modes")
    print("1. Common Orders")
    print("2. Individual Orders")
    print("3. Mixed Orders")

    mode = validate_integer(
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


# -----------------------------------
# Bill Calculations
# -----------------------------------
def calculate_subtotal(
    orders: List[Dict]
) -> float:
    return round(
        sum(order["price"] for order in orders),
        2
    )


def calculate_tax(
    subtotal: float
) -> Tuple[float, float]:

    tax_amount = round(
        subtotal * (TAX_RATE / 100),
        2
    )

    total_with_tax = round(
        subtotal + tax_amount,
        2
    )

    return tax_amount, total_with_tax


# -----------------------------------
# Tip
# -----------------------------------
def get_tip() -> float:
    print(SINGLE_LINE)
    print("TIP OPTIONS")
    print("1. 15%")
    print("2. 20%")
    print("3. Custom")
    print("4. No Tip")
    print(SINGLE_LINE)

    choice = validate_integer(
        "Choose tip option: ",
        1,
        4
    )

    if choice == 1:
        return 15.0

    elif choice == 2:
        return 20.0

    elif choice == 3:
        return validate_integer(
            f"Enter tip % (0-{int(MAX_TIP_RATE)}): ",
            0,
            int(MAX_TIP_RATE)
        )

    return 0.0


def calculate_tip(
    total_with_tax: float,
    tip_rate: float
) -> Tuple[float, float]:

    tip_amount = round(
        total_with_tax * (tip_rate / 100),
        2
    )

    final_total = round(
        total_with_tax + tip_amount,
        2
    )

    return tip_amount, final_total


# -----------------------------------
# Split Individual Totals
# -----------------------------------
def calculate_individual_totals(
    customers: List[str],
    orders: List[Dict],
    tax_amount: float,
    tip_amount: float
) -> Dict[str, float]:

    people_totals = {
        customer: 0
        for customer in customers
    }

    for order in orders:
        split_amount = (
            order["price"] /
            len(order["shared_by"])
        )

        for person in order["shared_by"]:
            people_totals[person] += split_amount

    extra_cost = (
        tax_amount + tip_amount
    ) / len(customers)

    for person in people_totals:
        people_totals[person] += extra_cost
        people_totals[person] = round(
            people_totals[person],
            2
        )

    return people_totals


# -----------------------------------
# Receipt
# -----------------------------------
def generate_receipt(
    customers,
    orders,
    subtotal,
    tax_amount,
    tip_amount,
    final_total,
    people_totals
):
    print(HASHED_LINE)
    print("FINAL RECEIPT")
    print(HASHED_LINE)

    print("\nOrdered Items:")

    for order in orders:
        print(
            f"{order['name']} "
            f"- ${order['price']:.2f} "
            f"(Shared by: "
            f"{', '.join(order['shared_by'])})"
        )

    print(SINGLE_LINE)

    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax: ${tax_amount:.2f}")
    print(f"Tip: ${tip_amount:.2f}")
    print(f"Final Total: ${final_total:.2f}")

    print(SINGLE_LINE)
    print("INDIVIDUAL TOTALS")

    for person, amount in people_totals.items():
        print(
            f"{person}: ${amount:.2f}"
        )


# -----------------------------------
# Export
# -----------------------------------
def export_receipt(
    customers,
    people_totals,
    final_total
):
    data = {
        "date": str(datetime.now()),
        "customers": customers,
        "individual_totals": people_totals,
        "final_total": final_total
    }

    filename = (
        f"bill_"
        f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    )

    with open(filename, "w") as file:
        json.dump(
            data,
            file,
            indent=4
        )

    print(
        f"\nReceipt exported to {filename}"
    )


# -----------------------------------
# Main
# -----------------------------------
def main():
    print(HASHED_LINE)
    print("WELCOME TO ADVANCED BILL SPLITTER")
    print(HASHED_LINE)

    try:
        customers = get_customers()

        orders = get_orders(customers)

        subtotal = calculate_subtotal(orders)

        print(SINGLE_LINE)
        print(f"Subtotal: ${subtotal:.2f}")

        tax_amount, total_with_tax = calculate_tax(
            subtotal
        )

        print(
            f"Tax ({TAX_RATE}%): "
            f"${tax_amount:.2f}"
        )

        print(
            f"Total After Tax: "
            f"${total_with_tax:.2f}"
        )

        tip_rate = get_tip()

        tip_amount, final_total = calculate_tip(
            total_with_tax,
            tip_rate
        )

        print(
            f"Tip Amount: "
            f"${tip_amount:.2f}"
        )

        print(
            f"Final Total: "
            f"${final_total:.2f}"
        )

        people_totals = calculate_individual_totals(
            customers,
            orders,
            tax_amount,
            tip_amount
        )

        generate_receipt(
            customers,
            orders,
            subtotal,
            tax_amount,
            tip_amount,
            final_total,
            people_totals
        )

        export_receipt(
            customers,
            people_totals,
            final_total
        )

    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")

    except Exception as e:
        print(
            f"\nAn error occurred: {str(e)}"
        )


if __name__ == "__main__":
    main()