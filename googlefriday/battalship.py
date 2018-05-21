from random import randint

#creat a board
board = []

for x in range(10):

        board.append(["X"] * 10)

def gameboard(board):

        for row in board:

                print " ".join(row)

game = gameboard(board)

print (game)

#start game
def randomR(board):

	return randint(0,len(board)-1)

def randomC(board):

	return randint(0,len(board[0])-1)

shipR = randomR(board)

shipC = randomC(board)

print (shipR)

print (shipC)

#game
#guesses = 0

for guesses in range(6):

	R = int(raw_input("pleace enter a number that you want to hit.(Row)"))

	C = int(raw_input("pleace enter a number that you want to hit.(colom)"))

	print (guesses)

	if R == shipR and C == shipC:

		print("Nice work. ")

		break

	else:

		if (0 < R > 10) or (0 < C > 10):

			print("pleace enter a valid number. ")

		elif board[R][C] == 'crash':

	        	print("You have crushed this point. ")

		else:

			if guesses == 5:

				print("Game over. ")

			else:

				print("You have missed. ")

				board[R][C] == 'crash'

		print(guesses), guesses + 1

		gameboard(board)




#game
#guess = "5"

#hits = 0

#guesses = 0

#isSunk = False

#guess = raw_input("Pleace enter the location you want to hit? (0 - 10)")

#while (isSunk == False):

#	if (guess >= "0" or guess <= "10"):

#                guesses = guesses + 1

#                if (guess == shipR or guess == shipC):

#                        print ("HIT!")

#                        hits = hits + 1

#                        if (hits == 2):

#                                isSunk = True

#                                print ("You have sunk the enemy")

#                        else:

#                                print ("miss!")

#	else:

#		print ("pleace enter a valid number.")

#print ("You took " + guesses + " guesses to sink the enemy ship.")
