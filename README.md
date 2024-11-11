# Room Expense Splitter

This project is a Python program designed to help roommates split monthly living expenses. It takes inputs such as rent, food expenses, electricity usage, and the number of people living together, then calculates each person’s share of the total monthly cost.

## Features

- **Room Rent Calculation**: Allows input of the total rent for the living space.
- **Food Expenses**: Enter the amount spent on shared food orders.
- **Electricity Charges**: Input the total electricity units consumed and the rate per unit to calculate electricity costs.
- **Cost Splitting**: Specify the number of people sharing the expenses to divide the costs equally.

## How It Works

The program calculates the total monthly expenses by adding up the rent, food costs, and calculated electricity charges, then divides the total by the number of roommates to get each person's share.

## Example Usage

Here is the Python code used for the calculation:

```python
# Get input values
rent = int(input("Enter your flat rent: "))
food = int(input("Enter the amount of food ordered: "))
electricity_spend = int(input("Enter the total electricity units spent: "))
charge_per_unit = int(input("Enter the charge per unit: "))
persons = int(input("Enter the number of persons living in room/flat: "))

# Calculate total bill
total_electricity_bill = electricity_spend * charge_per_unit
total_bill = rent + food + total_electricity_bill

# Calculate each person's share
share_per_person = total_bill / persons

# Print the results
print("Total bill =", total_bill)
print("Each person's bill =", share_per_person)
