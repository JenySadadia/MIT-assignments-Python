"""
Program to create diction whose keys are the name and values are age of the person.
"""
name = ['Alice', 'Bob', 'Cathy', 'Dan', 'Ed', 'Frank','Gary', 'Helen', 'Irene', 'Jack', 'Kelly', 'Larry']
age= [20, 21, 18, 18, 19, 20, 20, 19, 19, 19, 22, 19]
data={}
for i in range(len(age)):
    data[name[i]]=age[i]

#Function which give the age as argument and print the name of persons whose
#age is same as argument
def people(ag):
    for nm in data.keys():
        if(ag==data[nm]):
            print(nm)

ag=int(input("Enter age : "))
people(ag)

