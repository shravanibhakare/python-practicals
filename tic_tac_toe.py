import random

def tic_tac_toe(p1, p2):
    player1, player2 = p1, p2
    hor, ver = 0, 0

    print("Do you want to set grid?")
    opinion = input().strip().lower()

    if opinion == "yes":
        print("Enter the size of grid:")
        hor = int(input("Horizontal: "))
        ver = int(input("Vertical: "))
        display(hor, ver)  
    else:
        hor, ver = 3, 3 
        display(3, 3)  

    board = [[" " for _ in range(ver)] for _ in range(hor)]

    current_player = random.choice([p1, p2])
    print(f"{current_player} will start the game!\n")

    player_moves = []  
  
    for _ in range(hor * ver):
        print(f"\n{current_player}'s turn:")
        row, col = get_player_input(hor, ver, board)

        
        move = {"player": current_player, "row": row, "col": col}
        player_moves.append(move) 

        
        board[row][col] = "X" if current_player == p1 else "O"
        display_board(board)  

        if check_winner(board):
            print(f"\n{current_player} wins!")
            print(f"Moves: {player_moves}")
            return

        current_player = p2 if current_player == p1 else p1

    print("\nIt's a draw!")
    print(f"Final Moves: {player_moves}")

def display(horizontal, vertical):
    """Display an empty grid based on given dimensions."""
    for _ in range(horizontal):
        print(" --- " * vertical)
        print("|    " * (vertical + 1))
    print(" --- " * vertical)

def display_board(board):
    """Display the current state of the board."""
    for row in board:
        print(" ---" * len(row))
        print("| " + " | ".join(row) + " |")
    print(" ---" * len(board[0]))

def get_player_input(hor, ver, board):
   
    while True:
        row_input = input(f"Enter row (1-{hor}): ")
        col_input = input(f"Enter column (1-{ver}): ")

        if row_input.isdigit() and col_input.isdigit():
            row = int(row_input) - 1
            col = int(col_input) - 1

            if 0 <= row < hor and 0 <= col < ver and board[row][col] == " ":
                return row, col
            else:
                print("Invalid move! The cell is already occupied or out of bounds.")
        else:
            print("Please enter valid numbers.")

def check_winner(board):
    
    n = len(board)
    m = len(board[0])


    for row in board:
        if row.count(row[0]) == m and row[0] != " ":
            return True

    for col in range(m):
        if all(board[row][col] == board[0][col] != " " for row in range(n)):
            return True

    if all(board[i][i] == board[0][0] != " " for i in range(n)):
        return True

    if all(board[i][m - i - 1] == board[0][m - 1] != " " for i in range(n)):
        return True

    return False

tic_tac_toe("Shravani", "Anant")

