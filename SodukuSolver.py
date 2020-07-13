import numpy as np


class Board:
    def __init__(self):
        self.won = False
        # self.board = np.zeros(81).reshape(9, 9)
        self.board = np.arange(81).reshape(9, 9)
        self.board[::9, ::1] = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def printBoard(self):
        print(self.board)


class GameLogic(Board):
    def __init__(self):
        super().__init__()
        self.col = []
        self.rows = []

        for i in range(9):
            self.rows.append(self.board[i::9, ::1])
            self.col.append(self.board[::1, i::9])

    def checkWin(self):
        # Need to work on.
        pass

    def checkPosition(self, xPos, yPos):
        playerInput = int(input("Enter a number "))

        if any(playerInput in x for x in self.rows[xPos]) or any(playerInput in y for y in self.col[yPos]):
            print("Cannot enter number here")
            # Can't enter the number in this position so try a different number
        else:
            print("Can enter number here")
            # Can enter the number here. Move on to a different position


# Initialize
board = Board()
gameLogic = GameLogic()

board.printBoard()
gameLogic.checkWin()
#gameLogic.checkPosition(0, 0)
