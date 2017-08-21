print 'Exercise OPT.2 : List comprehension Challenges(tricky!)'

print '(1)'
print 'find integer number from list:'
def int_element(lists):
    return [element for element in lists if isinstance(element, int)]

lists = [52,53.5,"grp4",65,42,35]
print int_element(lists)

print '(2)'
print 'Here the y = x*x + 1 and [x,y] will be:'
print ([[x,x*x+1] for x in range(-5,6) if 0 <= x*x + 1 <=10])

print '(3)'
print 'The posible solutions for [x,y] with radious 5'
print ([[x,y] for x in range (-5,6) for y in range(-5,6) if x*x + y*y == 25])

print '(4)'
print 'List comprehension for Celsius to Fahrenheit'
celsius = [22,28,33,35,42,52]
print ([fahrenhit *(9/5) + 32 for fahrenhit in celsius])
