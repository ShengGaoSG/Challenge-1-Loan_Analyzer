# Loan Analyzer Application
## Valuing Microcredit Loans for a Lending Startup
---

**Part 1: Automate the Calculations**
1.	Use the len() function to calculate the total number of loans in the list.
2.	Use the sum() function to calculate the total of all loans in the list.
3.	Using the sum of all loans and the total number of loans, calculate the average loan price.
4.	Print all calculations with descriptive messages.

**Part 2: Analyze Loan Data**
1.	Use get() on the dictionary of loan data to extract the future value and remaining months on the loan. Save these variables, named future_value and remaining_months, and then print each variable.
2.	Use the formula for present value to calculate the fair value of the loan. Use a minimum required return of 20% as the discount rate. 
Present Value = Future Value / (1+ Annual_Discount_Rate/12)**Months
3.	Write a conditional statement (an if-else statement) to decide whether the present value represents the loan's fair value.
  •	If the present value of the loan is greater than or equal to the cost, then print a message that says that the loan is worth at least the cost to buy it.
  •	If the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

**Part 3: Perform Financial Calculations**

Create a financial function that can be reused with new data values.
1.	Define a new function to calculate present value. The function should meet the following criteria:
o	Include parameters for future_value, remaining_months, and the annual_discount_rate.
o	Return the present_value for the loan.
2.	Use the function to calculate the present value of the new loan. Use an annual_discount_rate of 0.2 for this new loan calculation.


**Part 4: Conditionally Filter Lists of Loans**

Loop through a series of loans that the company is considering and filter them to find the inexpensive ones.
1.	Create a new, empty list named inexpensive_loans.
2.	Use a for loop to select each loan from a list of loans. Inside the for loop, write an if statement to determine whether the loan_price is less than or equal to 500.
3.	If the loan_price is less than or equal to 500, append the loan to the inexpensive_loans list.
4.	Print the list of inexpensive loans.

**Part 5: Save the Results**
Output the list of inexpensive loans to a CSV file.
1.	Use with open to open a new CSV file.
2.	Create a csvwriter using the csv library.
3.	Use the new csvwriter to write the header variable as the first row.
4.	Use a for loop to iterate through each loan in inexpensive_loans.
5.	Use the csvwriter to write the loan.values() to a row in the CSV file.


