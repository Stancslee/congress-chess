"""
Stanley Lee
CSC 180
Congress Chess
"""

class Board:
    def __init__(self):
        self.rows = 6
        self.cols = 8
        self.board = self.generateBoard()

    def generateBoard(self):
        board = []
        # Initialize empty game board
        board = [ (['-'] * self.cols) for row in range(self.rows) ]

        # Initialize NPC Pieces
        board[0][0] = 'H'
        board[0][1] = 'H'
        board[0][3] = 'K'
        board[0][4] = 'K'
        board[0][6] = 'B'
        board[0][7] = 'B'
        for x in range(6):
            board[1][x+1] = 'P'

        # Initialize Player Pieces
        board[5][0] = 'h'
        board[5][1] = 'h'
        board[5][3] = 'k'
        board[5][4] = 'k'
        board[5][6] = 'b'
        board[5][7] = 'b'
        for x in range(6):
            board[4][x+1] = 'p'
        return board

    def printBoard(self):

        for x in range(self.rows):
            print( ('%s ' % str(self.rows - x)) + ' '.join(self.board[x]) )
        print('  ---------------')
        print('  A B C D E F G H')

class MoveGenerator:
    def __init__(self):
        self.legalMoves = self.generateMoves()

    def generateMoves(self):
        legalMoves = []

class King:
    def __init__(self):

class Horse:
    def __init__(self):

class Bishop:
    def __init__(self):

class Pawn:
    def __init__(self):


