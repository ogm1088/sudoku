# sudoku_solver.py

from sudoku_constraints import is_valid, forward_checking

def get_unassigned_var(board, domains):
    """
    Selects an unassigned variable (empty cell) using the MRV (Minimum Remaining Values) heuristic.
    If multiple cells have the same domain size, selects the first in left-to-right, top-to-bottom order.
    """
    min_len = float('inf')  # Track the smallest domain size
    candidates = []  # List to store cells with minimum domain size
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Only consider unassigned cells
                domain_size = len(domains[row][col])
                if domain_size < min_len:
                    min_len = domain_size
                    candidates = [(row, col)]
                elif domain_size == min_len:
                    candidates.append((row, col))
    return sorted(candidates)[0]  # Choose the first candidate in left-to-right, top-to-bottom order

def get_degree(board, row, col):
    """
    Calculates the degree of a variable at (row, col).
    The degree is the number of unassigned neighboring cells in the row, column, and 3x3 subgrid.
    """
    degree = 0
    # Check row and column neighbors
    for i in range(9):
        if i != col and board[row][i] == 0:
            degree += 1
        if i != row and board[i][col] == 0:
            degree += 1
    # Check 3x3 subgrid neighbors
    box_start_row, box_start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(box_start_row, box_start_row + 3):
        for j in range(box_start_col, box_start_col + 3):
            if (i != row or j != col) and board[i][j] == 0:
                degree += 1
    return degree

def backtracking(board, domains, assignments=[]):
    """
    Performs backtracking search with forward checking to solve the Sudoku puzzle.
    Prints the first 4 variable assignments for tracking.
    """
    if all(all(cell != 0 for cell in row) for row in board):  # Puzzle is solved
        return board

    # Select an unassigned cell using MRV heuristic
    row, col = get_unassigned_var(board, domains)
    domain_size = len(domains[row][col])
    degree = get_degree(board, row, col)

    for num in sorted(domains[row][col]):  # Try each value in the cell's domain in increasing order
        if is_valid(board, row, col, num):  # Check if placing the number is valid
            board[row][col] = num
            assignments.append((row, col, domain_size, degree, num))  # Track assignment

            # Print the first 4 assignments
            if len(assignments) <= 4:
                print(f"Assignment {len(assignments)} - Variable: ({row},{col}), Domain Size: {domain_size}, Degree: {degree}, Value: {num}")

            new_domains = forward_checking(board, domains, row, col, num)  # Apply forward checking
            result = backtracking(board, new_domains, assignments)  # Recursive call
            if result:  # If a solution is found, return it
                return result
            board[row][col] = 0  # Reset cell on backtrack

    return None  # Return None if no solution is possible from this configuration
