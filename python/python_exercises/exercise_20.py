# Power Calculation
# Ask the user for a base number and an exponent, then calculate the result.

base_number = int(input("Please enter a number: "))
exponent_number = int(input("Enter the exponent (how many times to multiply): "))
power_number = base_number ** exponent_number
print(f"Base Number : {base_number}\nExponent Number : {exponent_number}\n{base_number}^{exponent_number}={power_number}")

#In python we are using ** sign for exponent. But in real we are using ^ sign for exponent calculation