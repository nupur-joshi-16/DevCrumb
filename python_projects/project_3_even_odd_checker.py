# Project 3: Even or Odd Number Checker

# Task:
# Ask the user to enter a number.
# Check if the number is even or odd.
# Print a message displaying the result.

user_number = int(input("Please enter your number: "))

if user_number % 2 == 0:
    print(f"{user_number} is an even number.")
else:
    print(f"{user_number} is an odd number.")
