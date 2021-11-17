theBoard = {'1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '}

boardKeys = []

for key in theBoard:
    boardKeys.append(key)

def printBoard(board):
    print(" ___________________")
    print(' |  ' + board['1'] + '  |  ' + board['2'] + '  |  ' + board['3'] + '  | ')
    print(" -------------------")
    print(' |  ' + board['4'] + '  |  ' + board['5'] + '  |  ' + board['6'] + '  | ')
    print(" -------------------")
    print(' |  ' + board['7'] + '  |  ' + board['8'] + '  |  ' + board['9'] + '  | ')
    print(" -------------------")

def tictactoe_game():
    turn = 'X'
    count = 0

    while count < 9:

        printBoard(theBoard)
        print("It is turn of "+ turn +" Specify the place you want to go : ")
        move = input()

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1

        else:
            print("Sorry, this cell location is filled / not available. Please choose another one.")
            continue

        if count >= 5:

            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("\nGame Over")
                print("Player "+ turn + " won the game")
                break

            if theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
                printBoard(theBoard)
                print("\nGame Over")
                print("Player "+ turn + " won the game")
                break

            if theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print("\nGame Over")
                print("Player "+ turn + " won the game")
                break

            if theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':
                printBoard(theBoard)
                print("\nGame Over")
                print("Player "+ turn + " won the game")
                break

            if theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':
                printBoard(theBoard)
                print("\nGame Over")
                print("Player "+ turn + " won the game")
                break

            if theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("\nGame Over")
                print("Player "+ turn + " won the game")
                break

            if theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("\nGame Over")
                print("Player "+ turn + " won the game")
                break

            if theBoard['3'] == theBoard['5'] == theBoard['7'] != ' ':
                printBoard(theBoard)
                print("\nGame Over")
                print("Player "+ turn + " won the game")
                break

        if count == 9:
            print("\nGame Over")
            print("The game is Tie!")

        if turn == 'X':
            turn = 'O'

        else:
            turn = 'X'

    restart = input("Do you want to restart the Game? (y/n): ")

    if restart == 'y' or restart == 'Y':
        for key in boardKeys:
            theBoard[key] = ' '
        tictactoe_game()


if __name__ == "__main__":
    tictactoe_game()


