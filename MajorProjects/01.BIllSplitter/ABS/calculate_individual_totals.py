from typing import Dict, List, Tuple, Optional
def calculate_individual_totals(
    customers: List[str],
    orders: List[Dict],
    tax_amount: float,
    tip_amount: float
) -> Dict[str, float]:
    
    people_totals = {
        customers: 0
        for customers in customers
    }
    
    for orders in orders:
        split_amount = (
            orders["price"] /
            len(orders["Shared_by"])
        )

        for person in orders["shared_by"]:
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
