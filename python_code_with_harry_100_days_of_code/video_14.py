# if else conditional statements in python
# if elif else

# conditional operators
# >, <, >=, <=, ==, !=

# Returns boolean value

user_age = int(input("Please enter your age: "))
print("Your age is", user_age)

if(user_age >= 18):
    print("You can drive")
else:
    print("You can not drive")

num = int(input("please enter number: "))
if(num < 0):
    print("Number is negative")
elif(num == 0):
    print("Number is zero")
else:
    print("Number is positive number")
