import numpy as np

class Board:
    def __init__(self):
        self.board = np.zeros(81).reshape(9, 9)

    def printBoard(self):
        print(self.board)

test = Board()
test.printBoard()