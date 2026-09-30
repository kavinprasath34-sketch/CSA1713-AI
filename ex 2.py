# 8-Queens Problem using Backtracking

N = 8

def is_safe(board, row, col):
    # Check the same column
    for i in range(row):
        if board[i] == col:
            return False

        # Check diagonals
        if abs(board[i] - col) == abs(i - row):
            return False

    return True


def solve(board, row):
    # All queens are placed
    if row == N:
        print_board(board)
        return True

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col

            if solve(board, row + 1):
                return True

            # Backtrack
            board[row] = -1

    return False


def print_board(board):
    for row in range(N):
        for col in range(N):
            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


# Main program
board = [-1] * N

if not solve(board, 0):
    print("No solution exists")
