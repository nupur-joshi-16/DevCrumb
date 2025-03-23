# Project 8: Simple Word Counter
# Concepts Covered: Strings, User Input, split(), len(), Loops (Optional)

# Task:

# Ask the user to enter a sentence.
# Count the number of words in the sentence.
# Display the word count.
# Hint: Use .split() to break the sentence into words and len() to count them.
# Try it out and let me know if you need a hint!

user_text = input("Please enter a sentence.\n")
print(f"Input: {user_text}")
word_split = user_text.split()
word_count = (len(word_split))
print(f"Output: {word_count} words in your sentence.")







