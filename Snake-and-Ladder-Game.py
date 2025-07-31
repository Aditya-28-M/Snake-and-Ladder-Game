import tkinter as tk
from tkinter import messagebox
import random

# Define snakes and ladders
snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60,
          87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84,
           36: 44, 51: 67, 71: 91, 80: 100}

# Initialize player positions
player_positions = {"Player 1": 1, "Player 2": 1}
current_player = "Player 1"

# Roll the dice
def roll_dice():
    return random.randint(1, 6)

# Handle turn
def play_turn():
    global current_player

    dice = roll_dice()
    result_label.config(text=f"{current_player} rolled a {dice}")

    pos = player_positions[current_player] + dice

    if pos > 100:
        result_label.config(text=f"{current_player} rolled {dice} but needs exact roll to win.")
    else:
        if pos in snakes:
            messagebox.showinfo("Snake!", f"{current_player} hit a snake! Down to {snakes[pos]}")
            pos = snakes[pos]
        elif pos in ladders:
            messagebox.showinfo("Ladder!", f"{current_player} climbed a ladder! Up to {ladders[pos]}")
            pos = ladders[pos]

        player_positions[current_player] = pos
        update_positions()

        if pos == 100:
            messagebox.showinfo("Game Over", f"{current_player} wins!")
            root.destroy()
            return

    # Switch player
    current_player = "Player 2" if current_player == "Player 1" else "Player 1"
    turn_label.config(text=f"{current_player}'s Turn")

# Update position display
def update_positions():
    p1_pos.config(text=f"Player 1: {player_positions['Player 1']}")
    p2_pos.config(text=f"Player 2: {player_positions['Player 2']}")

# Create GUI window
root = tk.Tk()
root.title("Snake and Ladder Game")
root.geometry("400x300")

title = tk.Label(root, text="Snake and Ladder", font=("Arial", 18, "bold"))
title.pack(pady=10)

turn_label = tk.Label(root, text="Player 1's Turn", font=("Arial", 14))
turn_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

roll_button = tk.Button(root, text="Roll Dice", font=("Arial", 14), command=play_turn)
roll_button.pack(pady=20)

# Display positions
p1_pos = tk.Label(root, text="Player 1: 1", font=("Arial", 12))
p1_pos.pack()

p2_pos = tk.Label(root, text="Player 2: 1", font=("Arial", 12))
p2_pos.pack()

# Start GUI loop
root.mainloop()