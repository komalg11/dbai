def solve_n_queens(n):
    def backtrack(row):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if all(board[i] != col and board[i] - i != col - row and board[i] + i != col + row for i in range(row)):
                board[row] = col
                backtrack(row + 1)

    board = [-1] * n
    solutions = []
    backtrack(0)
    return solutions

def print_solution(solutions):
    for board in solutions:
        for row in board:
            print(" ".join('Q' if i == row else '.' for i in range(len(board))))
        print()

n = int(input("Enter the number of queens: "))
solutions = solve_n_queens(n)
print(f"Found {len(solutions)} solution(s) for {n}-queens problem:")
print_solution(solutions)


'''
1.Check Safety: For each queen, check if placing it on a specific row and column is safe:
    Make sure no other queens are in the same column.
    Check the diagonals to ensure no queens are positioned there, as they would attack each other.
2.Solve with Backtracking:
    Start with an empty chessboard.
    Try to place a queen in each row, one by one:
        For each row, attempt to place the queen in each column.
        If it’s safe, place the queen and move to the next row.
        If placing the queen leads to a solution, save it.
        If not, remove the queen and try the next column (backtracking).
        Repeat this process until you find all possible solutions.
3.Display Solutions:
    For each solution, print the board, showing queens as "Q" and empty spots as ".".
4.Run the Program:
    Ask the user for the number of queens.
    If the input is valid and greater than 3, run the backtracking solution.
    Print each solution or notify if none are found.
'''
