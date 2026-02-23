"""
----- Advanced Bill Splitter

Assignment Overview:

Build a comprehensive bill splitting application that handles real-world restaurant scenarios 

with flexible sharing options, tax/tip calculations, robust error handling, and data export 

capabilities. This project demonstrates mastery of Python data structures, functions, 

error handling, and file I/O.



Required Features



Core Functionality (Mandatory):

1. Multiple Users: 

   - Support 2-10 people splitting the bill

   - Collect unique names for each participant

   - Store participant information in a dictionary



2. Itemized Bill Entry:

   - Allow adding multiple items with names and prices

   - Support continuous item entry until user selects 'done'

   - Track each item's price and sharing configuration



3. Flexible Sharing Options:

   - Each item can be split in three ways:

     - Equally among ALL participants

     - Paid entirely by ONE person

   - Validate that specified people exist in the group



4. Tax Calculation:

   - Apply configurable sales tax percentage to the subtotal

   - Tax is calculated on pre-tip subtotal

   - Display tax amount separately



5. Tip Calculation:

   - Apply configurable tip percentage to the post-tax total

   - Display tip amount separately

   - Tip applies to subtotal + tax



6. Individual Totals:

   - Calculate exact amount each person owes

   - Item costs are split according to sharing rules

   - Tax and tip are split equally among all participants

   - Round to 2 decimal places for currency



**Input Validation & Error Handling (Mandatory):**



7. Robust Input Validation:

   - Amounts: Positive numbers only (prices, tax %, tip %)

   - People count: Integer between 2-10 inclusive

   - Names: Unique, non-empty strings

   - Percentages: Reasonable ranges (tax: 0-20%, tip: 0-30%)

   - Handle all non-numeric inputs gracefully

   - Validate sharing participants exist in group





**Data Management (Mandatory):**



8. Data Structures:

   - Use dictionaries to store:

     - `people_totals`: {name: amount_owed}

     - `items`: {item_name: {'price': float, 'shared_by': [names]}}



9. File Export:

    - Save results to `bill_split.txt` 

    - Include timestamp in filename if possible

    - Format should match console output



10. Detailed Receipt:

    - Generate identical output for both screen and file

    - Show:

      - Itemized breakdown with sharing info

      - Subtotal, tax amount, tip amount

      - Individual amounts owed

      - Grand total verification



Advanced Features:



11. Uneven Split Options:

    - Allow percentage-based splits (e.g., "Alice:60%, Bob:40%")

    - Validate percentages sum to 100%

    - Apply to specific items



12. Payment Tracking:

    - Track partial payments from participants

    - Calculate remaining balances

    - Mark people as "paid in full"



13. Historical Records:

    - Load previous splits from files

    - Track group spending patterns

    - Calculate average contributions





- Main Function: 

- Constants: 

  MAX_PEOPLE = 10

  MIN_PEOPLE = 2

  MAX_TAX_RATE = 20.0

  MAX_TIP_RATE = 30.0

  OUTPUT_FILE = "bill_split.txt"





=== Advanced Bill Splitter ===



--- Group Setup ---

Enter number of people (2-10): 3

Enter names:

Person 1: Alice

Person 2: Bob

Person 3: Charlie



--- Tax & Tip ---

Enter sales tax % (0-20): 8.25

Enter tip % (0-30): 18



--- Add Items ---

Item name: Pizza Margherita

Price: $35.99

Shared by (comma-separated or 'all'): all

✓ Added: Pizza Margherita ($35.99) - Shared by all



Item name: Wine Bottle

Price: $45.00

Shared by: Alice,Bob

✓ Added: Wine Bottle ($45.00) - Shared by Alice, Bob



Item name: Dessert Platter

Price: $22.50

Shared by: Charlie

✓ Added: Dessert Platter ($22.50) - Paid by Charlie



Item name (or 'done'): done



--- Calculations ---

SUBTOTAL: $103.49

SALES TAX (8.25%): $8.54

TIP (18% on $112.03): $20.17

===================================

GRAND TOTAL: $132.20



--- Individual Amounts ---

Alice owes: $54.73

Bob owes:   $39.24

Charlie owes: $38.23

===================================



Results exported to: bill_split.txt



File Output Format (`bill_split.txt`):

Advanced Bill Splitter Results

Date: 2025-01-15 14:30:22

Group: Alice, Bob, Charlie

Tax: 8.25% | Tip: 18%



ITEM BREAKDOWN:

Pizza Margherita ($35.99) - Shared: all

Wine Bottle ($45.00) - Shared: Alice, Bob

Dessert Platter ($22.50) - Shared: Charlie



CALCULATIONS:

Subtotal: $103.49

Tax: $8.54

Tip: $20.17

GRAND TOTAL: $132.20



AMOUNTS OWED:

Alice: $54.73

Bob: $39.24

Charlie: $38.23

Please go through the assignment and let me know if you have any queries.
"""

