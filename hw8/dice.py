import random

#the sum of two random numbers that has bveen rolled
def dicesum():

	return random.randint(1,6) + random.randint(1,6)

#determine who wins
def winner(firstplayer,secondplayer):

	if firstplayer > secondplayer:

		return fpname + " win the round."

	elif secondplayer > firstplayer:

		return spname + " win the round."

	else:

		return "no one won the game"

#determine the final winner
def finalwinner(fpwin,spwin):

	if fpwin > spwin:

		return fpname + " win the game."

	elif spwin > fpwin:

		return spname + " win the game."

	else:

		return (game)


#ask for the name
fpname = raw_input ("what is your name?")

spname = raw_input ("what is your name?")

#1 game
round = 3

fpwin = 0

spwin = 0

#game start
while (round >= 0):

#what each player get on their numbers
	firstplayer = dicesum()

	secondplayer = dicesum()

#play the game
	game = winner(firstplayer,secondplayer)

	if (firstplayer > secondplayer):

		fpwin += 1

	elif (secondplayer > firstplayer):

		spwin += 1

	round -= 1
	print (firstplayer,secondplayer,game)

#finash the game
gamewin = finalwinner(fpwin,spwin)

print (gamewin)
