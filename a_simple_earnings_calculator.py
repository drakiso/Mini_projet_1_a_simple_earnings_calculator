"""A simple console application that help an employer
calculate an employee's earning in a given week."""

name = input("Please enter the employee's name:    ").strip().title()
wage = float(input("Please enter the employee's hourly wage:    "))
hours = float(input("How many hours the employee worked:    "))

earnings = wage * hours

print(f"{name} earned ${earnings:.2f} this week")