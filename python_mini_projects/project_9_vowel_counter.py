# Project 9: Vowel Counter 

# Concepts Covered: Strings, Loops, Conditional Statements  

# Task:
# 1. Ask the user to enter a sentence.  
# 2. Count how many vowels (`a, e, i, o, u`) are in the sentence.  
# 3. Display the total vowel count.  

# Hint: You can loop through the sentence and check if each character is a vowel.  

user_text = input("Please enter a sentence: ")
print(user_text)

# vowel_e = user_text.find("e")
# vowel_i = user_text.find("i")
# vowel_o = user_text.find("o")
# vowel_u = user_text.find("u")
# vowel_a = user_text.find("a")

# print(f"Your sentence is: {user_text} and there are some vowels as per below.\n a = {vowel_a}\n e ={vowel_e}\n i = {vowel_i}")

for i in user_text:
    if user_text.find("u"):
        print("u")
    else:
        print("no")




# user_task_list = []
# a = 1
# user_task = ""
# while user_task != "Done":
#     user_task = input("Please enter a task: ").title()
#     user_task_list.append(f"{a}. {user_task}")
#     a = a + 1

# user_task_list= user_task_list[:-1]