# Simple Interest Calculator
# Take Principal, Rate, and Time from the user and calculate simple interest using the formula: SI = (Principle * Interest_Rate * Time ) / 100
# import math
# print("Interest Calculator")
# principle_amount = int(input("Enter Your Principle Amount to invest: "))
# print(principle_amount)
# rate_of_interest = int(input("Enter Rate of Interest: "))
# print(rate_of_interest)
# time_period = math.floor(int(input("Enter time period (in Year): ")))
# print(time_period)
# simple_interest = (principle_amount * rate_of_interest * time_period) / 100
# print(f"Principle Amount: {principle_amount}\nRate of Interest(p.a.): {rate_of_interest}%\nTime Period: {time_period} year\nSimple Interest is : {simple_interest}")

print("This is an Interest Calculator")
principle_amount = float(input("Enter Your Principle Amount to invest: "))
rate_of_interest = float(input("Enter Rate of Interest: "))
time_period = float(input("Enter time period (in Year): "))
print(time_period)
simple_interest = (principle_amount * rate_of_interest * time_period) / 100
print(f"Principle Amount: {principle_amount}\nRate of Interest(p.a.): {rate_of_interest}%\nTime Period: {time_period} year\nSimple Interest is : {simple_interest}")
