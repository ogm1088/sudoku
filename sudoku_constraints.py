# sudoku_constraints.py

import copy

def is_valid(board, row, col, num):
    """
    Checks if placing a number (num) at a specific position (row, col) on the board is valid.
    Returns False if the number is already present in the same row, column, or 3x3 subgrid.
    """
    # Check row for duplicate
    if num in board[row]: 
        return False
    # Check column for duplicate
    if num in [board[i][col] for i in range(9)]:  
        return False
    # Check 3x3 subgrid for duplicate
    box_start_row, box_start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(box_start_row, box_start_row + 3):
        for j in range(box_start_col, box_start_col + 3):
            if board[i][j] == num:
                return False
    return True

def forward_checking(board, domains, row, col, num):
    """
    Applies forward checking after assigning a number (num) to a cell at (row, col).
    Removes num from the domain of cells in the same row, column, and 3x3 subgrid.
    """
    new_domains = copy.deepcopy(domains)  # Create a copy of domains to avoid mutating the original
    for i in range(9):
        # Remove num from the domain of cells in the same row and column
        if num in new_domains[row][i]:
            new_domains[row][i].remove(num)
        if num in new_domains[i][col]:
            new_domains[i][col].remove(num)
    # Remove num from the domain of cells in the same 3x3 subgrid
    box_start_row, box_start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(box_start_row, box_start_row + 3):
        for j in range(box_start_col, box_start_col + 3):
            if num in new_domains[i][j]:
                new_domains[i][j].remove(num)
    return new_domains
