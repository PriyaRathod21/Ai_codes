def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == row - i:
            return False
    return True

def solve_n_queens(board, row, n):
    if row == n:
        #print(board)
        return True
    
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            if solve_n_queens(board, row + 1, n):
                return True
            board[row] = -1
    return False

def n_queens_backtracking(n):
    board = [-1] * n
    if not solve_n_queens(board, 0, n):
        print("No solution found")
    else:
        print("Solution found:")
        print(board)
        printboard(board, n)

def printboard(board, n):
	print("\nBoard: ")
	for i in range(n):
		print("\n")
		for j in range(n):
			if(board[i] == j):
				print(" Q ", end="")
			else:
				print(" - ", end="") 

n = int(input("Enter no. of Queens: "))
n_queens_backtracking(n)

