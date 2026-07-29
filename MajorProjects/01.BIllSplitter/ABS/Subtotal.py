from typing import Dict, List, Tuple, Optional
def calculate_subtotal(
        orders: List[Dict]
) -> float:
    return round(
        sum(order["price"] for order in orders),
        2
    )