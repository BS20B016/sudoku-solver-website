def is_valid(board, row, col, num):
    for c in range(9):
        if board[row][c] == num:
            return False
    for r in range(9):
        if board[r][col] == num:
            return False
    block_row, block_col = 3 * (row // 3), 3 * (col // 3)
    for r in range(block_row, block_row + 3):
        for c in range(block_col, block_col + 3):
            if board[r][c] == num:
                return False
    return True

def find_empty_cell(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return r, c
    return None

def solve_sudoku(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True
    row, col = empty_cell
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False
