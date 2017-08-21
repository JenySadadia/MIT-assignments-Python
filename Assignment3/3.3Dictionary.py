D={}  #Creates new empty dictionary
def add_class(class_no,desc):  #method for adding values in dictionary
    D[class_no]=desc
def print_classes(course_no): #display values of specified course id
    if course_no not in D:
        print("Data not Found!")
    else:
            print(D[course_no])
add_class(12,"python1")
add_class(13,"python2")
add_class(14,"python3")
print_classes(12)