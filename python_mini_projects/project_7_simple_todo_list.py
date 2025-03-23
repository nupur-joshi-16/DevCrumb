# Project 5 (Original): Simple To-Do List
# Concepts Used: lists, append(), loops, input, print, f-strings

# Task:
# Allow the user to add tasks to a list.
# Display all tasks when the user is done.

# Enter a task (or type 'done' to finish): Buy groceries  
# Enter a task (or type 'done' to finish): Complete Python project  
# Enter a task (or type 'done' to finish): done  

# Your To-Do List:  
# 1. Buy groceries  
# 2. Complete Python project  

user_task_list = []
a = 1
user_task = ""
while user_task != "Done":
    user_task = input("Please enter a task: ").title()
    user_task_list.append(f"{a}. {user_task}")
    a = a + 1

user_task_list= user_task_list[:-1]

# Print tasks one by one
for task in user_task_list:
    print(task)
