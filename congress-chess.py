"""
Stanley Lee
CSC 180
Congress Chess
"""

from classes import (
    Board
)
import random

def main():
    board = Board()
    player_turn = False
    choice = True
    turn_choice = ''
    move = ''
    player_kings = 2
    npc_kings = 2
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
            legal_moves = board.generate_moves(player_turn)
            # Opponent wins of no playable moves
            if not legal_moves:
                game_over = True
                print('-----------------------------------')
                print('             GAME OVER')
                print('  NO PLAYER LEGAL MOVES REMAINING')
                print('           OPPONENT WINS')
                print('-----------------------------------')
                break
            print(legal_moves)

            # Player makes move
            move = input('Enter your move: ')
            while(move not in legal_moves):
                move = input('Please enter a valid move: ')
            print('Your move: %s\n' % move)
            board.make_move(move)
            npc_kings = board.update_kings(player_turn)
            if(npc_kings == 0):
                game_over = True
                print('-------------------------------')
                print('           GAME OVER')
                print('  ALL OPPONENT KINGS CAPTURED')
                print('          PLAYER WINS')
                print('-------------------------------')
                break
            player_turn = False
        else:
            # NPC Move Generator (returns list of legal moves)
            legal_moves = board.generate_moves(player_turn)
            # Player wins if no playable moves
            if not legal_moves:
                game_over = True
                print('-------------------------------------')
                print('              GAME OVER')
                print('  NO OPPONENT LEGAL MOVES REMAINING')
                print('             PLAYER WINS')
                print('-------------------------------------')
                break
            print(legal_moves)

            # NPC makes move
            """
            # Optional Player 2 Input
            move = input('Enter your move: ')
            while(move not in legal_moves):
                move = input('Please enter a valid move: ')
            """
            move = random.choice(legal_moves)
            print('Computer move: %s\n' % move)
            board.make_move(move)
            player_kings = board.update_kings(player_turn)
            if(player_kings == 0):
                game_over = True
                print('-----------------------------')
                print('          GAME OVER')
                print('  ALL PLAYER KINGS CAPTURED')
                print('        OPPONENT WINS')
                print('-----------------------------')
                break
            player_turn = True

        # Check legality of move
            # Compare list of legal moves to user input
        if(move == 'stop'):
            game_over = True

if __name__ == "__main__":
    main()
