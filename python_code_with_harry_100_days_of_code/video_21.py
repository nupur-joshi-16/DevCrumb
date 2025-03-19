# function arguments

# default arguments




def add_numbers(num_1=1, num_2=1):
    print(num_1, "+", num_2, "=", num_1 + num_2)

add_numbers() #take default parameter
add_numbers(10, 5) #avoide default parameters and take parametaers from here
add_numbers(60) #take first parameter as 60 and second is 1 as default parameter.
add_numbers(num_2=25) #take second value of parameter = 25.


# return statement

student_first_name = input("Please enter your name: ")
student_last_name = input("Please enter your last name: ")
english_marks = float(input("Please enter English marks: "))
maths_marks = float(input("Please enter maths marks: "))
science_marks = float(input("Please enter science marks: "))
total_marks = english_marks + maths_marks + science_marks

def marks_percentage(total_marks):
    return((total_marks / 300)*100)


student_percentage = marks_percentage(total_marks)
formatted_num = "%.2f" % student_percentage
print(student_first_name, student_last_name, "percentage :", formatted_num)

