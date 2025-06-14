import tkinter as tk
from tkinter import messagebox
import sys
import random


class TicTacToeGUI:
    def __init__(self):
        # Initialize the main window
        self.root = tk.Tk()
        self.root.title("Tic-Tac-Toe")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        
        # Game state variables
        self.board = [' '] * 9
        self.current_player = 'X'
        self.buttons = []
        self.game_mode = 'human'  # 'human' for 2-player, 'cpu' for vs CPU
        self.human_player = 'X'   # Human always plays X
        self.cpu_player = 'O'     # CPU always plays O
        
        # Create the UI elements
        self.create_widgets()
        
    def create_widgets(self):
        """Create all UI elements including title, game board, and control buttons."""
        # Title label
        title_label = tk.Label(self.root, text="Tic-Tac-Toe", 
                              font=("Arial", 24, "bold"), pady=20)
        title_label.pack()
        
        # Game mode selection frame
        mode_frame = tk.Frame(self.root)
        mode_frame.pack(pady=10)
        
        tk.Label(mode_frame, text="Game Mode:", font=("Arial", 14)).pack()
        
        self.mode_var = tk.StringVar(value='human')
        mode_buttons_frame = tk.Frame(mode_frame)
        mode_buttons_frame.pack(pady=5)
        
        tk.Radiobutton(mode_buttons_frame, text="2 Players", variable=self.mode_var, 
                      value='human', font=("Arial", 12), command=self.change_mode).pack(side=tk.LEFT, padx=10)
        tk.Radiobutton(mode_buttons_frame, text="vs CPU", variable=self.mode_var, 
                      value='cpu', font=("Arial", 12), command=self.change_mode).pack(side=tk.LEFT, padx=10)
        
        # Current player display
        self.player_label = tk.Label(self.root, text=f"Current Player: {self.current_player}", 
                                    font=("Arial", 16), pady=10)
        self.player_label.pack()
        
        # Game board frame
        board_frame = tk.Frame(self.root, bg="black")
        board_frame.pack(pady=20)
        
        # Create 3x3 grid of buttons
        for i in range(3):
            for j in range(3):
                # Calculate button index (0-8)
                idx = i * 3 + j
                # Create button with click handler
                button = tk.Button(board_frame, text=" ", font=("Arial", 20, "bold"),
                                 width=4, height=2, bg="lightgray",
                                 command=lambda index=idx: self.make_move(index))
                button.grid(row=i, column=j, padx=2, pady=2)
                self.buttons.append(button)
        
        # Control buttons frame
        control_frame = tk.Frame(self.root)
        control_frame.pack(pady=20)
        
        # New game button
        new_game_btn = tk.Button(control_frame, text="New Game", font=("Arial", 12),
                                bg="lightblue", command=self.new_game)
        new_game_btn.pack(side=tk.LEFT, padx=10)
        
        # Quit button
        quit_btn = tk.Button(control_frame, text="Quit", font=("Arial", 12),
                           bg="lightcoral", command=self.quit_game)
        quit_btn.pack(side=tk.LEFT, padx=10)

    def change_mode(self):
        """Handle game mode change."""
        self.game_mode = self.mode_var.get()
        self.new_game()  # Reset game when mode changes

    def make_move(self, idx):
        """Handle button click - make a move at the specified position."""
        # Check if the position is already taken
        if self.board[idx] != ' ':
            messagebox.showwarning("Invalid Move", "That position is already taken!")
            return
        
        # In CPU mode, only allow human player to click
        if self.game_mode == 'cpu' and self.current_player == self.cpu_player:
            return
        
        # Make the move
        self.place_move(idx, self.current_player)
        
        # Check for game end
        if self.check_game_end():
            return
        
        # Switch to next player
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        self.update_player_display()
        
        # If it's CPU's turn, make CPU move after a short delay
        if self.game_mode == 'cpu' and self.current_player == self.cpu_player:
            self.root.after(500, self.cpu_move)  # 500ms delay for better UX

    def place_move(self, idx, player):
        """Place a move on the board and update the UI."""
        self.board[idx] = player
        self.buttons[idx].config(text=player, 
                               bg="lightgreen" if player == 'X' else "lightcoral",
                               state="disabled")

    def cpu_move(self):
        """Make a move for the CPU player using advanced AI algorithm."""
        # Use minimax algorithm for unbeatable AI
        move = self.minimax_move()
        self.place_move(move, self.cpu_player)
        
        # Check for game end
        if self.check_game_end():
            return
        
        # Switch back to human player
        self.current_player = self.human_player
        self.update_player_display()

    def minimax_move(self):
        """Find the best move using minimax algorithm with alpha-beta pruning."""
        best_score = float('-inf')
        best_move = None
        
        for i in range(9):
            if self.board[i] == ' ':
                # Try the move
                self.board[i] = self.cpu_player
                score = self.minimax(self.board, 0, False, float('-inf'), float('inf'))
                self.board[i] = ' '  # Undo the move
                
                if score > best_score:
                    best_score = score
                    best_move = i
        
        return best_move

    def minimax(self, board, depth, is_maximizing, alpha, beta):
        """
        Minimax algorithm with alpha-beta pruning.
        Returns the best score for the current position.
        """
        # Check terminal states
        if self.check_win(board, self.cpu_player):
            return 10 - depth  # Prefer faster wins
        elif self.check_win(board, self.human_player):
            return depth - 10  # Prefer slower losses
        elif self.check_draw(board):
            return 0
        
        if is_maximizing:
            # CPU's turn - maximize score
            max_score = float('-inf')
            for i in range(9):
                if board[i] == ' ':
                    board[i] = self.cpu_player
                    score = self.minimax(board, depth + 1, False, alpha, beta)
                    board[i] = ' '
                    max_score = max(score, max_score)
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        break  # Alpha-beta pruning
            return max_score
        else:
            # Human's turn - minimize score
            min_score = float('inf')
            for i in range(9):
                if board[i] == ' ':
                    board[i] = self.human_player
                    score = self.minimax(board, depth + 1, True, alpha, beta)
                    board[i] = ' '
                    min_score = min(score, min_score)
                    beta = min(beta, score)
                    if beta <= alpha:
                        break  # Alpha-beta pruning
            return min_score

    def find_winning_move(self, player):
        """Find a move that would result in a win for the given player."""
        # This method is now only used as backup/validation
        for i in range(9):
            if self.board[i] == ' ':
                # Try the move
                self.board[i] = player
                if self.check_win(self.board, player):
                    self.board[i] = ' '  # Undo the move
                    return i
                self.board[i] = ' '  # Undo the move
        return None

    def find_best_move(self):
        """Find the best strategic move for CPU (backup method)."""
        # This is now a fallback method, minimax should handle all cases
        # Priority order: center, corners, edges
        priority_positions = [4, 0, 2, 6, 8, 1, 3, 5, 7]
        
        for pos in priority_positions:
            if self.board[pos] == ' ':
                return pos
        
        # Fallback to random move (shouldn't happen)
        available_moves = [i for i in range(9) if self.board[i] == ' ']
        return random.choice(available_moves) if available_moves else None

    def check_game_end(self):
        """Check if the game has ended (win or draw) and handle accordingly."""
        # Check for win condition
        if self.check_win(self.board, self.current_player):
            if self.game_mode == 'cpu':
                winner_msg = "You win!" if self.current_player == self.human_player else "CPU wins!"
            else:
                winner_msg = f"Player {self.current_player} wins! Congratulations!"
            messagebox.showinfo("Game Over", winner_msg)
            self.disable_all_buttons()
            return True
        
        # Check for draw condition
        if self.check_draw(self.board):
            messagebox.showinfo("Game Over", "It's a draw!")
            return True
        
        return False

    def update_player_display(self):
        """Update the current player display label."""
        if self.game_mode == 'cpu':
            display_text = "Your turn" if self.current_player == self.human_player else "CPU's turn"
        else:
            display_text = f"Current Player: {self.current_player}"
        self.player_label.config(text=display_text)

    def check_win(self, board, player):
        """Checks if the given player has won."""
        # Define all possible winning combinations (rows, columns, diagonals)
        wins = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
            (0, 4, 8), (2, 4, 6)              # diagonals
        ]
        # Check if any winning combination has all three positions occupied by the same player
        return any(board[a] == board[b] == board[c] == player for a, b, c in wins)

    def check_draw(self, board):
        """Checks if the board is full without a winner."""
        # Return True if all spaces are filled (no empty spaces remain)
        return all(space != ' ' for space in board)

    def disable_all_buttons(self):
        """Disable all game board buttons after game ends."""
        for button in self.buttons:
            button.config(state="disabled")

    def new_game(self):
        """Reset the game to initial state."""
        # Reset game state
        self.board = [' '] * 9
        self.current_player = 'X'
        self.update_player_display()
        
        # Reset all buttons
        for button in self.buttons:
            button.config(text=" ", bg="lightgray", state="normal")

    def quit_game(self):
        """Close the application."""
        self.root.quit()
        self.root.destroy()

    def run(self):
        """Start the GUI application."""
        # Handle window close event
        self.root.protocol("WM_DELETE_WINDOW", self.quit_game)
        # Start the main event loop
        self.root.mainloop()


def main():
    """Create and run the Tic-Tac-Toe GUI application."""
    game = TicTacToeGUI()
    game.run()


# Entry point of the program
if __name__ == '__main__':
    try:
        # Start the GUI game
        main()
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        print("\nGame interrupted. Goodbye!")
        sys.exit()