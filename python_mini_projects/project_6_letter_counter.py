# Project 6: Letter Counter

# Task:
# Ask the user to enter a word or sentence.
# Count the number of characters (excluding spaces).
# Display the character count.

user_text = input("Please add text: ")
user_text_length = len(user_text.replace(" ", ""))
print(f"{user_text}\n(Total character(s) in above text : {user_text_length})")