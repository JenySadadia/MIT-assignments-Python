import math
def roots(a,b,c):
    eq = (b*b)-(4*a*c)
    if eq < 0:
        print "error: complex roots"

    else:
        root1 = -b/(2.0*a) + math.sqrt(eq)
        root2 = -b/(2.0*a) - math.sqrt(eq)
        print "Roots are: \nRoot1 is: " +str(root1)+"  \nRoot2 is: " +str(root2)

#Test Cases
roots(1,2,1)
roots(5,-1,-2)
