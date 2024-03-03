def printSolution(board, N):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()

def isSafe(board, row, col, N):
    i, j = row, col

    while (i > -1 and j > -1):
        if (board[i][j] == 'Q'):
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while (i > -1 and j < N):
        if (board[i][j] == 'Q'):
            return False
        i -= 1
        j += 1

    i, j = row, col
    while (i > -1):
        if (board[i][j] == 'Q'):
            return False
        i -= 1

    return True


def solutionExists(board, N, row):
    if (row >= N):
        return True

    for col in range(N):
        if (isSafe(board, row, col, N)):
            board[row][col] = 'Q'
            print("Placing Queen at row:", row, "column:", col)
            printSolution(board, N)  # Print board after placing the queen
            print()  
            if (solutionExists(board, N, row + 1)):
                return True
            board[row][col] = '.'  # Backtrack
    return False


def solveNQueenProblem(N):
    board = []
    for i in range(N):
        temp = []
        for j in range(N):
            temp.append('.')
        board.append(temp)

    if (solutionExists(board, N, 0) == False):
        print("No solution exists for N =", N)


N = int(input("Enter the no. of Queens : "))
solveNQueenProblem(N)
