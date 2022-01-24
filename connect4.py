board = []
cols = [" ", 1, 2, 3, 4, 5, 6, 7]
rows = [6, 6, 6, 6, 6, 6, 6]
players = [""]
colors = ["", "R", "B"]


def connect4():
    init()
    printBoard()
    turns = 0
    p = 1
    while 1:
        col = -1
        while 1:
            turns += 1
            col = int(input(players[p] + " (team " + colors[p] + ") what column would you like to put your piece in? ")) - 1
            if rows[col] >= 0:
                break
            print("Invalid choice, pick a different column")
        board[rows[col]][col] = colors[p]
        rows[col] -= 1
        printBoard()
        if checkWin():
            break
        p *= -1
        if turns >= 49:
            print("It's a tie!")
            return False

    print("Congratulations", players[p] + "!")
    return True

def printBoard():
    for i in range(7):
        print('|', end=' ')
        for j in range(7):
            print(board[i][j], end=' ')
        print('|')
    for i in range(8):
        print(cols[i], end=' ')
    print()


def checkWin():
    return checkRow() or checkColumn() or checkDiagonal1() or checkDiagonal2()

def checkRow():
    for r in range(7):
        for c in range(4):
            if board[r][c] != '.':
                if board[r][c] == board[r][c + 1] and board[r][c + 2] == board[r][c + 1] and board[r][c + 3] == board[r][c + 2]:
                    return True
    return False

def checkColumn():
    for r in range(3, 7):
        for c in range(7):
            if board[r][c] != '.':
                if board[r][c] == board[r - 1][c] and board[r - 1][c] == board[r - 2][c] and board[r - 2][c] == board[r - 3][c]:
                    return True
    return False

def checkDiagonal1():
    for r in range(3, 7):
        for c in range(4):
            if board[r][c] != '.':
                if board[r][c] == board[r - 1][c + 1] and board[r - 1][c + 1] == board[r - 2][c + 2] and board[r - 2][c + 2] == board[r - 3][c + 3]:
                    return True
    return False


def checkDiagonal2():
    for r in range(4):
        for c in range(4):
            if board[r][c] != '.':
                if board[r][c] == board[r + 1][c + 1] and board[r + 1][c + 1] == board[r + 2][c + 2] and board[r + 2][c + 2] == board[r + 3][c + 3]:
                    return True
    return False


def init():
    k = 0
    for i in range(7):
        board.append([])
        for j in range(7):
            board[i].append('.')
            k += 1
    players.append(input("What is the name of the player 1? "))
    print(players[1], "you will be on the Red team (denoted with the red pieces on the board)")
    players.append(input("What is the name of the player 2? "))
    print(players[-1], "you will be on the Blue team (denoted with the blue pieces on the board)")