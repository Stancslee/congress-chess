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
    player_turn = False
    choice = True
    turn_choice = ''
    move = ''
    game_over = False

    while(not game_over):
        while(choice):
            turn_choice = input("Please select your turn (1 or 2): ")
            if(turn_choice == '1'):
                player_turn = True
                choice = False
            elif(turn_choice == '2'):
                player_turn = False
                choice = False
            else:
                print('Your input is not an integer 1 or 2. Please try again.\n')

        # Call move Generator
        board.print_board()
        # Players take turns
        if(player_turn):
            # Print Legal Player Moves
            legal_moves = board.generate_moves()
            print(legal_moves)

            # Player makes move
            move = input('Enter your move: ')
            print('Your move: %s\n' % move)
            board.make_move(move)
            player_turn = False
        else:
            # NPC Move Generator (returns list of legal moves)
            # legalMoves = moveGenerator()

            # NPC makes move
            print('Computer move: rand\n')
            player_turn = True

        # Check legality of move
            # Compare list of legal moves to user input
        if(move == 'stop'):
            game_over = True

if __name__ == "__main__":
    main()
