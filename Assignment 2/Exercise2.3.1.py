                        ##Name : Krutika Shah
                        ##date: 10 Aug
                        ##Assignment 2- Exercise 2.3.1

import math
print ("------------Exercise 2.3.1--------------")
def multadd(a,b,c):
    return a*b+c

print ("------------Exercise 2.3.2--------------")
print ("-------------Test Cases:--------------")
angle_test = multadd(math.cos(math.pi/4), 1/2.0, math.sin(math.pi/4))
print "sin(pi/4) + cos(pi/4)/2 is:"
print (angle_test)
ceiling_test = multadd(2, math.log(12,7), math.ceil(279/19.0))
print "ceiling(276/19) + 2 log_7(12) is:"
print ceiling_test

print ("------------Exercise 2.3.3--------------")
def yikes(x):
    return multadd(x, math.exp(-x), math.sqrt(1 - math.exp(-x)))

print ("yikes(5)\n" +str(yikes(5)))
print ("yikes(0)\n" +str(yikes(0)))
print ("yikes(10)\n" +str(yikes(10)))
