#Author:Group4
#Rock paper scissors

def check(s):

	if (s=="rock" or s=="scissors" or s=="paper"):
		pass
	else:
		print("This is not a valid object selection")
	

def result(player1,player2):
        if Player1=="rock" and Player2=="rock":
                return ("It's a tie !")

        elif Player1=="rock" and Player2=="paper":
                return("Player2 wins !")

        elif Player1=="rock" and Player2=="scissors":
                return("Player1 wins !")

        elif Player1=="scissors" and Player2=="rock":
                return("Player2 wins !")

        elif Player1=="scissors" and Player2=="paper":
                return("Player1 wins !")

        elif Player1=="scissors" and Player2=="scissors":
                return("It's a tie !")

        elif Player1=="paper" and Player2=="rock":
                return("Player1 wins !")

        elif Player1=="paper" and Player2=="scissors":
                return("Player2 wins !")

        elif Player1=="paper" and Player2=="paper":
                return("It's a tie !")

Player1=raw_input("Player1?")
check(Player1)
Player2=raw_input("Player2?")
check(Player2)
result = result(Player1,Player2)
print result







