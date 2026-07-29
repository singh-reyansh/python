import Constant
import Validate
from typing import Dict, List, Tuple, Optional
def get_customers() -> List[str]:


    num_people = Validate.validate_intigers(
        f"Enter number of people ({Constant.MIN_PEOPLE}-{Constant.MAX_PEOPLE}): ",
       Constant.MIN_PEOPLE,
       Constant.MAX_PEOPLE
    ) 

    customers = []

    print("\nEnter names:")

    for i in range(num_people):
        name = Validate.validate_name(
            f"Person {i+1}: ",
            customers
        )
        customers.append(name)

    print(f"\nGroup created for {len(customers)} people")

    return customers