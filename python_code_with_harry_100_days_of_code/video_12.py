# String Slicing

my_friends = "Ram, Shyam, Bhim, Arjun"
print(my_friends[0:3])  # Includes index 0 to 2, not 3.
print(my_friends[:3])   # If we skip the first number, Python assumes it as 0.
print(my_friends[5:-1]) # -1 refers to the last character, but slicing stops before it.
print(len(my_friends))  # Prints the length of the string.

# Quick quiz
nm = "Harry"
print(nm[-4:-2])  # Output: ar
