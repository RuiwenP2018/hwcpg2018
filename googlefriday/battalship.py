import random

#creat a board
board = ()

for x in range(10):

        board.append(["O"] * 10)

def gameboard(board):

        for row in board:

                print " ".join(row)

game = gameboard(board)

print (game)



