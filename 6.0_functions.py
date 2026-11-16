# 1. In: A list of monthly sales.
# 2. Process: Add all the sales together.
# 3. Out: Return the total sales.
# 4. My function is called calculate_total_sales.
# The name clearly explains what it does.
# Return allows us to use the result again.
# Print only shows the result on the screen.

def calculate_total_sales(sales):
    return sum(sales)

sales = [1200, 1500, 1100, 1800, 2000, 1700, 1400, 1600]

print(calculate_total_sales(sales))
print(calculate_total_sales(sales[:3]))
print(calculate_total_sales(sales[3:6]))

# Testing with an empty list
print(calculate_total_sales([]))

# An empty list returns 0.
# This is acceptable because there are no sales to add.