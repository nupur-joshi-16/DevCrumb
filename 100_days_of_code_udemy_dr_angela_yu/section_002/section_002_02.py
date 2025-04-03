# Type error, type checking and type conversion

# len() function is not working on numbers. It will show an type error.
# len(12345)

# type operator
print(type("hi"))
print(type(123))
print(type(123.45))
print(type(True))

# Type conversion or type casting
print("2" + "3") #23
print(int("2") + int("3")) #5
# print(int("abc")) We can't conver string to integer. It wii give ValueError.


# Make this line of code run without errors
# print("Number of letters in your name: " + len(input("Enter your name")))

print("Number of letters in your name: " + str(len(input("Enter your name: "))))