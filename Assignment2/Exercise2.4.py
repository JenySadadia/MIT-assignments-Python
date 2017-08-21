##Author : Group 4
##Assingnment 2

## --------------------Exercise 2.4.1--------------
import math
import random

def rand_divis_3():
    number = random.randint(0,100)
    print ("number: " +str(number))

    if number%3 == 0:
        return True
    else:
        return False

print rand_divis_3()

#---------------------------Exercise 2.4.2----------------------
print ("Random die print for three times")
def roll_dice(sides, dice):
    while dice>0:
        dice -= 1
        print random.randint(1,sides)
    return ("That's all!")
        
print (roll_dice(6,3))
print (roll_dice(4,4))
print (roll_dice(10,2))

