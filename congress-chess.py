"""
Stanley Lee
CSC 180
Congress Chess
"""

from classes import (
    Board
)

def main():
    board = Board()
    board.printBoard()
    playerTurn = False
    choice = True
    turnChoice = ''
    move = ''
    gameOver = False

    while(not gameOver):
        while(choice):
            turnChoice = input("Please select your turn (1 or 2): ")
            if(turnChoice == '1'):
                playerTurn = True
                choice = False
            elif(turnChoice == '2'):
                playerTurn = False
                choice = False
            else:
                print('Your input is not an integer 1 or 2. Please try again.\n')

        # Call move Generator
        print(board[0][0])
        # Players take turns
        if(playerTurn):
            #player makes move
            move = input('Enter your move: ')
            print('Your move: %s\n' % move)
            make_move(move, board)
            playerTurn = False
        else:
            # NPC Move Generator (returns list of legal moves)
            # legalMoves = moveGenerator()

            # NPC makes move
            print('Computer move: rand\n')
            playerTurn = True

        # Check legality of move
            # Compare list of legal moves to user input
        if(move == 'stop'):
            gameOver = True

def make_move(cur_move, board):
    move = parse_move(cur_move, board)
    print(move[1][0])
    print(move[1][1])
    # Save src & dst values
    print( "src = " + board[ move[0][0] ][ move[0][1] ] )
    print( "dst = " + board[ move[1][0] ][ move[1][1] ] )
    # Make move
    board[ move[1][0] ][ move[1][1] ] = src
    board[ move[0][0] ][ move[0][1] ] = '-'

def parse_move(move, board):
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
        print(c)
    src = (board.rows - int(char[1]), col_map.get(char[0]))
    dst = (board.rows - int(char[3]), col_map.get(char[2]))
    print(src, dst)
    return [src, dst]


if __name__ == "__main__":
    main()
