#!/usr/bin/env python3

# Water Bill Calculation

# Input current consumption
consumption = int(input("Enter your current consumption in cubic meter:"))

# Calculate basic charge
basic_charge = consumption * 41.66

# Calculate value-added tax
value_added_tax = basic_charge * .12 

# Apply residential discount
residential_discount = 10
total_current_bill = (basic_charge + value_added_tax) - residential_discount

# Other Charges
meter_maintainance_fee = 10
septage_fee = 88.13
reconnection_fee = 0.00
promissory_note_amount = 0.00
penalty_balance = 0.00

# Calculate total amount due
total_amount_due = total_current_bill + meter_maintainance_fee + septage_fee


print(round(total_amount_due, 2))
