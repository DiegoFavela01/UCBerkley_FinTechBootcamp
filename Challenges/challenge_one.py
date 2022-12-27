import csv
###Module 1 Challenge###

#List of loan costs
loan_costs = [500, 600, 200, 1000, 450]

# #Part 1: Automate the Calculations

#Find the quanity of loans and print value
loan_quantity = len(loan_costs) 
print(f"There are {loan_quantity} loans in the list")

#Find the sum of all the loans and print value
loan_sum= sum(loan_costs)
print(f"The total sum of the loan is ${loan_sum}")

#Find the average cost of the loans and print value
average_loan = loan_sum / loan_quantity
print(f"The average cost of the loans is ${average_loan}")

# #Part 2: Analyze Loan Data

# Data from a loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

#Get the future value and remaining months from the loan data and print
future_value = loan.get("future_value")
print(f"The future value of the loan is ${future_value}")

remaining_months = loan.get("remaining_months")
print(f"The remaning months of the loan is {remaining_months}")

#Formula to find present value and set the discount rate
discount_rate = 0.2
present_value = future_value / (1 + discount_rate) ** remaining_months


# Check if the present value is greater than or equal to the loan price and print action
if present_value >= loan.get("loan_price"):
    print("The loan is worth at least the cost to buy it")
else:
    print("The loan is too expensive and not worth the price")

# #Part 3: Perform Financial Calculations.

#Data for new loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

#function that calculates the present value of a loan, given the future value, remaining months, and annual discount rate
def present_value(future_value, remaining_months, annual_discount_rate):
    discount_rate = annual_discount_rate / 12
    present_value = future_value / (1+ discount_rate) ** remaining_months
    return present_value

#Get the future value and remaning months from the new loan and set the annual discount rate
future_value = new_loan.get("future_value")
remaining_months = new_loan.get("remaining_months")
annual_discount_rate = 0.2

#Calcuate the present value of the new loan and print
present_value = present_value(future_value, remaining_months, annual_discount_rate)
print(f"The present value of the loan is: {present_value:.2f}")

# #Part 4: Conditionally filter lists of loans.

#Data list of loans
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

#Empty list of inexpensive loans created
inexpensive_loans = []

#Set the parameters for the loans to be added to inexpensive loans
for loan in loans:
    if loan.get("loan_price") <= 500:
        inexpensive_loans.append(loan)

#Print the inexpensive loans
print("inexpensive loans:")
for loan in inexpensive_loans:
    print(loan)

# #Part 5: Save the results.

#Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = "inexpensive_loans.csv"

#Open a new CSV file in write mode and use the `csvfile` variable to write to it
with open(output_path, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    #Iterate through each loan in the `inexpensive_loans` list
    for loan in inexpensive_loans:
        # Write the values of each loan as a row in the CSV file
        writer.writerow(loan.values())
