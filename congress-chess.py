"""
Stanley Lee
CSC 180
Congress Chess
"""

def main():
    board = generateBoard()
    print(list(self.board))
    #printBoard(board)

class Board:
    def __init__(self):
        self.board = self.generateBoard()

    def generateBoard(self):
        board = []
        rows = 6
        cols = 8
        # Initialize empty game board
        board = [ (['-'] * cols) for row in range(rows) ]

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
        for x in range(cols):
            print(' '.join(x))

if __name__ == "__main__":
    main()
