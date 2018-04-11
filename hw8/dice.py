import random

#ask for the name
fpname = raw_input ("what is your name?")

spname = raw_input ("what is your name?")

#1 game
game = 0

#the sum of two random numbers that has bveen rolled
def dicesum():

	return random.randint(1,6) + random.randint(1,6)

#what each player get on their numbers
firstplayer = dicesum()

secondplayer = dicesum()

print (firstplayer,secondplayer)

#determine who wins
def winner(game)

	if firstplayer > secondplayer:

		game = firstplayer

	elif secondplayer > firstplayer:

		game = secondplayer

	else:

		game = tie

	return game


#game end
if 
