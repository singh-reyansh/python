import Constant
from typing import Dict, List, Tuple, Optional
def calculate_tax(
    subtotal: float
) -> Tuple[float, float]:
    
    tax_amount = round(
        subtotal * (Constant.TAX_RATE / 100),
    )

    total_with_tax = round(
        subtotal + tax_amount,
        2
    )

    return tax_amount, total_with_tax
