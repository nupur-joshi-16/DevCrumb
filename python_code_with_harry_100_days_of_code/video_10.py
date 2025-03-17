# User Input in Python

user_name = input("Enter your name: ")
print("User name is", user_name)

num_1 = input("Enter first number: ")
num_2 = input("Enter second number: ")

# Python stores user input as a string. 
# That's why the result of the following code will be: 10 + 20 = 1020
print("Sum of", num_1, "+", num_2, "=", num_1 + num_2)

# If we want the sum of two numbers, we need to explicitly convert the string type to int.
# Result: 10 + 20 = 30
print("Sum of", num_1, "+", num_2, "=", int(num_1) + int(num_2))
