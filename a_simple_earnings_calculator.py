"""A simple console application that help an employer
calculate an employee's earning in a given week."""

name: str = input("Please enter the employee's name:    ").strip().title()
wage: float = float(input("Please enter the employee's hourly wage:    "))
hours: float = float(input("How many hours the employee worked:    "))

earnings: float = wage * hours

print(f"{name} earned ${earnings:.2f} this week")
