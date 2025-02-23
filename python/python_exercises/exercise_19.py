# Swap Two Numbers (Using a Temporary Variable)
# Take two numbers from the user and swap their values.

user_input_1 = input("Enter your favorite number: ")
user_input_2 = input("Enter your second favorite number: ")

temp_value = user_input_1
user_input_1 = user_input_2
user_input_2 = temp_value

print(f"After swapping, your first favorite number is {user_input_1} and second favorite number is {user_input_2}")
