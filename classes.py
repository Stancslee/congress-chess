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
        # Iterate through board
        for row in range(self.rows):
            for col in range(self.cols):
                # If player piece
                if(self.get_board()[row][col] in self.get_player_pieces()):
                    # Save src and compute dst
                    src = (row, col)
                    dst = self.piece_gen_moves(src)
                    # Reverse parse list of tuples [src, dst]
                    move = [src, dst]
                    legal_moves.append(self.reverse_parse(move))
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

    def reverse_parse(self, move):
        s = ''
        rev_col_map = {
                    0: 'A',
                    1: 'B',
                    2: 'C',
                    3: 'D',
                    4: 'E',
                    5: 'F',
                    6: 'G',
                    7: 'H'
                }
        # Parse move [src, dst], list of tuples
        s.join(rev_col_map.get(move[0][1]))
        s.join(self.rows - move[0][0])
        s.join(rev_col_map.get(move[1][1]))
        s.join(self.rows - move[1][0])
        return s

    def get_npc_pieces(self):
        return ['H', 'K', 'B', 'P']

    def get_player_pieces(self):
        return ['h', 'k', 'b', 'p']

    def piece_gen_moves(self, src):
        piece_generate_moves = {
                    'H': self.horse_gen_moves(src),
                    'K': self.king_gen_moves(src),
                    'B': self.bishop_gen_moves(src),
                    'P': self.pawn_gen_moves(src)
                }
        return piece_generate_moves

    def king_gen_moves(self, src):
        x = src[1]

        # Player Left King
        if( (x > 0 and x <= 3) and ( (self.get_board()[5][x-1] == '-') 
            or (self.get_board()[5][x-1] in board.get_npc_pieces()) )):
            # Return dst
            return (5, x-1)

        # Player Right King
        if( (x >= 4 and x < 7) and ( (self.get_board()[5][x+1] == '-') 
            or (self.get_board()[5][x+1] in board.get_npc_pieces()) )):
            # Return dst
            return (5, x+1)

        # NPC Left King
        if( (x > 0 and x <= 3) and ( (self.get_board()[0][x-1] == '-') 
            or (self.get_board()[0][x-1] in board.get_npc_pieces()) )):
            # Return dst
            return (0, x-1)

        # NPC Right King
        if( (x >= 4 and x < 7) and ( (self.get_board()[0][x+1] == '-') 
            or (self.get_board()[0][x+1] in board.get_npc_pieces()) )):
            # Return dst
            return (0, x+1)

    def pawn_gen_moves():
        return

    def horse_gen_moves():
        return

    def bishop_gen_moves():
        return

