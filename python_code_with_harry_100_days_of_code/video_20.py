# Functions

# built in functions

# Here’s a list of commonly used built-in functions in Python:  

# 1. `print()`  
# 2. `input()`  
# 3. `len()`  
# 4. `type()`  
# 5. `int()`  
# 6. `float()`  
# 7. `str()`  
# 8. `list()`  
# 9. `dict()`  
# 10. `set()`  
# 11. `tuple()`  
# 12. `range()`  
# 13. `abs()`  
# 14. `round()`  
# 15. `min()`  
# 16. `max()`  
# 17. `sum()`  
# 18. `sorted()`  
# 19. `reversed()`  
# 20. `enumerate()`  
# 21. `zip()`  
# 22. `map()`  
# 23. `filter()`  
# 24. `any()`  
# 25. `all()`  
# 26. `chr()`  
# 27. `ord()`  
# 28. `bin()`  
# 29. `hex()`  
# 30. `id()`  
# 31. `isinstance()`  
# 32. `dir()`  
# 33. `help()`  
# 34. `eval()`  
# 35. `exec()`  



user_age = int(input("Please enter your age: "))
print("Your age is", user_age)


def isDrive(user_age):
    if(user_age >= 18):
        print("You can drive")
    else:
        print("You can not drive")

isDrive(user_age)



num_1 = int(input("Please enter first number: "))
num_2 = int(input("Please enter second number: "))

def add_numbers(num_1, num_2):
    print(num_1, "+", num_2, "=", num_1 + num_2)

add_numbers(num_1, num_2)