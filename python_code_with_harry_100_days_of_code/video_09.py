# Type casting

a = "1"
b = "2"
print(a + b)  # String Concatenation. Result = "12"
print(int(a) + int(b))  # Converted String to integer using int function. Result = 3

# str(), ord(), hex(), oct(), tuple(), set(), list(), dict(), etc. functions or methods

# Explicit conversion or type casting - I (the developer) will convert manually.
# Implicit conversion or type casting - Python will change automatically.

c = 1.5
d = 10
print(c + d)  # Implicit type conversion: int to float.
