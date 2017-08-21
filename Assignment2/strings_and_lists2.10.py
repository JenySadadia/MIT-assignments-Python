
# **********  Exercise 2.10 **********

print "list comprehension to print a list of cubes of 1 to 10 numbers"
lists = [x ** 3 for x in range(1,11)]
print lists

print
print "List comprehension for coin flip"
print [x + y for x in ('h','t') for y in ('h','t')]

print
print "Print all the vowels in string"
vowel = ['a','e','i','o','u']
def find_vowel(string):
    return [x for x in string if x in vowel]
string = raw_input("Enetr your String")
print find_vowel(string)


# **********  Exercise OPT.1 **********
# If you do any work for this problem, submit it here 

