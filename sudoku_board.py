# sudoku_board.py

def print_sudoku(board):
    """Prints the Sudoku board in a human-readable format, with empty cells as dots."""
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))
    print()

def initialize_domains(board):
    """
    Initializes domains for each cell.
    For cells that already have a number, the domain is that single number.
    For empty cells, the domain is [1-9].
    """
    return [[[num] if num != 0 else list(range(1, 10)) for num in row] for row in board]
