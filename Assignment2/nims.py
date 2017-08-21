# Name: Group 4
# Date: 11 Aug
# Section: Assingnment 2
# nims.py

def play_nims(pile, max_stones):
    '''
    An interactive two-person game; also known as Stones.
    @param pile: the number of stones in the pile to start
    @param max_stones: the maximum number of stones you can take on one turn
    '''

    ## Basic structure of program (feel free to alter as you please):
    player_turn = 1
    while pile > 0:
        move = 0
        while move < 1 or move > max_stones:
            move = raw_input ("Player(%s) Enter number of stones: " %player_turn)
            move = int(move)
        pile -= move
        if pile < 0:
            print ("Player %s is winner " %player_turn)
        else:
            print ("There are %s Stones remaining: " % pile)

        if player_turn == 1:
            player_turn = 2
        else:
            player_turn = 1

    print "Game over"
play_nims(100,5)
