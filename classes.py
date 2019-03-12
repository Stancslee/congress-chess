"""
Stanley Lee
CSC 180
Congress Chess
"""

class Board:
    def __init__(self):
        self.rows = 6
        self.cols = 8
        self.board = self.generate_board()

    def generate_board(self):
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

    def print_board(self):
        for x in range(self.rows):
            print( ('%s ' % str(self.rows - x)) + ' '.join(self.board[x]) )
        print('  ---------------')
        print('  A B C D E F G H')

    def generate_moves(self):
        legal_moves = []
        return legal_moves

    def get_board(self):
        return self.board

    def make_move(self, cur_move):
        move = self.parse_move(cur_move)
        # Save src & dst values
        src = self.get_board()[ move[0][0] ][ move[0][1] ]
        dst = self.get_board()[ move[1][0] ][ move[1][1] ]
        # Make move
        self.get_board()[ move[1][0] ][ move[1][1] ] = src
        self.get_board()[ move[0][0] ][ move[0][1] ] = '-'

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
        return [src, dst]

    def get_npc_pieces(self):
        return ['H', 'K', 'B', 'P']

    def get_player_pieces(self):
        return ['h', 'k', 'b', 'p']

    def king_gen_moves(self, pos):
        x = pos[1]
        # Player Left King
        if( (x > 0 and x <= 3) and ( (self.get_board()[5][x-1] == '-') 
            or (self.get_board()[5][x-1] is in board.get_npc_pieces() ):
            # Return dst

        return

    def pawn_gen_moves():
        return

    def horse_gen_moves():
        return

    def bishop_gen_moves():
        return

