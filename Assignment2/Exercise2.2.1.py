print ("------------------Exercise:2.2(.1)------------------")
print ("Program to check m is divisible by n or not")
m = int(raw_input("Enter your m value: "))         # initialize m value    
n = int(raw_input("Enter your n value: "))         # initialize n value

def is_divisible(m,n):              #function defination
    if (n == 0):
        return False
    elif (m % n == 0):
        return True
    else:
        return False

result = is_divisible(m,n)#call the function
print (result)

##print ("Test Cases:")
##print (is_divisible(4,2)) #True
##print (is_divisible(3,4)) #False
##print (is_divisible(52,42)) #False
##print (is_divisible(100,10)) #True
##print (is_divisible(100,0))
