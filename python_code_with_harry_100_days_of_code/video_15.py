# Exercise : Good morning

import time

time_stamp = time.strftime('%H:%M:%S')
# print(time_stamp)
time_hour = int(time.strftime('%H'))
time_min = int(time.strftime('%M'))
time_sec = int(time.strftime('%S'))
# print(time_hour,time_min, time_sec)


if 0 <= time_hour < 12:
    print("Good morning")
elif 12 <= time_hour < 17:
    print("Good afternoon")
elif 17 <= time_hour < 21:
    print("Good evening")
else:
    print("Good night")