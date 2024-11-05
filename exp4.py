from random import choice
from math import inf

board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def Gameboard(board):
    chars = {1: 'X', -1: 'O', 0: ' '}
    for row in board:
        print('|' + '|'.join(f' {chars[cell]} ' for cell in row) + '|')
    print('===============')

def Clearboard(board):
    for x in range(3):
        for y in range(3):
            board[x][y] = 0

def winningPlayer(b, p):
    return [p]*3 in [[b[0][0], b[0][1], b[0][2]], [b[1][0], b[1][1], b[1][2]], [b[2][0], b[2][1], b[2][2]], 
                     [b[0][0], b[1][0], b[2][0]], [b[0][1], b[1][1], b[2][1]], [b[0][2], b[1][2], b[2][2]], 
                     [b[0][0], b[1][1], b[2][2]], [b[0][2], b[1][1], b[2][0]]]

def gameWon(board):
    return winningPlayer(board, 1) or winningPlayer(board, -1)

def printResult(board):
    if winningPlayer(board, 1): print('X has won!')
    elif winningPlayer(board, -1): print('O\'s have won!')
    else: print('Draw')

def blanks(board):
    return [[x, y] for x in range(3) for y in range(3) if board[x][y] == 0]

def setMove(board, x, y, player):
    board[x][y] = player

def playerMove(board):
    while True:
        move = int(input('Enter a number between 1-9: ')) - 1
        x, y = move // 3, move % 3
        if board[x][y] == 0:
            setMove(board, x, y, 1)
            break
        print('Invalid Move! Try again!')
    Gameboard(board)

def abminimax(board, depth, alpha, beta, player):
    if depth == 0 or gameWon(board):
        return [-1, -1, (10 if winningPlayer(board, 1) else -10) if gameWon(board) else 0]
    best = [-1, -1, -inf if player == 1 else inf]
    for cell in blanks(board):
        setMove(board, cell[0], cell[1], player)
        score = abminimax(board, depth - 1, alpha, beta, -player)
        score[0], score[1] = cell
        setMove(board, cell[0], cell[1], 0)
        if player == 1:
            if score[2] > best[2]: best = score
            alpha = max(alpha, best[2])
        else:
            if score[2] < best[2]: best = score
            beta = min(beta, best[2])
        if beta <= alpha: break
    return best

def o_comp(board):
    if len(blanks(board)) == 9:
        setMove(board, choice(range(3)), choice(range(3)), -1)
    else:
        result = abminimax(board, len(blanks(board)), -inf, inf, -1)
        setMove(board, result[0], result[1], -1)
    Gameboard(board)

def makeMove(board, player):
    if player == 1: playerMove(board)
    else: o_comp(board)

def pvc():
    Clearboard(board)
    currentPlayer = 1 if int(input('Enter to play 1st or 2nd: ')) == 1 else -1
    while not (gameWon(board) or len(blanks(board)) == 0):
        makeMove(board, currentPlayer)
        currentPlayer *= -1
    printResult(board)

# Driver Code
pvc()

'''
1.Initialize the Game Board: Set up a 3x3 grid where each cell starts empty.
2.Display the Game Board: For each cell, display an "X" if occupied by the player, "O" if occupied by the computer, and an empty space if unoccupied.
3.Clear the Board: Reset the game by clearing all cells to make them empty.
4.Check for Winning Condition: Define the winning patterns (rows, columns, and diagonals). A player wins if they occupy any one of these patterns completely.
5.Game Result Display: After the game finishes, show whether the player won, the computer won, or if it was a draw.
6.Identify Empty Cells: Check each cell in the grid, and if it’s empty, save its location. This helps in identifying possible moves.
7.Set a Move on the Board: Place the player's or computer's symbol in the specified cell.
8.Player's Turn: Ask the player to enter a move between 1 and 9. Convert this input to a cell position and place their symbol if the cell is empty. If it’s occupied, ask for a new input.
9.Computer's Turn (Optimal Move): Use the minimax algorithm:
    Simulate all possible moves by the computer and player.
    Score each possible outcome:
        If the player wins, score is -10.
        If the computer wins, score is +10.
        If it’s a draw, score is 0.
    Choose the move that maximizes the computer's chance of winning and minimizes the player’s.
    Place the computer's symbol in the best position.
10.Switch Turns: Alternate turns between the player and the computer until someone wins or there are no empty cells.
11.Play the Game: Allow the player to choose if they want to play first or second. Continue the game loop, switching turns until a win or a draw occurs. Display the final result.
12.Start Game: Begin the game with the above steps and handle the entire flow until the game concludes.
'''