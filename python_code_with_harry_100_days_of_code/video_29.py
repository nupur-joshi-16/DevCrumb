# docstrings & PEP-8

student_first_name = input("Please enter your name: ")
student_last_name = input("Please enter your last name: ")
english_marks = float(input("Please enter English marks: "))
maths_marks = float(input("Please enter maths marks: "))
science_marks = float(input("Please enter science marks: "))
total_marks = english_marks + maths_marks + science_marks

def marks_percentage(total_marks):
    '''This is a student percentage calculator function. I am taking student_first_name, student_last_name, english_marks, maths_marks, science_marks and store them in total_marks variable. This function returns student percentage. '''
    return((total_marks / 300)*100)


student_percentage = marks_percentage(total_marks)
formatted_num = "%.2f" % student_percentage
print(student_first_name, student_last_name, "percentage :", formatted_num)

print(marks_percentage.__doc__)

# docstrings is not a comment. Python specially treats docstrings.
# docstrings must write above function defination otherwise it will not work.


# PEP8 - I will explore this later in detail.

