board = [' ' for x in range(10)]

def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '

def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def isWinner(bo, le):
    return (bo[1] == le and bo[2] == le and bo[3] == le) or (bo[4] == le and bo[5]==le and bo[6]==le) or (bo[7] == le and bo[8]==le and bo[9]==le) or (bo[1] == le and bo[4]==le and bo[7]==le) or (bo[2] == le and bo[5]==le and bo[8]==le) or(bo[3] == le and bo[6]==le and bo[9]==le) or (bo[1] == le and bo[5]==le and bo[9]==le) or (bo[3] == le and bo[5]==le and bo[7]==le)

def playerMove():
    run = True
    while(run):
        move = input("Please select a position to place an \'X\' [1-9]: ")
        try:
            move = int(move)
            if move>0 and move<10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X',move)
                else:
                    print("Sorry, This Space is Occupied!")
            else:
                print("Please Type a number within the given range: ")
        except:
            print("Please type a Number: ")

def compMove():
    possibleMoves = [x for x,letter in enumerate(board) if letter == ' ' and x!=0]
    move = 0

    for let in ['O','X']:
        for i in possibleMoves:
            boardClone = board[:]
            boardClone[i] = let
            if isWinner(boardClone, let):
                move = i
                return move

    openCorner = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            openCorner.append(i)
    if len(openCorner) > 0:
        move = selectRandom(openCorner)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    openEdges = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            openEdges.append(i)
    if len(openEdges) > 0:
        move = selectRandom(openEdges)

    return move


def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def main():
    print("LETS PLAY TIC TAC TOE")
    printBoard(board)
    while not (isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print("Sorry, Computer won the Game")
            break

        if not(isWinner(board, 'X')):
            move = compMove()
            if move==0:
                print("Game Tied!")
            else:
                insertLetter('O', move)
                print("Computer Placed an \'O\' in position",move,':')
                printBoard(board)
        else:
            print("Congratulations, you won the Game")
            break

    if isBoardFull(board):
        print("Game Tied!")

while True:
    answer = input('Do you want to play again? (Y/N)')
    if answer.lower() == 'y' or answer.lower == 'yes':
        board = [' ' for x in range(10)]
        print('-----------------------------------')
        main()
    else:
        break
