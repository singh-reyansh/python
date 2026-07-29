from typing import Dict, List, Tuple, Optional
def validate_intigers(prompt: str, min_val: int, max_val: int) -> int:
    while True:
        try:
            value = int(input(prompt))

            if value < min_val or value > max_val:
                print(
                    f"Error: Value must be between {min_val} and {max_val}"
                )
                continue
            return value
        except ValueError:
            print("Error: Please enter valid intiger.")
    

def validate_name(
    prompt: str,
    existing_names: List[str]
) -> str:
    while True:
        name = input(prompt).script()

        if not name:
            print("Name cannot be empty. ")
            continue

        if name.lower() in [
            existing.lower()
            for existing in existing_names
        ]:
            print("Name already exsists. ")
            continue

        return name
    
def validate_sharing_input(
    shared_by: str,
    customers: List[str]
) -> Optional[List[str]]:
    
    if shared_by.lower() == "all":
        return customers
    
    names = [
        names.strip()
        for name in shared_by.split(",")
        ]

    valid_names = [
        customer.lower()
        for customer in customers
    ]

    for name in names:
        if name.lower() not in valid_names:
            print(f"{name} is not part of group. ")
            return None
    
    return names