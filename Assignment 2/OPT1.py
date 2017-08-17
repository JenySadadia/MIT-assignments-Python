# **********  Exercise 2.9 **********

# Write any helper functions you need here.

VOWELS = ['a', 'e', 'i', 'o', 'u']
def pig_latin(word):
    for i in range (0,len(VOWELS)):
        if word[0] == VOWELS[i]:
            return "%s%s" % (word,"hay")
        else:
            b = word[1:] + word[0]
            return "%s%s" % (b,"ay")
    
word = raw_input("Enter Your word:")
print pig_latin(word)
