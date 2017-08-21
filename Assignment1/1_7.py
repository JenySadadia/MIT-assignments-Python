#Author:Group4
#Rock paper scissors

def check(s):

	if (s=="rock" or s=="scissors" or s=="paper"):
		pass
	else:
		print("This is not a valid object selection")
	

Player1=input("Player1?")
check(Player1)
Player2=input("Player2?")
check(Player2)

if Player1=="rock" and Player2=="rock":
	print("It's a tie !")

elif Player1=="rock" and Player2=="paper":
	print("Player2 wins !")

elif Player1=="rock" and Player2=="scissors":
	print("Player1 wins !")

elif Player1=="scissors" and Player2=="rock":
	print("Player2 wins !")

elif Player1=="scissors" and Player2=="paper":
	print("Player1 wins !")

elif Player1=="scissors" and Player2=="scissors":
	print("It's a tie !")

elif Player1=="paper" and Player2=="rock":
	print("Player1 wins !")

elif Player1=="paper" and Player2=="scissors":
	print("Player2 wins !")

elif Player1=="paper" and Player2=="paper":
	print("It's a tie !")






