print("This is an Interest Calculator")
principle_amount = float(input("Enter Your Principle Amount to invest: "))
rate_of_interest = float(input("Enter Rate of Interest: "))
time_period = float(input("Enter time period (in Year): "))
print(time_period)
simple_interest = (principle_amount * rate_of_interest * time_period) / 100
print(f"Principle Amount: {principle_amount}\nRate of Interest(p.a.): {rate_of_interest}%\nTime Period: {time_period} year\nSimple Interest is : {simple_interest}")