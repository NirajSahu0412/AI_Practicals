def isAttacked(i, j, board):
    n = len(board)
    for k in range(n):
        if board[i][k] == 1 or board[k][j] == 1:
            return True

    for k in range(n):
        for l in range(n):
            if (k + l == i + j or k - l == i - j) and board[k][l] == 1:
                return True

    return False


def nQueen(n):
    board = [[0] * n for _ in range(n)]

    def solve(p):
        if p == 0:
            return True

        for i in range(n):
            for j in range(n):
                if not isAttacked(i, j, board) and board[i][j] != 1:
                    board[i][j] = 1
                    if solve(p - 1):
                        return True
                    board[i][j] = 0
        return False

    if solve(n):
        for row in board:
            print(row)
    else:
        print("No solution found.")


print("Enter the No. of Queens:")
n = int(input())
nQueen(n)

# Output:
# Enter the No. of Queens:
# 4
# [0, 1, 0, 0]
# [0, 0, 0, 1]
# [1, 0, 0, 0]
# [0, 0, 1, 0]
