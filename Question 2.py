def solve_sudoku(board):
    def is_valid(num, row, col):
        # Check if the number is not present in the current row, column, and 3x3 sub-grid
        return (
            num not in board[row] and
            all(num != board[i][col] for i in range(9)) and
            all(num != board[i // 3 + 3 * (row // 3)][j // 3 + 3 * (col // 3)] for i in range(9) for j in range(9)
        ) )

    def backtrack():
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for num in map(str, range(1, 10)):
                        if is_valid(num, i, j):
                            board[i][j] = num
                            if backtrack():
                                return True
                            board[i][j] = '.'  # If the current configuration is invalid, backtrack
                    return False
        return True

    backtrack()

# Example usage:
input_board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

solve_sudoku(input_board)

# Print the solved Sudoku board
for row in input_board:
    print(row)