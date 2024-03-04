def printSolution(board, N):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end =" ")
        
        print()

def isSafe (board, row, col, N):
    i, j = row, col

    # Checking if the left (main) diagonal has any queen.
    while (i > -1 and j > -1):
        # If a queen is found, return 'false'
        if (board[i][j] == 'Q'):
            return False

        i -= 1
        j -= 1
    

    i, j = row, col
    # Checking if the right (secondary) diagonal has any queen.
    while (i > -1 and j < N):
        # If a queen is found, return 'false'
        if (board[i][j] == 'Q'):
            return False

        i -= 1
        j += 1
    
    i, j = row, col
    # Checking if the columns (col) has any queen.
    while (i > -1):
        # If a queen is found, return 'false'
        if (board[i][j] == 'Q'):
            return False

        i -= 1
    
    # If we have reached here, it means it is safe
    return True


# Function to check whether solution exists
# for N queen problem, for the provided N.
# board -> Chess Board of dimensions N*N
# N -> Size of the chess board
# row -> Row number in which we will try to place the queen. It's value ranges from [0, N-1].
def solutionExists(board, N, row):
    # If we have placed a queen in all the rows, it means solution exists.
    if (row >= N):
        return True
    
    # Trying to place the queen in every cell
    for col in range(N):
        if (isSafe(board, row, col, N)):
            # If found true, place a queen 
            board[row][col] = 'Q'
            
            if (solutionExists(board, N, row + 1)):
                return True

            # This statement will execute only if placing queen in cell (row, col) is not possible
            board[row][col] = '.'
        
    # Returning false if we do not find any valid Solution.
    return False

def solveNQueenProblem(N):
    # Defining the board
    board = []
    for i in range(N):
        temp = []
        # '.' Represents empty cell
        for j in range(N):
            temp.append('.')

        board.append(temp)
    
    # If the solution do not exists
    if (solutionExists(board, N, 0) == False):
        print("No solution exists for N : ", N)
     
    # Otherwise, if the solution exists.
    else:
        print("One of the possible solution for N : ", N, "is : ")
        printSolution(board, N)

N = int(input("Enter the no. of Queens : "))
solveNQueenProblem(N)
