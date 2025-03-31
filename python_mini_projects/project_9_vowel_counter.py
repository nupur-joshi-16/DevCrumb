# Project 9: Vowel Counter 

# Concepts Covered: Strings, Loops, Conditional Statements  

# Task:
# 1. Ask the user to enter a sentence.  
# 2. Count how many vowels (`a, e, i, o, u`) are in the sentence.  
# 3. Display the total vowel count.  

# Hint: You can loop through the sentence and check if each character is a vowel.  

user_text = input("Please enter a sentence: ")
print(user_text)

vowels = {"a", "e", "i", "o", "u"}
count = 0
for char in user_text:
    if char in vowels:
        count = count + 1

print(f"Your sentence is: {user_text}\nTotal vowels in your sentence are: {count}")