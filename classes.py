"""
Stanley Lee
Dr. Scott Gordon
CSC 180
Congress Chess
Program Name: user.sentience(0)
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

    def generate_moves(self, player_turn):
        legal_moves = []

        """ DELETE LATER """
        from collections import defaultdict
        debug_legal_moves = defaultdict(list) 
        """ DELETE LATER """

        piece_gen_moves = {
                    'H': self.horse_gen_moves,
                    'K': self.king_gen_moves,
                    'B': self.bishop_gen_moves,
                    'P': self.pawn_gen_moves
                }
        # Iterate through board
        for row in range(self.rows):
            for col in range(self.cols):
                # If player piece
                if(player_turn):
                    if(self.get_board()[row][col] in self.get_player_pieces()):
                    # Save src and compute dst
                        src = (row, col)
                        cur_piece = self.get_board()[row][col].upper()
                        # dst = list of tuples [ (), (), () ]
                        dst = piece_gen_moves[cur_piece](src)
                        # If a legal move exists / dst list is not empty
                        if dst: 
                            # Pair src with each dst tuple
                            for pos in dst:
                                # Reverse parse list of tuples [src, dst]
                                move = [src, pos]
                                legal_moves.append(self.reverse_parse(move))
                                debug_legal_moves[cur_piece].append(self.reverse_parse(move)) # DELETE LATER

                # If computer piece
                else:
                    if(self.get_board()[row][col] in self.get_npc_pieces()):
                        # Save src and compute dst
                        src = (row, col)
                        cur_piece = self.get_board()[row][col].upper()
                        # If a legal move exists / dst list is not empty
                        dst = piece_gen_moves[cur_piece](src)
                        # If a legal move exists
                        if dst:
                            for pos in dst:
                                # Reverse parse list of tuples [src, dst]
                                move = [src, pos]
                                legal_moves.append(self.reverse_parse(move))
                                debug_legal_moves[cur_piece].append(self.reverse_parse(move)) # DELETE LATER
               
        """ DELETE LATER """
        for piece in debug_legal_moves.keys():
            print(piece)
            for move in debug_legal_moves[piece]:
                print('\t' + move)
        """ DELETE LATER """

        return legal_moves

    def get_board(self):
        return self.board

    def minimax(self, player_kings, npc_kings, player_turn):
        best_score = -9999
        best_move = ''
        depth = 0
        max_depth = 3
        # For each legal move in the game
        legal_moves = self.generate_moves(player_turn)
        '''
        if(len(legal_moves) < max_depth):
            max_depth = len(legal_moves)
        '''
        for move in legal_moves:
            print(move)
            # Make move and save changes of board state
            changes = self.make_move(move)
            # Keep track of score after move is made
            score = self.min(depth+1, max_depth, player_kings, npc_kings, not player_turn)
            if(score > best_score):
                best_score = score
                best_move = move
            # Undo move
            self.undo_move(move, changes)
        # Make best_move
        if(best_move):
            print('Best Move:')
            print(best_move)
            self.make_move(best_move)
        return best_move

    def min(self, depth, max_depth, player_kings, npc_kings, player_turn):
        print('...Calculating Min')
        print('depth = %d' % depth)
        best_score = 9999
        # Check win/loss
        if(player_kings == 0):
            return 5000
        if(npc_kings == 0):
            return -5000
        # Return node value at max depth
        if(depth == max_depth):
            print('max depth: %d; val: %d' % (max_depth, self.eval()))
            return (self.eval() + depth)
        # For each legal move
        legal_moves = self.generate_moves(player_turn)
        for move in legal_moves:
            # Make move and save changes of board state
            changes = self.make_move(move)
            score = self.max(depth+1, max_depth, player_kings, npc_kings, not player_turn)
            if(score < best_score):
                best_score = score
            # Undo move
            self.undo_move(move, changes)
        return best_score

    def max(self, depth, max_depth, player_kings, npc_kings, player_turn):
        print('...Calculating Max')
        print('depth = %d' % depth)
        best_score = -9999
        # Check win/loss
        if(player_kings == 0):
            return 5000
        if(npc_kings == 0):
            return -5000
        # Return node value at max depth
        if(depth == max_depth):
            print('max depth: %d; val: %d' % (max_depth, self.eval()))
            return (self.eval() - depth)
        # For each legal move
        legal_moves = self.generate_moves(player_turn)
        for move in legal_moves:
            # Make move and save changes of board state
            changes = self.make_move(move)
            score = self.min(depth+1, max_depth, player_kings, npc_kings, not player_turn)
            print(move)
            print('score = %d' % score)
            if(score > best_score):
                best_score = score
            # Undo Move
            self.undo_move(move, changes)
        return best_score

    def eval(self):
        val = 0
        npc_piece_values = {
                'P': 1,
                'H': 3,
                'B': 3,
                'K': 5
                }
        player_piece_values = {
                'p': 1,
                'h': 3,
                'b': 3,
                'k': 5
                }
        for row in range(self.rows):
            for col in range(self.cols):
                if(self.get_board()[row][col] in npc_piece_values):
                    val += npc_piece_values.get(self.get_board()[row][col])
                    '''
                    # PRINT PIECE VALUES AND TOTAL VALUES
                    print('Piece: %s; Val: %d' % (self.get_board()[row][col], npc_piece_values.get(self.get_board()[row][col])))
                    print('Total NPC Val: %d' % val)
                    '''
                elif(self.get_board()[row][col] in player_piece_values):
                    val -= player_piece_values.get(self.get_board()[row][col])
        return val

    # Applies move to board
    def make_move(self, cur_move):
        # cur_move (String) to move (int[ ( , ), ( , )])
        move = self.parse_move(cur_move)
        # Save src & dst values
        src = self.get_board()[ move[0][0] ][ move[0][1] ]
        dst = self.get_board()[ move[1][0] ][ move[1][1] ]
        changes = (src, dst)
        # Make move
        self.get_board()[ move[1][0] ][ move[1][1] ] = src
        self.get_board()[ move[0][0] ][ move[0][1] ] = '-'
        # Change piece to horse if on left half of board
        if(src == 'B' and move[1][1] < 4):
            self.get_board()[ move[1][0] ][ move[1][1] ] = 'H'
        elif(src == 'b'  and move[1][1] < 4):
            self.get_board()[ move[1][0] ][ move[1][1] ] = 'h'
        # Change piece to bishop of on right half of board
        elif(src == 'H' and move[1][1] > 3):
            self.get_board()[ move[1][0] ][ move[1][1] ] = 'B'
        elif(src == 'h' and move[1][1] > 3):
            self.get_board()[ move[1][0] ][ move[1][1] ] = 'b'
        return changes

    def undo_move(self, cur_move, changes):
        move = self.parse_move(cur_move)
        self.get_board()[ move[0][0] ][ move[0][1] ] = changes[0]
        self.get_board()[ move[1][0] ][ move[1][1] ] = changes[1]

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
        src = (self.rows - int(char[1]), col_map.get(char[0])) # INDEX OUT OF BOUNDS
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
        s += rev_col_map.get(move[0][1])
        s += str(self.rows - move[0][0])
        s += rev_col_map.get(move[1][1])
        s += str(self.rows - move[1][0])
        return s

    def translate_move(self, move):
        src_num = (self.cols-1) - int(move[1])
        dst_num = (self.cols-1) - int(move[3])
        trans_move = move[0] + str(src_num) + move[2] + str(dst_num)
        return trans_move

    def update_kings(self, player_turn):
        player_kings = 0
        npc_kings = 0
        # If player makes move, update NPC Kings
        if(player_turn):
            for col in self.get_board()[0]:
                if(col == 'K'):
                    npc_kings += 1
            return npc_kings
        else:
            for col in self.get_board()[5]:
                if(col == 'k'):
                    player_kings += 1
            return player_kings

    def get_npc_pieces(self):
        return ['H', 'K', 'B', 'P']

    def get_player_pieces(self):
        return ['h', 'k', 'b', 'p']

    def king_gen_moves(self, src):
        row = src[0]
        col = src[1]
        dst = []

        # Player Left King
        if((row==5 and col>0 and col<=3) and ((self.get_board()[5][col-1]=='-') 
            or (self.get_board()[5][col-1] in self.get_npc_pieces()) )):
            # Return dst
            dst.append( (5, col-1) )

        # Player Right King
        if((row==5 and col>=4 and col<7) and ((self.get_board()[5][col+1]=='-') 
            or (self.get_board()[5][col+1] in self.get_npc_pieces()) )):
            # Return dst
            dst.append( (5, col+1) )

        # NPC Left King
        if((row==0 and col>0 and col<=3) and ((self.get_board()[0][col-1]=='-') 
            or (self.get_board()[0][col-1] in self.get_player_pieces()) )):
            # Return dst
            dst.append( (0, col-1) )

        # NPC Right King
        if((row==0 and col>=4 and col<7) and ((self.get_board()[0][col+1]=='-') 
            or (self.get_board()[0][col+1] in self.get_player_pieces()) )):
            # Return dst
            dst.append( (0, col+1) )
        return dst

    def pawn_gen_moves(self, src):
        row = src[0]
        col = src[1]
        dst = []

        # Player Moves
        if(self.get_board()[row][col].islower() and row != 0):
            # Forward movement
            if(self.get_board()[row-1][col] == '-'):
                dst.append( (row-1, col) )
            # Capture Left
            if(col>0 and self.get_board()[row-1][col-1]
                    in self.get_npc_pieces()):
                dst.append ((row-1, col-1) )
            # Capture Right
            if(col<self.cols-1 and self.get_board()[row-1][col+1] 
                    in self.get_npc_pieces()):
                dst.append( (row-1, col+1) )
        
        # NPC Moves
        elif(self.get_board()[row][col].isupper() and row != self.rows-1):
	    # Forward movement
            if(self.get_board()[row+1][col] == '-'):
                dst.append( (row+1, col) )
	    # Capture Left
            if(col>0 and self.get_board()[row+1][col-1]
		    in self.get_player_pieces()):
                dst.append( (row+1, col-1) )
	    # Capture Right
            if(col<self.cols-1 and self.get_board()[row+1][col+1]
	    	    in self.get_player_pieces()):
                dst.append( (row+1, col+1) )
        return dst

    def horse_gen_moves(self, src):
        row = src[0]
        col = src[1]
        dst = []

        # Player Moves
        if(self.get_board()[row][col].islower()):
            # Up-Right
            if(row > 1 and col < self.cols-1):
                if(self.get_board()[row-2][col+1] == '-' or 
                        self.get_board()[row-2][col+1] in self.get_npc_pieces()):
                    dst.append( (row-2, col+1) )
            
            # Up-Left
            if(row > 1 and col > 0): 
                if(self.get_board()[row-2][col-1] == '-' or 
                        self.get_board()[row-2][col-1] in self.get_npc_pieces()):
                    dst.append( (row-2, col-1) )
            
            # Left-Up
            if(row > 0 and col > 1): 
                if(self.get_board()[row-1][col-2] == '-' or 
                        self.get_board()[row-1][col-2] in self.get_npc_pieces()):
                    dst.append( (row-1, col-2) )
            
            # Left-Down
                # Only on capture AND above 1/2 the board (senior)
            if(row < 3 and col > 1):
                if(self.get_board()[row+1][col-2] in self.get_npc_pieces()):
                    dst.append( (row+1, col-2) )

            # Right-Up
            if(row > 0 and col < self.cols-2):
                if(self.get_board()[row-1][col+2] == '-' or 
                        self.get_board()[row-1][col+2] in self.get_npc_pieces()): 
                    dst.append( (row-1, col+2) )

            # Right-Down
                # Only on capture AND above 1/2 the board (senior)
            if(row < 3 and col < self.cols-2):
                if(self.get_board()[row+1][col+2] in self.get_npc_pieces()): 
                    dst.append( (row+1, col+2) )

            # Down-Left
                # Only on capture AND above 1/2 the board (senior)
            if(row < 3 and col > 0):
                if(self.get_board()[row+2][col-1] in self.get_npc_pieces()): 
                    dst.append( (row+2, col-1) )
            
            # Down-Right
                # Only on capture AND above 1/2 the board (senior)
            if(row < 3 and col < self.cols-1):
                if(self.get_board()[row+2][col+1] in self.get_npc_pieces()):
                    dst.append( (row+2, col+1) )

        # NPC Moves
        elif(self.get_board()[row][col].isupper()):
	    # Up-Right
                # Only on capture AND below 1/2 the board (senior)
            if(row > 2 and col < self.cols-1):
                if(self.get_board()[row-2][col+1] in self.get_player_pieces()):
                    dst.append( (row-2, col+1) )
            
            # Up-Left
            if(row > 2 and col > 0):
                if(self.get_board()[row-2][col-1] in self.get_player_pieces()): 
                    dst.append( (row-2, col-1) )
            
            # Left-Up
            if(row > 2 and col > 1):
                if(self.get_board()[row-1][col-2] in self.get_player_pieces()): 
                    dst.append( (row-1, col-2) )
            
            # Left-Down
            if(row < self.rows-1 and col > 1):
                if(self.get_board()[row+1][col-2] == '-' or 
                        self.get_board()[row+1][col-2] in self.get_player_pieces()): 
                    dst.append( (row+1, col-2) )
  
            # Right-Up
            if(row > 2 and col < self.cols-2):
                if(self.get_board()[row-1][col+2] in self.get_player_pieces()): 
                    dst.append( (row-1, col+2) )

            # Right-Down
            if(row < self.rows-1 and col < self.cols-2):
                if(self.get_board()[row+1][col+2] == '-' or 
                        self.get_board()[row+1][col+2] in self.get_player_pieces()): 
                    dst.append( (row+1, col+2) )

            # Down-Left
            if(row < self.rows-2 and col > 0):
                if(self.get_board()[row+2][col-1] == '-' or 
                        self.get_board()[row+2][col-1] in self.get_player_pieces()): 
                    dst.append( (row+2, col-1) )
            
            # Down-Right
            if(row < self.rows-2 and col < self.cols-1):
                if(self.get_board()[row+2][col+1] == '-' or 
                        self.get_board()[row+2][col+1] in self.get_player_pieces()): 
                    dst.append( (row+2, col+1) )
        return dst

    def bishop_gen_moves(self, src):
        # Source position
        row = src[0]
        col = src[1]
        dst = []

        # Current checking position (starts at source)
        cur_pos = src
        cur_row = row
        cur_col = col

        # Next checking position
        nxt_row = row
        nxt_col = col

        # Player Move
        if(self.get_board()[row][col].islower()):
            # Up-Left
            while(cur_row > 0 and cur_col > 0):
                done = False
                nxt_row -= 1
                nxt_col -= 1
                nxt_pos = (nxt_row, nxt_col)

                """
                POSITION CHECKING
                print('\n...Checking. ({}, {}) -> ({}, {})'.format(cur_row, cur_col, nxt_row, nxt_col))
                print('Checking new bishop position. row: {}, col: {}'.format(nxt_row, nxt_col))
                """

                # If next space empty or capture, append that space
                if(self.get_board()[nxt_row][nxt_col] == '-'):
                    dst.append( (nxt_row, nxt_col) )
                    # print('\tThis is a valid move')
                    # BOUNDARY CHECK FOR EVERY LOOP
                    if(nxt_row == 0 or nxt_col == 0):
                        done = True
                elif(self.get_board()[nxt_row][nxt_col] in self.get_npc_pieces()):
                    dst.append( (nxt_row, nxt_col) )
                    # print('\tThis is a valid move')
                    done = True
                # Else if next piece is player's piece, done
                elif(self.get_board()[nxt_row][nxt_col] in self.get_player_pieces()):
                    done = True
                # Update cur_pos to nxt_pos
                if done:
                    cur_pos = src
                    cur_row = row
                    cur_col = col
                    nxt_row = row
                    nxt_col = col
                    # print('...Resetting position ({}, {})'.format(cur_row, cur_col))
                    break
                cur_pos = nxt_pos
                cur_row = nxt_row
                cur_col = nxt_col

            # Up-Right
            while(cur_row > 0 and cur_col < self.cols-1):
                done = False
                nxt_row -= 1
                nxt_col += 1
                nxt_pos = (nxt_row, nxt_col)

                """
                POSITION CHECKING
                print('\n...Checking. ({}, {}) -> ({}, {})'.format(cur_row, cur_col, nxt_row, nxt_col))
                print('Checking new bishop position. row: {}, col: {}'.format(nxt_row, nxt_col))
                """

                # If next space empty or capture, append that space
                if(self.get_board()[nxt_row][nxt_col] == '-'):
                    dst.append( (nxt_row, nxt_col) )
                    # print('\tThis is a valid move')
                    if(nxt_row == 0 or nxt_col == self.cols-1):
                        done = True
                elif(self.get_board()[nxt_row][nxt_col] in self.get_npc_pieces()):
                    dst.append( (nxt_row, nxt_col) )
                    # print('\tThis is a valid move')
                    done = True
                # Else if next piece is player's piece, done
                elif(self.get_board()[nxt_row][nxt_col] in self.get_player_pieces()):
                    done = True
                # Update cur_pos to nxt_pos
                if done:
                    cur_pos = src
                    cur_row = row
                    cur_col = col
                    nxt_row = row
                    nxt_col = col
                    break
                cur_pos = nxt_pos
                cur_row = nxt_row
                cur_col = nxt_col

            # Down-Left
                # While above 1/2 the board (senior)
            while(row < 3 and cur_row < self.rows and cur_col > 0):
                done = False
                nxt_row += 1
                nxt_col -= 1
                nxt_pos = (nxt_row, nxt_col)

                """
                POSITION CHECKING
                print('\n...Checking. ({}, {}) -> ({}, {})'.format(cur_row, cur_col, nxt_row, nxt_col))
                print('Checking new bishop position. row: {}, col: {}'.format(nxt_row, nxt_col))
                """

                # If next space is a capture, append that space
                if(self.get_board()[nxt_row][nxt_col] in self.get_npc_pieces()):
                    dst.append( (nxt_row, nxt_col) )
                    done = True
                    # print('\tThis is a valid move')
                # Else if next piece is player's piece,
                # break loop and do not append anything
                elif(self.get_board()[nxt_row][nxt_col] in self.get_player_pieces()):
                    done = True
                if(nxt_row == self.rows-1 or nxt_col == 0):
                    done = True
                # Update cur_pos to nxt_pos
                if done:
                    cur_pos = src
                    cur_row = row
                    cur_col = col
                    nxt_row = row
                    nxt_col = col
                    break
                cur_pos = nxt_pos
                cur_row = nxt_row
                cur_col = nxt_col

            # Down-Right
                # While above 1/2 the board (senior)
            while(row < 3 and cur_row < self.rows and cur_col < self.cols-1):
                done = False
                nxt_row += 1
                nxt_col += 1
                nxt_pos = (nxt_row, nxt_col)

                """
                POSITION CHECKING
                print('\n...Checking. ({}, {}) -> ({}, {})'.format(cur_row, cur_col, nxt_row, nxt_col))
                print('Checking new bishop position. row: {}, col: {}'.format(nxt_row, nxt_col))
                """

                # If next space is a capture, append that space
                if(self.get_board()[nxt_row][nxt_col] in self.get_npc_pieces()):
                    dst.append( (nxt_row, nxt_col) )
                    done = True
                    # print('\tThis is a valid move')
                # Else if next piece is player's piece,
                # break loop and do not append anything
                elif(self.get_board()[nxt_row][nxt_col] in self.get_player_pieces()):
                    done = True
                # BOUNDARY CHECK FOR ALL BACKWARDS CAPTURE LOOP
                if(nxt_row == self.rows-1 or nxt_col == self.cols-1):
                    done = True
                # Update cur_pos to nxt_pos
                if done:
                    cur_pos = src
                    cur_row = row
                    cur_col = col
                    nxt_row = row
                    nxt_col = col
                    break
                
                cur_pos = nxt_pos
                cur_row = nxt_row
                cur_col = nxt_col

        # NPC Move
        elif(self.get_board()[row][col].isupper()):
            # Down-Left
            while(cur_row < self.rows-1 and cur_col > 0):
                done = False
                nxt_row += 1
                nxt_col -= 1
                nxt_pos = (nxt_row, nxt_col)
                # If next space empty or capture, append that space
                if(self.get_board()[nxt_row][nxt_col] == '-'):
                    dst.append( (nxt_row, nxt_col) )
                    if(nxt_row == self.rows-1 or nxt_col == 0):
                        done = True
                elif(self.get_board()[nxt_row][nxt_col] in self.get_player_pieces()):
                    dst.append( (nxt_row, nxt_col) )
                    done = True
                # Else if next piece is npc's piece, done
                elif(self.get_board()[nxt_row][nxt_col] in self.get_npc_pieces()):
                    done = True
                # Update cur_pos to nxt_pos
                if done:
                    cur_pos = src
                    cur_row = row
                    cur_col = col
                    nxt_row = row
                    nxt_col = col
                    break
                cur_pos = nxt_pos
                cur_row = nxt_row
                cur_col = nxt_col
            
            # Down-Right
            while(cur_row < self.rows-1 and cur_col < self.cols-1):
                done = False
                nxt_row += 1
                nxt_col += 1
                nxt_pos = (nxt_row, nxt_col)
                # If next space empty or capture, append that space
                if(self.get_board()[nxt_row][nxt_col] == '-'):
                    dst.append( (nxt_row, nxt_col) )
                    if(nxt_row == self.rows-1  or nxt_col == self.cols-1):
                        done = True
                elif(self.get_board()[nxt_row][nxt_col] in self.get_player_pieces()):
                    dst.append( (nxt_row, nxt_col) )
                    done = True
                # Else if next piece is npc's piece, done
                elif(self.get_board()[nxt_row][nxt_col] in self.get_npc_pieces()):
                    done = True
                # Update cur_pos to nxt_pos
                if done:
                    cur_pos = src
                    cur_row = row
                    cur_col = col
                    nxt_row = row
                    nxt_col = col
                    break
                cur_pos = nxt_pos
                cur_row = nxt_row
                cur_col = nxt_col

            # Up-Left
                # While above 1/2 the board (senior)
            while(row > 2 and cur_row > 0 and cur_col > 0):
                done = False
                nxt_row -= 1
                nxt_col -= 1
                nxt_pos = (nxt_row, nxt_col)
                # If next space is a capture, append that space
                if(self.get_board()[nxt_row][nxt_col] in self.get_player_pieces()):
                    dst.append( (nxt_row, nxt_col) )
                    done = True
                # Else if next piece is npc's piece,
                # break loop and do not append anything
                elif(self.get_board()[nxt_row][nxt_col] in self.get_npc_pieces()):
                    done = True
                if(nxt_row == 0 or nxt_col == 0):
                    done = True
                # Update cur_pos to nxt_pos
                if done:
                    cur_pos = src
                    cur_row = row
                    cur_col = col
                    nxt_row = row
                    nxt_col = col
                    break
                cur_pos = nxt_pos
                cur_row = nxt_row
                cur_col = nxt_col

            # Up-Right
                # While above 1/2 the board (senior)
            while(row > 2 and cur_row > 0 and cur_col < self.cols-1):
                done = False
                nxt_row -= 1
                nxt_col += 1
                nxt_pos = (nxt_row, nxt_col)
                # If next space is a capture, append that space
                if(self.get_board()[nxt_row][nxt_col] in self.get_player_pieces()):
                    dst.append( (nxt_row, nxt_col) )
                    done = True
                # Else if next piece is npc's piece,
                # break loop and do not append anything
                elif(self.get_board()[nxt_row][nxt_col] in self.get_npc_pieces()):
                    done = True
                if(nxt_row == 0 or nxt_col == self.cols-1):
                    done = True
                # Update cur_pos to nxt_pos
                if done:
                    cur_pos = src
                    cur_row = row
                    cur_col = col
                    nxt_row = row
                    nxt_col = col
                    break
                cur_pos = nxt_pos
                cur_row = nxt_row
                cur_col = nxt_col
                
        return dst

