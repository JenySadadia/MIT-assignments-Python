#Author:Group4
#Loops

#Part1
for i in range(1,11):
	print(1/i)

#Part2
n=int(input("Enter a number"))

if n<0:
	print("Enter a positive number")

else:
	while n>0:
		print(n)
		n-=1

#Part3
base=int(input("Enter the base"))
exp=int(input("Enter the exponential"))
print(base**exp)

#Part4
while True:
	num=int(input("Enter a number"))

	if (num%2)==0:
		print("Congrats ! You entered an even number")
		break

	elif (num%2)!=0:
		print("It's not an even number")

	
