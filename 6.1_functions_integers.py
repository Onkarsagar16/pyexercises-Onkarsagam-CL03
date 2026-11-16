# 1. In: A list of monthly business sales.
# 2. Process, function by function:
# First function calculates total sales.
# Second function counts the months.
# Third function calculates average sales.
# 3. Out: Total sales, number of months and average.
# 4. My fourth function answers:
# What is the sales summary of the business?
# Splitting the work makes it easier to check
# because each function does only one job.

def calculate_total(sales):
    return sum(sales)

def count_months(sales):
    return len(sales)

def calculate_average(sales):
    if len(sales) == 0:
        return 0
    return sum(sales) / len(sales)

def sales_summary(sales):
    total = calculate_total(sales)
    months = count_months(sales)
    average = calculate_average(sales)
    return total, months, average


sales = [1200, 1500, 1100, 1800, 2000, 1700, 1400, 1600]

# Testing each function separately
# Test 1: Input [1200, 1500], expected total 2700
print(calculate_total([1200, 1500]))

# Test 2: Input [1200, 1500], expected count 2
print(count_months([1200, 1500]))

# Test 3: Input [1200, 1500], expected average 1350
print(calculate_average([1200, 1500]))

# Using all three functions together
print("Sales summary:", sales_summary(sales))