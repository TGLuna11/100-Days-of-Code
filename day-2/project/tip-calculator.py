# Final project for day 2: Tip Calculator
# This project is a tip calculator that asks the user for the total bill,
# the tip percentage, and the number of people to split the bill with.
# It then calculates the total bill, and the amount each person should pay.

print("Welcome to the Tip Calculator")
# Asks the user for the total bill, tip percentage, and the number of people to split the bill with.
bill = float(input("What was the total bill? £"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))

# Calculates the tip amount, total bill, and the amount each person should pay.
tip_amount = bill * (tip_percentage / 100)
total = bill + tip_amount
total_per_person = total / number_of_people

print(f"The total bill is £{total:.2f}\nEach person should pay £{total_per_person:.2f}")
