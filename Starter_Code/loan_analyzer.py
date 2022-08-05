# coding: utf-8
import csv
from pathlib import Path

"""Part 1: Automate the Calculations.

Automate the calculations for the loan portfolio summaries.

"""
loan_costs = [500, 600, 200, 1000, 450]

# Use the `len` function to calculate the total number of loans in the list.
# Print the number of loans from the list
total_number_of_loans = len(loan_costs)
print("The total number of loans is ", total_number_of_loans)

# Use the `sum` function to calculate the total of all loans in the list.
# Print the total value of the loans
total_sum_of_loans = sum(loan_costs)
print("The total sum of loans is ", total_sum_of_loans)

# Using the sum of all loans and the total number of loans, calculate the average loan price.
# Print the average loan amount
average_loan = total_sum_of_loans/total_number_of_loans
print("The average loan amount is ", average_loan)

"""Part 2: Analyze Loan Data.

Analyze the loan to determine the investment evaluation.

"""

loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Use get() on the dictionary of additional information to extract the Future Value and Remaining Months on the loan.
# Print each variable.
future_value = loan.get("future_value")
remaining_months = loan.get("remaining_months")
print("The future value of the loan is ", future_value)
print("The remaining months of the loan is ", remaining_months)


# Use the formula for Present Value to calculate a "fair value" of the loan.
# Use a minimum required return of 20% as the discount rate.
# Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months
present_value = future_value / (1 + 0.2/12) ** remaining_months

# Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
# If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
# Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.
if present_value >= loan.get("loan_price"):
    print("The loan is worth at least the cost to buy it")
else:
    print("The loan is too expensive and not worth the price")


"""Part 3: Perform Financial Calculations.

Perform financial calculations using functions.

"""

new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Define a new function that will be used to calculate present value.
# This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
# The function should return the `present_value` for the loan.
def calculate_present_value(future_value, remaining_months, annual_discount_rate):
    present_value = future_value / (1 + annual_discount_rate / 12) ** remaining_months
    return present_value


# Use the function to calculate the present value of the new loan given below.
# Use an `annual_discount_rate` of 0.2 for this new loan calculation.
present_value = calculate_present_value(new_loan.get("future_value"), new_loan.get("remaining_months"), 0.2)
print(f"The present value of the loan is: {present_value}")


"""Part 4: Conditionally filter lists of loans.

Use a loop to iterate through a series of loans and select only the inexpensive loans.

"""

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# Create an empty list called `inexpensive_loans`
inexpensive_loans = []

# Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
for i in loans:
    if i.get("loan_price") <= 500:
        inexpensive_loans.append(i)

# Print the `inexpensive_loans` list
for i in inexpensive_loans:
    print(i)


"""Part 5: Save the results.

Output this list of inexpensive loans to a csv file

"""

# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")

# Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
with open(output_path, 'w', newline='') as csvfile:
    csvwriter  = csv.writer(csvfile)

    #Write header row first
    csvwriter.writerow(header)

    #Write the data rows
    for row in inexpensive_loans:
        csvwriter.writerow(row.values())
