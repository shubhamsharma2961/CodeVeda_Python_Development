def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1
    return True

def solve_nqueens(board, row, n):
    if row == n: 
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve_nqueens(board, row + 1, n):
                return True
            board[row][col] = 0 
    return False

def print_board(board, n):
    for i in range(n):
        row = ""
        for j in range(n):
            row += "Q " if board[i][j] == 1 else ". "
        print(row)
    print()

n = int(input("Enter number of queens (N): "))
board = [[0 for _ in range(n)] for _ in range(n)]

if solve_nqueens(board, 0, n):
    print(f"One solution for {n}-Queens:")
    print_board(board, n)
else:
    print("No solution exists")
