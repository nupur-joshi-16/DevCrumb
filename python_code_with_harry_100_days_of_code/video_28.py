# f-strings in Python

# Problem : The below writing method is not incorrect or there is no problem with this code. But this is not convinient way to writing below code
letter = "Hey my name is {0} and I am from {1}"
print(letter)
country = "India"
name = "Nupur"
print(letter.format(name, country))

# Solution : f-strings
print(f"Hey my name is {name} and I am from {country}")
# We can put directly variable names inside f-string.

price = 80.679321
print(f"Price: {price:.2f}")

print(f"This is Curly brackets sign {{}}.")