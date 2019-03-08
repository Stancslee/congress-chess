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

        # Players take turns
        if(playerTurn):
            #player makes move
            move = input('Enter your move: ')
            print('Your move: %s\n' % move)
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


if __name__ == "__main__":
    main()
