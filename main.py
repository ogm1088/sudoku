# main.py

import time
from sudoku_board import print_sudoku, initialize_domains
from sudoku_solver import backtracking

def solve_sudoku(puzzles):
    """
    Solves each puzzle in the list of puzzles using backtracking with forward checking.
    If a solution is found, it is printed; if it takes more than 1 hour, it stops and moves on.
    """
    for i, puzzle in enumerate(puzzles):
        print(f"Solving puzzle {i + 1}...")
        start_time = time.time()  # Track the start time for each puzzle
        domains = initialize_domains(puzzle)  # Initialize domains based on the puzzle
        solution = backtracking(puzzle, domains)  # Attempt to solve the puzzle
        if solution:
            print(f"Solution for puzzle {i + 1}:")
            print_sudoku(solution)
        else:
            print(f"Puzzle {i + 1} could not be solved within the time limit.")
        if time.time() - start_time > 3600:  # If the puzzle takes more than 1 hour, stop solving
            print("Time limit exceeded.")
            break

if __name__ == "__main__":
    # List of puzzles to solve
    puzzles = [
        [
            [0, 0, 1, 0, 0, 2, 0, 0, 0],
            [0, 0, 5, 0, 0, 6, 0, 3, 0],
            [4, 6, 0, 0, 0, 5, 0, 0, 0],
            [0, 0, 0, 1, 0, 4, 0, 0, 0],
            [6, 0, 0, 8, 0, 0, 1, 4, 3],
            [0, 0, 0, 0, 9, 0, 5, 0, 8],
            [8, 0, 0, 0, 4, 9, 0, 5, 0],
            [1, 0, 0, 3, 2, 0, 0, 0, 0],
            [0, 0, 9, 0, 0, 0, 3, 0, 0]
        ],
        [
            [0, 0, 5, 0, 1, 0, 0, 0, 0],
            [0, 0, 2, 0, 0, 4, 0, 3, 0],
            [1, 0, 9, 0, 0, 0, 2, 0, 6],
            [2, 0, 0, 0, 3, 0, 0, 0, 0],
            [0, 4, 0, 0, 0, 0, 7, 0, 0],
            [5, 0, 0, 0, 0, 7, 0, 0, 1],
            [0, 0, 0, 6, 0, 3, 0, 0, 0],
            [0, 6, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 7, 0, 0, 5, 0]
        ],
        [
            [6, 7, 0, 0, 0, 0, 0, 0, 0],
            [0, 2, 5, 0, 0, 0, 0, 0, 0],
            [0, 9, 0, 5, 6, 0, 2, 0, 0],
            [3, 0, 0, 0, 8, 0, 9, 0, 0],
            [0, 0, 0, 0, 0, 0, 8, 0, 1],
            [0, 0, 0, 4, 7, 0, 0, 0, 0],
            [0, 0, 8, 6, 0, 0, 0, 9, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0],
            [1, 0, 6, 0, 5, 0, 0, 7, 0]
        ]
    ]
    
    solve_sudoku(puzzles)  # Solve each puzzle in sequence
