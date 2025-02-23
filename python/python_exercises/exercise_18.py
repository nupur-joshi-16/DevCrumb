# Find the Greatest Number
# Ask the user for three numbers and find the largest among them.

# print("Find the largest number")
# num_1 = int(input("Write your number: "))
# num_2 = int(input("Write your number: "))
# num_3 = int(input("Write your number: "))

# if num_1 > num_2 and num_1 > num_3:
#     print("num_1 is largest")
# elif num_2 > num_1 and num_2 > num_3:
#     print("num_2 is largest")
# elif num_3 > num_1 and num_3 > num_2:
#     print("Num_3 is largest")
# else:
#     print("All numbers are equal")

print("This is an Auction Fun Game.\nPlace your blind bid and win iPhone 16 Pro.")
print("--------------------")

player_1 = input("Enter your username : ")
player_1_bid = int(input("Enter your bid amount: "))
print("--------------------")
player_2 = input("Enter your username : ")
player_2_bid = int(input("Enter your bid amount: "))
print("--------------------")
player_3 = input("Enter your username : ")
player_3_bid = int(input("Enter your bid amount: "))
print("--------------------")


# if player_1_bid > player_2_bid and player_1_bid > player_3_bid:
#     print(f"{player_1} bid: {player_1_bid}\n{player_2} bid: {player_2_bid}\n{player_3} bid: {player_3_bid}")
#     print(f"{player_1} places the highest bid and wins an iPhone 16 Pro! 📱 Congratulations! 🎊🌟")
# elif player_2_bid > player_1_bid and player_2_bid > player_3_bid:
#     print(f"{player_1} bid: {player_1_bid}\n{player_2} bid: {player_2_bid}\n{player_3} bid: {player_3_bid}")
#     print(f"{player_2} places the highest bid and wins an iPhone 16 Pro! 📱 Congratulations! 🎊🌟")
# elif  player_3_bid >  player_1_bid and  player_3_bid >  player_2_bid:
#     print(f"{player_1} bid: {player_1_bid}\n{player_2} bid: {player_2_bid}\n{player_3} bid: {player_3_bid}")
#     print(f"{player_3} places the highest bid and wins an iPhone 16 Pro! 📱 Congratulations! 🎊🌟")
# else:
#     print("All numbers are equal")


def my_function():
  print(f"{player_1} bid: {player_1_bid}\n{player_2} bid: {player_2_bid}\n{player_3} bid: {player_3_bid}")
  print("--------------------")
  
if player_1_bid > player_2_bid and player_1_bid > player_3_bid:
    my_function()
    print(f"{player_1} places the highest bid and wins an iPhone 16 Pro! 📱 Congratulations! 🎊🌟")
elif player_2_bid > player_1_bid and player_2_bid > player_3_bid:
   my_function()
   print(f"{player_2} places the highest bid and wins an iPhone 16 Pro! 📱 Congratulations! 🎊🌟")
elif  player_3_bid >  player_1_bid and  player_3_bid >  player_2_bid:
   my_function()
   print(f"{player_3} places the highest bid and wins an iPhone 16 Pro! 📱 Congratulations! 🎊🌟")
else:
    print("All numbers are equal")