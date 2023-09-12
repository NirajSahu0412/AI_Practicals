print("Enter the No. of Queens : ")
n = int(input())

#Chess Board
board = [[0] * n for _ in range(n)]

def isAttacked(i, j):
    for k in range(0, n):
        #Checking rows and column
        if (board[i][j] == 1):
            return True

    for k in range(0, n):
        for l in range(0, n):
            #Checking Diagonals
            if (k + l == i + j) or (k - l == i - j):
                if(board[k][l] == 1):
                    return True
        return False

def nQueen(p):
    if(p == 0):
        return True
    
    for i in range(0, n):
        for j in range(0, n):
            if(not(isAttacked(i, j))) and (board[i][j] != 1):
                board[i][j] == 1
                if (nQueen(p - 1) == True):
                    return True
                board[i][j] = 0
        return False
    
nQueen(n)
for i in board:
    print(i)