phrase=input("Enter a phrase to encode")
shift=int(input("Enter a shift value"))

encoded_phrase=""

for c in phrase:

	if c.isupper():
		a=(ord(c)+shift)

		if a>90:
			a-=26
		elif a<65:
			a+=26
		encoded_phrase=encoded_phrase+chr(a%90)

	elif c.islower():
		a=(ord(c)+shift)

		if a>122:
			a-=26
		elif a<97:
			a+=26
		encoded_phrase=encoded_phrase+chr(a%122)

	else:
		encoded_phrase=encoded_phrase+c

print(encoded_phrase)