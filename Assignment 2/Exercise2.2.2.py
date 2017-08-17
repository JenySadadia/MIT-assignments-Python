##Name : Krutika Shah
##date: 10 Aug
##Assignment 2.2.2
print ("------------------Exercise:2.2(.2)------------------")
def not_equal(number1,number2):
    if number1 == number2:
        return False
    else:
        return True

number1 = int(raw_input('Enter first number: '))
number2 = int(raw_input('Enter second number: '))

result = not_equal(number1, number2)
print result
