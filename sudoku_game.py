from random import randint
from math import ceil

def display(grid):
    """Display the current Sudoku grid."""
    size = len(grid)
    hr_line = "---" * ((size * 2) - 2)
    print(hr_line)
    for row in range(size):
        for col in range(size):
            print(f"| {grid[row][col]} ", end='')
        print("|")
    print(hr_line)

def fill_grid(size):
    """Fill the Sudoku grid with valid numbers."""
    sudoku_state = [[0] * size for _ in range(size)]
    possibility = set(range(1, size + 1))

    for row in range(size):
        for col in range(size):
            availability = set(sudoku_state[row] + [r[col] for r in sudoku_state])
            candidates = list(possibility - availability)

            if candidates:
                sudoku_state[row][col] = candidates[randint(0, len(candidates) - 1)]
            else:
                return fill_grid(size)  # Retry filling the grid if stuck

    return sudoku_state

def initialize():
    """Initialize the Sudoku game with input validation."""
    print("Welcome to Sudoku!!")

    # Validate the grid size input
    while True:
        try:
            size = int(input("Enter the grid size: "))
            if size > 1:  # Grid size must be at least 2x2
                break
            else:
                print("Please enter a number greater than 1.")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

    state = fill_grid(size)

    game_levels = {
        1: ('Very Easy', 20), 
        2: ('Easy', 30), 
        3: ('Medium', 50), 
        4: ('Hard', 60), 
        5: ('Very Hard', 75)
    }

    print(f"There are {len(game_levels)} levels")
    for level, info in game_levels.items():
        print(f"Level {level}: {info[0]}")

    # Validate the difficulty level input
    while True:
        try:
            difficulty_level = int(input("Enter game level (1-5): "))
            if 1 <= difficulty_level <= 5:
                break
            else:
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

    hidden_fields = ceil(game_levels[difficulty_level][1] * size / 100)
    positions = []
    p = list(range(size * size))

    for _ in range(hidden_fields):
        popped = p.pop(randint(0, len(p) - 1))
        positions.append((popped // size, popped % size))

    for row, col in positions:
        state[row][col] = "X"

    return state, positions

def start_game(ss, positions):
    """Start the game and collect user inputs."""
    display(ss)
    for r, c in positions:
        while True:
            try:
                value = int(input(f"Enter a value for row {r + 1}, col {c + 1}: "))
                if 1 <= value <= len(ss):
                    ss[r][c] = value
                    break
                else:
                    print(f"Please enter a value between 1 and {len(ss)}.")
            except ValueError:
                print("Invalid input! Please enter a valid integer.")

def is_valid_solution(grid):
    """Check if the Sudoku solution is valid."""
    size = len(grid)
    possibility = set(range(1, size + 1))

    # Check rows
    for row in grid:
        if set(row) != possibility:
            return False

    # Check columns
    for col in range(size):
        column_values = [grid[row][col] for row in range(size)]
        if set(column_values) != possibility:
            return False

    return True

def stop_game(ss):
    """End the game and validate the solution."""
    print("Your solution is given below:")
    display(ss)

    if is_valid_solution(ss):
        print("Congratulations, you won!")
    else:
        print("Sorry, your solution is incorrect.")

def sudoku():
    """Main function to run the Sudoku game."""
    sudoku_state, positions = initialize()
    start_game(sudoku_state, positions)  # Grid position
    stop_game(sudoku_state)

# Start the game
sudoku()

