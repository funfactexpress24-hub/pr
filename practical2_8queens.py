N = 8

def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_queens(board, row):
    if row == N:
        print_solution(board)
        return True
    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            if solve_queens(board, row + 1):
                return True
            board[row] = -1
    return False

def print_solution(board):
    print("\nOne possible 8-Queens arrangement:\n")
    for i in range(N):
        row = ''.join(' Q ' if board[i] == j else ' . ' for j in range(N))
        print(row)
    print("\nColumn positions:", board)

board = [-1] * N
solve_queens(board, 0)
