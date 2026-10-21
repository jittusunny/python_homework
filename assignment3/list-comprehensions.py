import csv

# Task 3.1: Read employees.csv into a list of lists
with open("../csv/employees.csv", "r", newline="") as file:
    reader = csv.reader(file)
    employees = list(reader)

# Task 3.2: Create a list of employee names, skipping the header
names = [
    employee[0] + " " + employee[1]
    for employee in employees[1:]
]
print(names)

# Task 3.3: Create a list of names containing the letter "e"
names_with_e = [name for name in names if "e" in name]
print(names_with_e)