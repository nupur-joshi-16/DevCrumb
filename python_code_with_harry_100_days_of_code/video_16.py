# Match case statement
day = input("Please enter today's day: ").lower()
# day_lower = day.lower()
# print(day_lower)

match day:
    case "monday":
        print("Monday is dedicated to Lord Shiva.")
    case "tuesday":
        print("Tuesday is dedicated to Lord Ganesha.")
    case "wednesday":
        print("Wednesday is dedicated to planet Mercury and an incarnation of Krishna.")
    case "thursday":
        print("Thursday is dedicated to Lord Vishnu.")
    case "friday":
        print("Friday is dedicated to Goddess Mahalaxmi.")
    case "saturday":
        print("Saturday is dedicated to alleviating the bad influence of Lord Shani.")
    case "sunday":
        print("Sunday is dedicated to Lord Surya (the Sun God).")
    case _:
        print("Enter a valid day.")


