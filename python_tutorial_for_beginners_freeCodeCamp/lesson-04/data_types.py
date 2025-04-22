import math
# String data type

# literal assignments
first = "Nupur"
last = "Joshi"

# print(type(first))
# print(type(first)==str)
# print(isinstance(first, str))

# constructor function
# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza)==str)
# print(isinstance(pizza, str))

# Concatination
# fullName = first + ' ' + last
# print(fullName)
# fullName += "!"
# print(fullName)

# Casting a number to a string
# decade = str(1980)
# print(type(decade))
# print(decade)

# statement = "I like rock music from the " + decade + "s."
# print(statement)

# Multiple lines
multiline = '''
# Hey, how are you?

# I was just checking in.

#                 All good?

# '''

# print(multiline)


# Escaping special characters
# sentence = 'I\'m back at work!\tHey!\n\nWhere\'s at\\located'
# print(sentence)

# String methods
# print(first)
# print(first.lower())
# print(first.upper())
# print(first)

# print(multiline.title())
# print(multiline.replace("good", "ok"))

# print(len(multiline))
# multiline += "                        "
# print(len(multiline))
# multiline = "                         " + multiline
# print(len(multiline))

# print(len(multiline.strip()))
# print(multiline)

# Build a menu
# title = "menu".upper()
# print(title.center(20, "="))
# print("Cofee".ljust(16, ".") + "$1".rjust(0))
# print("Muffin".ljust(16, ".") + "$2".rjust(0))
# print("Cheesecake".ljust(16, ".") + "$4".rjust(0))
# print("")

# String index values
print(first[0])
print(first[-1])
print(first[2:-1])
print(first[2:])

# Some methods return boolean data
print(first.startswith("N"))
print(first.endswith("u"))

# Boolean data type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))


# Numeric data types

# Integer type

price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# float type
gpa = 3.28
y = float(1.14)
print(type(gpa))


# complex type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built-in functions for numbers
print(abs(gpa))
print(round(gpa))
print(round(gpa, 1))

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# Casting a string to a number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))

# Error if you attempt to cast incorrect data
# zip_value = int("New York")