import json
from datetime import datetime
from typing import Dict, List, Tuple, Optional
import Constant
import Menu
import Order
import Validate
import Subtotal
import Get_Customers
import Tax
import Tip
import calculate_individual_totals
import Receipt

def main():
    print("WELCOME TO ADVANCED BILL SPLITTER")

    try:
        customers = Get_Customers.get_customers()

        orders = Order.get_orders(customers)

        subtotal = Subtotal.calculate_subtotal(orders)

        print(f"Subtotal: ${subtotal:.2f}")

        tax_amount, total_with_tax, = Tax.calculate_tax(
            subtotal
        )

        print(
            f"Tax ({Constant.TAX_RATE}%): "
            f"${tax_amount:.2f}"
        )

        print(
            f"Total After TAX: "
            f"${total_with_tax}"
        )

        tip_rate = Tip.get_tip()

        tip_amount, final_total = Tip.calculate_tip(
            total_with_tax,
            tip_rate
        )

        print(
            f"Tip Amount: "
            f"${tip_amount:.2f}" 
        )

        print(
            f"Final Total: "
            f"${tip_amount}"
        )

        people_totals = calculate_individual_totals(
            customers,
            orders,
            tax_amount,
            tip_amount,
        )

        Receipt.generate_receipt(
            customers,
            orders,
            subtotal,
            tax_amount,
            tip_amount,
            final_total,
            people_totals
        )

        Receipt.export_receipt(
            customers,
            people_totals,
            final_total
        )

    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")

    except Exception as e:
        print(
            f"\nAn error has occured: {str(e)}"
        )

if __name__ == "__main__":
    main()