# **********  Exercise OPT.1 **********

# Write any helper functions you need here.

VOWELS = ['a', 'e', 'i', 'o', 'u']
Latin_rules = ['th','st','qu','pl','tr']
def pig_latin(word):
        if word[0].lower() in VOWELS:
            return word + "hay"
        elif word[0:2].lower() in Latin_rules:
            return word[2:] + word[0:2] + "ay"
        else:
            return word[1:] + word[0] + "ay"

def pig_latin_sentences():
    while True:
        sentences = ''
        space = ''
        sentence = raw_input("Enter Your Sentence: ")
        if sentence.lower() == "quit":
            break

        sentence_split = sentence.split()
        for word in sentence_split:
            sentences += space + pig_latin(word)
            space = ' '
        print 'Pig Latin Sentence will be like:'
        print sentences
    return

pig_latin_sentences()
