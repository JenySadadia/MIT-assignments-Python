# Name: Group 4
# Section: Assignment 2
# strings_and_lists.py

# **********  Exercise 2.8 **********

def report_card(class_grade):
    record = 0.0
    for i in class_grade:
        record = record + i
    return float(record / len(class_grade))
   
class_name = []
class_grade = []
classes = int(raw_input('How many classes did you take?'))
number = classes
while classes > 0:
    classes -= 1
    name = raw_input('What was the name of this class?  ')
    grade = int(raw_input ('What was your grade? '))
    class_name.append(name)
    class_grade.append(grade)

print "Record Card"
for i in range(number):
    print class_name[i], " - " , class_grade[i]

print "Overall GPA: ", report_card(class_grade)


