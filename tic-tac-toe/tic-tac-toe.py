import sys


def print_board(board):
    """Prints the current state of the board."""
    print()
    # Display the board in a 3x3 grid format with separators
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def check_win(board, player):
    """Checks if the given player has won."""
    # Define all possible winning combinations (rows, columns, diagonals)
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]
    # Check if any winning combination has all three positions occupied by the same player
    return any(board[a] == board[b] == board[c] == player for a, b, c in wins)


def check_draw(board):
    """Checks if the board is full without a winner."""
    # Return True if all spaces are filled (no empty spaces remain)
    return all(space != ' ' for space in board)


def get_move(board, player):
    """Prompts the player to enter a move and validates it."""
    while True:
        try:
            # Get player input and convert to 0-based index
            idx = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            # Check if the position is within valid range (0-8)
            if idx < 0 or idx > 8:
                print("Invalid position. Choose a number between 1 and 9.")
            # Check if the chosen position is already occupied
            elif board[idx] != ' ':
                print("That position is already taken. Try again.")
            else:
                # Valid move found, return the index
                return idx
        except ValueError:
            # Handle non-numeric input
            print("Invalid input. Please enter a number between 1 and 9.")


def main():
    # Initialize empty board with 9 spaces
    board = [' '] * 9
    # Start with player X
    current_player = 'X'

    # Display welcome message and board layout guide
    print("Welcome to Tic-Tac-Toe!")
    print("Positions are numbered 1 to 9 as follows:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")

    # Main game loop
    while True:
        # Display current board state
        print_board(board)
        # Get valid move from current player
        move = get_move(board, current_player)
        # Place player's mark on the board
        board[move] = current_player

        # Check if current player has won
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins! Congratulations!")
            break
        # Check if the game is a draw
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch to the other player for next turn
        current_player = 'O' if current_player == 'X' else 'X'

    print("Game over.")


# Entry point of the program
if __name__ == '__main__':
    try:
        # Start the game
        main()
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        print("\nGame interrupted. Goodbye!")
        sys.exit()