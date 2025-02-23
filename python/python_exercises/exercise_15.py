# Find Remainder (Modulo Operator)
# Ask the user for two numbers and print the remainder when the first number is divided by the second.
# import math

# first_number = int(input("Please enter a number: "))
# second_number = int(input("Please enter a another number: "))
# quotient = math.floor(first_number / second_number)
# print(quotient)
# remainder = first_number - (second_number * quotient)
# print(f"You have enter first number is: {first_number} and second number is: {second_number} and\nremainder is: {remainder}")

first_number = int(input("Please enter a number: "))
second_number = int(input("Please enter a another number: "))
remainder = first_number % second_number
print(f"You have enter first number is: {first_number} and second number is: {second_number} and\nremainder is: {remainder}")