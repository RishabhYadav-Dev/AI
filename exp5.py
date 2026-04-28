# Title: To implement any game in Python
# Aim: Program on game playing algorithm
#Code
# Create an empty board (9 positions)
board = [" "] * 9

# Starting player
player = "X"


def display_board():
    """Prints the board in 3x3 format"""
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        print("-" * 11)


def check_status():
    """Checks if any player has won"""
    # All possible winning combinations
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),   # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),   # columns
        (0, 4, 8), (2, 4, 6)               # diagonals
    ]

    for a, b, c in wins:
        # Check if same symbol and not empty
        if board[a] == board[b] == board[c] != " ":
            return "win"

    return None


# Game loop (maximum 9 moves)
for move in range(1, 10):

    # Show current board
    display_board()

    try:
        # Take user input
        pos = int(input(f"Move {move} - Player {player}, enter (0-8): "))

        # Check if position already filled
        if board[pos] != " ":
            print("Spot taken! Try again.")
            continue

        # Place player's symbol
        board[pos] = player

    except (ValueError, IndexError):
        print("Invalid input! Enter 0-8.")
        continue

    # Check for win only after at least 5 moves
    if move >= 5:
        status = check_status()

        if status == "win":
            display_board()
            print(f"GAME OVER: Player {player} Wins!")
            break

    # If last move and no winner → draw
    if move == 9:
        display_board()
        print("GAME OVER: It's a Draw!")
        break
    else:
        print("Status: No winner yet, keep playing...")

    # Switch player
    player = "O" if player == "X" else "X"








#output
#    |   |   
# -----------
#    |   |   
# -----------
#    |   |   
# -----------
# Move 1 - Player X, enter (0-8): 0
# Status: No winner yet, keep playing...
#  X |   |   
# -----------
#    |   |   
# -----------
#    |   |   
# -----------
# Move 2 - Player O, enter (0-8): 2
# Status: No winner yet, keep playing...
#  X |   | O 
# -----------
#    |   |   
# -----------
#    |   |   
# -----------
# Move 3 - Player X, enter (0-8): 4
# Status: No winner yet, keep playing...
#  X |   | O 
# -----------
#    | X |   
# -----------
#    |   |   
# -----------
# Move 4 - Player O, enter (0-8): 4
# Spot taken! Try again.
#  X |   | O 
# -----------
#    | X |   
# -----------
#    |   |   
# -----------
# Move 5 - Player O, enter (0-8): 2
# Spot taken! Try again.
#  X |   | O 
# -----------
#    | X |   
# -----------
#    |   |   
# -----------
# Move 6 - Player O, enter (0-8): 1
# Status: No winner yet, keep playing...
#  X | O | O 
# -----------
#    | X |   
# -----------
#    |   |   
# -----------
# Move 7 - Player X, enter (0-8): 8
#  X | O | O 
# -----------
#    | X |   
# -----------
#    |   | X 
# -----------



# Title: To implement any game in Python
# Aim: Program on game playing algorithm

#Theory:

# Tic-Tac-Toe is a classic problem in Artificial Intelligence, used to demonstrate:

# Game playing strategies
# State space representation
# Decision making

# It is a deterministic, turn-based, zero-sum game, where:

# One player’s gain = other player’s loss
# 🔹 AI Concepts Involved
# State Space → All possible board configurations
# Initial State → Empty board
# Goal State → Player wins or draw
# Operators → Placing X or O in empty cells
# Utility Function:
# +1 → Win
# 0 → Draw
# -1 → Loss

# Algorithm
# START
# Initialize empty board
# Set current player = X

# REPEAT until game ends:
#     Display current state

#     Get valid move from player
#     Apply move (state transition)

#     IF goal state reached:
#         Declare winner
#         STOP

#     IF no moves left:
#         Declare draw
#         STOP

#     Switch player

# END
