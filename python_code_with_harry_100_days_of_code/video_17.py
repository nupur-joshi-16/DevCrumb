# Loops in Python

my_name = "Nupur"

#for loop
for i in my_name:
    print(i)
    if i == "r":
        print("r is the last letter in this name.")


colors = ["Red", "Green", "Blue", "Yellow"]

for color in colors:
    print(color)
    for i in color:
        print(i)

#range function

for n in range(5):
    print(n)

for n in range(1, 11):
    print(n)

# Need to explore step argument.

for n in range(1, 100, 4):
    print(n)