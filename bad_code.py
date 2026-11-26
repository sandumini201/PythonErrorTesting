
import os
import sys
import random

# 1. Hardcoded password
ADMIN_PASSWORD = "Admin12345"

# 2. Unused variable
unused_variable = 100

# 3. Unused import
import math


# 4. Function with unused parameter
def calculate_total(price, quantity, discount):
    total = price * quantity
    return total


# 5. Possible division by zero
def calculate_average(marks):
    return sum(marks) / len(marks)


# 6. Incorrect comparison with None
def check_user(username):
    if username == None:
        print("Username missing")
    else:
        print("Welcome", username)


# 7. Bare except
def read_file(filename):
    try:
        file = open(filename, "r")
        return file.read()
    except:
        pass


# 8. Dangerous use of eval
def calculate_expression(expression):
    return eval(expression)


# 9. Duplicate code
def calculate_tax(price):
    tax = price * 0.15
    return tax


def calculate_service_charge(price):
    charge = price * 0.15
    return charge


# 10. Incorrect password validation
def login(username, password):
    if password == ADMIN_PASSWORD:
        print("Login successful")
    else:
        print("Login successful")


# 11. Infinite loop risk
def process_numbers():
    number = 10

    while number > 0:
        print(number)


# 12. Mutable default argument
def add_student(name, students=[]):
    students.append(name)
    return students


# 13. Unsafe command execution
def run_command(command):
    os.system(command)


# 14. Unnecessary condition
def check_age(age):
    if age >= 18:
        if age >= 18:
            print("Adult")


# 15. Incorrect resource handling
def write_file(filename, content):
    file = open(filename, "w")
    file.write(content)


# 16. Main program
def main():
    print("Python Code Quality Testing")

    print(calculate_total(100, 2, 10))

    print(calculate_average([80, 90, 70]))

    check_user(None)

    print(calculate_tax(1000))

    print(calculate_service_charge(1000))

    login("admin", "wrongpassword")


if __name__ == "__main__":
    main()
