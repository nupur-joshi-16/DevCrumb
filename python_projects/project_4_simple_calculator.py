# Project 4: Simple Calculator

# Task:
# Ask the user for two numbers.
# Ask the user for an operation (+, -, *, /).
# Perform the calculation and display the result.

first_number = int(input("Enter your first number: "))
second_number = int(input("Enter your second number: "))
choose_operation = input("Enter your prefer opration: ")

if choose_operation == "+":
    print(f"{first_number + second_number}")
elif choose_operation == "-":
    print(f"{first_number - second_number}")
elif choose_operation == "*":
    print(f"{first_number * second_number}")
elif choose_operation == "/":
    print(f"{first_number / second_number}")
else:
    print("Choose valid operation.")


