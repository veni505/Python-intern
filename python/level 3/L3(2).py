def print_board(board, N):
    for row in board:
        for cell in row:
            if cell == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

def is_safe(board, row, col, N):

    for i in range(col):
        if board[row][i] == 1:
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

def solve_nqueens(board, col, N):

    if col >= N:
        return True

    for row in range(N):

        if is_safe(board, row, col, N):
            board[row][col] = 1

            if solve_nqueens(board, col + 1, N):
                return True

            board[row][col] = 0

    return False

N = int(input("Enter the value of N: "))

board = [[0 for _ in range(N)] for _ in range(N)]

if solve_nqueens(board, 0, N):
    print("\nSolution Found:\n")
    print_board(board, N)
else:
    print("\nNo Solution Exists")
