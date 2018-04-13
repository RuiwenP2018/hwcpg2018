import random


def roll(beginning,end):
	return random.randint(beginning,end)

def roundWinner(rollResult1,rollResult2):
	if(rollResult1 > rollResult2):
		return "Player 1 Wins the Round"
	elif(rollResult2 > rollResult1):
		return "Player 2 Wins the Round"
	else:
		return "Tie and Re-roll"

def gameWinner(score1,score2):
	if(score1 > score2):
		return "Player 1 Wins the Game"
	elif(score2 > score1):
		return "Player 2 Wins the Game"
	else:
		return "Nobody Won"



#beginning = 1
#end = 6
#rollRange1 = (beginning,end)
#rollRange2 = (beginning,end)
score1 = 0
score2 = 0
ledger = []
#rollResult1 = rollRange1
#rollResult2 = rollrange2

gameRunning = 3

while(gameRunning >= 0):
	rollResult1 = roll(beginning,end)
	rollResult2 = roll(beginning,end)
	rollWin = roundWinner(rollResult1,rollResult2)
	if(rollResult1 > rollResult2):
		score1 += 1
	elif(rollResult2 > rollResult1):
		score2 += 1
	gameRunning -= 1
	print(rollResult1,rollResult2,rollWin)

gameWin = gameWinner(score1,score2)

print(gameWin)
