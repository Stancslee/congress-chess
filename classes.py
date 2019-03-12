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

    def generateMoves(self):
        legalMoves = []

    def getBoard(self):
        return self.board

    """
    def make_move(self, cur_move, board):
        move = self.parse_move(cur_move)
        print(move[1][0])
        print(move[1][1])
        # Save src & dst values
        print( "src = " + board[ move[0][0] ][ move[0][1] ] )
        print( "dst = " + board[ move[1][0] ][ move[1][1] ] )
        # Make move
        board[ move[1][0] ][ move[1][1] ] = src
        board[ move[0][0] ][ move[0][1] ] = '-'

    def parse_move(self, move):
        col_map = {
            'A': 0,
            'B': 1,
            'C': 2,
            'D': 3,
            'E': 4,
            'F': 5,
            'G': 6,
            'H': 7
        }
        char = []
        for c in move:
            char.append(c)
        src = (self.rows - int(char[1]), col_map.get(char[0]))
        dst = (self.rows - int(char[3]), col_map.get(char[2]))
        print(src, dst)
        return [src, dst]
    """

    def king_gen_moves(pos):
        return




