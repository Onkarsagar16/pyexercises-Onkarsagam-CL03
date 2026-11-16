# 1. In: Product name, sales amount and month.
# 2. Process: Ask for details and save them in a CSV file.
# 3. Out: business_sales.csv
# Columns: product, month, sales
# 4. These columns help track business sales.
# With 200 rows, I can compare sales and
# find which products sell the most.

import csv
import os

filename = "business_sales.csv"

product = input("Enter product name: ").strip()
month = input("Enter month: ").strip()

while True:
    try:
        sales = float(input("Enter sales amount: "))
        if sales < 0:
            print("Sales cannot be negative.")
        else:
            break
    except ValueError:
        print("Please enter a valid number.")

while product == "":
    product = input("Enter a product name: ").strip()

while month == "":
    month = input("Enter a month: ").strip()

file_exists = os.path.exists(filename)

with open(filename, "a", newline="") as file:
    writer = csv.writer(file)

    if not file_exists or os.path.getsize(filename) == 0:
        writer.writerow(["product", "month", "sales"])

    writer.writerow([product, month, sales])

print("Sales data saved successfully!")