# Tic Tac Toe game

# Importing modules
import os
import sys

# Clear terminal - cross-platform
def clear_terminal() -> None:
    if sys.platform in ('linux', 'darwin'):  # macOS is also included here
        os.system('clear')
    elif sys.platform == 'win32':
        os.system('cls')
    else:
        print("Unsupported OS")
        
# Initialize board
def init_board() -> list:
    # Sets a 3x3 board with empty spaces
    board: list = [[' ' for _ in range(3)] for _ in range(3)]
    return board


# Menu - print, input, match
def menu() -> None:
    print("1. Play")
    print("2. Exit")
    choice: int = int(input("Choose an option: "))
    match choice:
        case 1:
            print("Let's play!")
            play()
        case 2:
            quit()
        case _:
            clear_terminal()
            print("Invalid choice")
            menu()

# Print board
def print_board(board: list) -> None:
    print("--------")
    # row is declared with the for loop, magik!
    for row in board: 
        print(" |".join(row))
        print("--------")

# A player's turn 
def player_turn(board: list, player_turn: int) -> None:
    row: int = int(input("Enter row: "))
    col: int = int(input("Enter column: "))
    if player_turn == 1:
        board[row][col] = 'X'
    if player_turn == 2:
        board[row][col] = 'O'

# Main play loop
def play() -> None:
    clear_terminal()
    board = init_board()
    print_board(board)
    player_turn : int = 1 # Player 1 starts
    while True:
        player_turn(board, player_turn)
        print_board(board)
        player_turn = 2 if player_turn == 1 else 1

# Cya !
def quit() -> None:
    print("Bye byee")
    exit(0)

# Main loop
menu()