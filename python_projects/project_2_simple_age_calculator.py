# Project 2: Simple Age Calculator

# Task:
# Ask the user for their birth year.
# Calculate their age.
# Print a message displaying their age.

import datetime

birth_year = int(input("Please enter your birth year: "))
date_today = datetime.datetime.now()
user_age = date_today.year - birth_year
print(f"You are {user_age} years old!")
