# Project 5: Word Repeater

# Task:
# Ask the user for a word.
# Ask the user how many times they want to repeat it.
# Print the word that many times.

user_text = input("Please enter your text: ")
new_line = "\n"
repeat_text = int(input("Enter how many times you want to repeat: "))

print(f"{(user_text + new_line) * repeat_text}")