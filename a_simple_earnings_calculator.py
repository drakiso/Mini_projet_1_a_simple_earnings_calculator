"""A simple console application that help an employer
calculate an employee's earning in a given week."""

employee_s_name: str = input("Please enter the employee's name:    ").strip().title()
hourly_wage: float = float(input("Please enter the employee's hourly wage:    "))
worked_hours: float = float(input("How many hours the employee worked:    "))

employee_s_earnings: float = hourly_wage * worked_hours

print(f"{employee_s_name} earned ${employee_s_earnings:.2f} a week")
