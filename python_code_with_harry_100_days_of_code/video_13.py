# String Methods in Python

my_friends = "Ram, Shyam, Bhim, Arjun"

# Strings are immutable in Python

print(my_friends.upper())  # Uppercase method
print(my_friends.lower())  # Lowercase method

best_friend = "He said, \"You\'re my best friend!!!!!\""
print(best_friend)
print(best_friend.rstrip("!"))  # Won't work as '!' isn't the last character

hey = "Hey!!!!!!!!"
print(hey.rstrip("!"))  # Removes trailing "!"

print(my_friends.replace(", ", " -"))  # Replaces ', ' with ' -'
print(my_friends.split(", "))  # Splits the string into a list

print(my_friends.capitalize())  # First character uppercase, rest lowercase
print(my_friends.center(50))  # Centers text in a 50-character space
print(my_friends.count(","))  # Counts occurrences of ","
print(my_friends.endswith("n"))  # Checks if string ends with "n"
print(my_friends.endswith("!"))  # Checks if string ends with "!"
print(my_friends.endswith("am", 2, 10))  # Checks if substring "am" appears between index 2 and 10

print(my_friends.find("i"))  # Returns index of first occurrence of "i"
print(my_friends.find("z"))  # Returns -1 as "z" is not found

# print(my_friends.index("z"))  # Raises an exception because "z" is not found
print(my_friends.index("a"))  # Returns index of first occurrence of "a"

print(my_friends.isalnum())  # Checks if the string is alphanumeric (False because of spaces & commas)
print(my_friends.isalpha())  # Checks if the string contains only letters (False because of spaces & commas)
print(my_friends.islower())  # Checks if all letters are lowercase
print(my_friends.isprintable())  # Checks if all characters are printable
print(my_friends.isspace())  # Checks if string contains only spaces
print(my_friends.istitle())  # Checks if each word starts with uppercase
print(my_friends.isupper())  # Checks if all letters are uppercase
print(my_friends.startswith("R"))  # Checks if string starts with "R"
print(my_friends.swapcase())  # Swaps uppercase to lowercase and vice versa
print(my_friends.title())  # Converts string to title case
