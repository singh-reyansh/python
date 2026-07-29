from datetime import datetime
import json
def generate_receipt(
    customers,
    orders,
    subtotal,
    tax_amount,
    tip_amount,
    final_total,
    people_totals
):
    print("FINAL RECIEPT")

    print("\nOrdered Items:")

    for orders in orders:
        print(
            f"{orders['name']} "
            f"- ${orders['price']:.2f}"
            f"(Shared by: "
            f"{', '.join(orders['shared_by'])}"
        )

    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax: ${tax_amount:.2f}")
    print(f"Tip: ${tip_amount:.2f}")
    print(f"Final Total: ${final_total:.2f}")

    print("INDIVIDUAL TOTALS")

    for person, amount in people_totals.items():
        print(
             f"{person}: ${amount:.2f}"
        )
def export_receipt(
    customers,
    people_totals,
    final_total
):
    data = {
        "Date": str(datetime.now()),
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
    f"\nReceipt exported to (filename)"

)
