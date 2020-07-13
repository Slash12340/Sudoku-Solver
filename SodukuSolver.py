import numpy as np


class Board:
    def __init__(self):
        self.won = True
        self.winningArray = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        self.col = []
        self.rows = []

        self.colWon = []
        self.rowWon = []
        # self.board = np.zeros(81).reshape(9, 9)

        # This is just for testing
        # Solved Sudoku array (got from google):
        self.board = np.array([8, 2, 7, 1, 5, 4, 3, 9, 6,
                               9, 6, 5, 3, 2, 7, 1, 4, 8,
                               3, 4, 1, 6, 8, 9, 7, 5, 2,
                               5, 9, 3, 4, 6, 8, 2, 7, 1,
                               4, 7, 2, 5, 1, 3, 6, 8, 9,
                               6, 1, 8, 9, 7, 2, 4, 3, 5,
                               7, 8, 6, 2, 3, 5, 9, 1, 4,
                               1, 5, 4, 7, 9, 6, 8, 2, 3,
                               2, 3, 9, 8, 4, 1, 5, 6, 7]).reshape(9, 9)

    def printBoard(self):
        print(self.board)


class GameLogic(Board):
    def __init__(self):
        super().__init__()

        for i in range(9):
            self.rows.append(self.board[i::9, ::1])
            self.col.append(self.board[::1, i::9])

    def checkWin(self):
        # Currently being worked on
        for i in range(9):
            if all(items in self.rows[i] for items in self.winningArray):
                self.rowWon.append(["True"])
            else:
                self.rowWon.append(["False"])

            if all(items in self.col[i] for items in self.winningArray):
                self.colWon.append(["True"])
            else:
                self.colWon.append(["False"])

        if all(items == ["True"] for items in self.rowWon) and all(items == ["True"] for items in self.colWon):
            print("Game Won!!!")
            # Game is won and is over
        else:
            print("Game not won. Keep trying!")
            # Game not won. Continue trying

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
# gameLogic.checkPosition(0, 0)
