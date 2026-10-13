# Task 2 Read a CSV File

import csv
import custom_module

def read_employees():
    employee_dict = {}
    rows = []

    try:
        with open("../csv/employees.csv", "r") as file:
            reader = csv.reader(file)

            first_row = True

            for row in reader:
                if first_row:
                    employee_dict["fields"] = row
                    first_row = False
                else:
                    rows.append(row)

            employee_dict["rows"] = rows

    except Exception as e:
        print(f"Error reading employees: {e}")

    return employee_dict


employees = read_employees()
print(employees)

# Task 3 Find the Column Index
def column_index(column_name):
    return employees["fields"].index(column_name)


employee_id_column = column_index("employee_id")
print(employee_id_column)


# Task 4: Get the index of the "name" column
def first_name(row_number):
    first_name_column = column_index("first_name")
    return employees["rows"][row_number][first_name_column]
print(first_name(0))

# Task 5: Get the index of the "last_name" column
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    matches = list(filter(employee_match, employees["rows"]))
    return matches
#  Task6  Find the Employee with a Lambda
def employee_find_2(employee_id):
    matches = list(
        filter(
            lambda row: int(row[employee_id_column]) == employee_id,
            employees["rows"],
        )
    )
    return matches
#Task7  Sort the Rows by last_name Using a Lambda
def sort_by_last_name():
    last_name_column = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[last_name_column])
    return employees["rows"]
#task8  Create a dict for an Employee
def employee_dict(row):
    result = {}

    for field, value in zip(employees["fields"], row):
        if field != "employee_id":
            result[field] = value

    return result

#print(employee_dict(employees["rows"][0])) 

#Task9 A dict of dicts, for All Employees

def all_employees_dict():
    result = {}
    id_index = employees["fields"].index("employee_id")

    for row in employees["rows"]:
        employee_id = row[id_index]
        result[employee_id] = employee_dict(row)

    return result


    # print(all_employees_dict()

# Task 10 Use the os Module
import os


def get_this_value():
    return os.getenv("THISVALUE")


# Test the function.
print(get_this_value())

# Task 11 Creating Your Own Module
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)


set_that_secret("my new secret")
print(custom_module.secret)



# Task 12: Read minutes1.csv and minutes2.csv

def read_csv(filename):
    minutes_dict = {}
    rows = []

    with open(filename, "r") as file:
        reader = csv.reader(file)
        first_row = True

        for row in reader:
            if first_row:
                minutes_dict["fields"] = row
                first_row = False
            else:
                rows.append(tuple(row))

        minutes_dict["rows"] = rows

    return minutes_dict


def read_minutes():
    minutes1 = read_csv("../csv/minutes1.csv")
    minutes2 = read_csv("../csv/minutes2.csv")

    return minutes1, minutes2


minutes1, minutes2 = read_minutes()

print(minutes1)
print(minutes2)

# Task 13 Create minutes_set
def create_minutes_set():
    minutes1_set = set(minutes1["rows"])
    minutes2_set = set(minutes2["rows"])

    return minutes1_set.union(minutes2_set)


minutes_set = create_minutes_set()

# Task 14: Convert to datetime

from datetime import datetime


def create_minutes_list():
    minutes_list = list(minutes_set)

    minutes_list = list(map(
        lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")),
        minutes_list
    ))

    return minutes_list


minutes_list = create_minutes_list()

# Task 15: Write Out Sorted List

def write_sorted_list():
    minutes_list.sort(key=lambda x: x[1])

    converted_list = list(map(
        lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")),
        minutes_list
    ))

    with open("./minutes.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"])
        writer.writerows(converted_list)

    return converted_list


sorted_minutes = write_sorted_list()
print(sorted_minutes)


