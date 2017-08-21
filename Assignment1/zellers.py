A=int(input("Enter month of the year"))
B=int(input("Enter day of the month "))
C=int(input("Enter the year of the centuary"))
D=int(input("Enter the centuary"))

if A==11 or A==12:
	C=-1

W=(13*A-1)/5
X=C/4
Y=D/4
Z=W+X+Y+B+C-2*D
R=Z%7

print(int(R))