# sudoku_solver.py

from sudoku_constraints import is_valid, forward_checking

def get_unassigned_var(board, domains):
    """
    Selects an unassigned variable (empty cell) using the MRV (Minimum Remaining Values) heuristic.
    If multiple cells have the same MRV, selects the first in left-to-right, top-to-bottom order.
    """
    min_len = float('inf')  # Track the smallest domain size
    candidates = []  # List to store cells with minimum domain size
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Only consider unassigned cells
                domain_size = len(domains[row][col])
                if domain_size < min_len:
                    min_len = domain_size
                    candidates = [(row, col)]  # New candidate with smaller domain size
                elif domain_size == min_len:
                    candidates.append((row, col))  # Add candidate if domain size matches minimum
    return sorted(candidates)[0]  # Choose the first candidate in left-to-right, top-to-bottom order

def backtracking(board, domains):
    """
    Performs backtracking search with forward checking to solve the Sudoku puzzle.
    Returns the solved board if a solution is found, or None if there is no solution.
    """
    # Base case: if all cells are filled, the puzzle is solved
    if all(all(cell != 0 for cell in row) for row in board):
        return board

    # Select an unassigned cell using MRV heuristic
    row, col = get_unassigned_var(board, domains)
    for num in sorted(domains[row][col]):  # Try each value in the cell's domain in increasing order
        if is_valid(board, row, col, num):  # Check if placing the number is valid
            board[row][col] = num  # Place the number on the board
            new_domains = forward_checking(board, domains, row, col, num)  # Apply forward checking
            result = backtracking(board, new_domains)  # Recursively solve the rest of the puzzle
            if result:  # If a solution is found, return it
                return result
            board[row][col] = 0  # Reset cell on backtrack if no solution is found
    return None  # Return None if no solution is possible from this configuration
