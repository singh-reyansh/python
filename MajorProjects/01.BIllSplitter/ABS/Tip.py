import Validate
import Constant
from typing import Dict, List, Tuple, Optional
def get_tip() -> float:
    print("TIP OPTIONS")
    print("1. 15%")
    print("2. 20%")
    print("3. Custom")
    print("4. No Tip")

    choice = Validate.validate_intigers(
        "Choose tip option: ",
        1,
        4
    )

    if choice == 1:
        return 15.0

    elif choice == 2:
        return 20.0
    
    elif choice == 3:
        return Validate.validate_intigers(
            f"Enter tip % (0-{int(Constant.MAX_TIP_RATE)}): ",
            0,
            int(Constant.MAX_TIP_RATE)
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
