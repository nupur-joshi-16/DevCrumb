# Swapping Variables
# Swap the values of a and b without using a third variable:

a = 5
b = 10

# Without using third variable. It's a real Python developer way.
a, b = b, a
print(a)
print(b)


# With Using a third variable
c = a
print(c)
a = b
print(a)
b = c
print(b)

