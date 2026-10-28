import tkinter as tk

current_player = "X"
board = [""] * 9
scores = {"X": 0, "O": 0, "Ties": 0}
game_active = True

# All 8 winning combinations (3 rows, 3 columns, 2 diagonals)
WINNING_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
    (0, 4, 8), (2, 4, 6)             # Diagonals
]

def handle_click(index):
    global current_player, game_active

    # Ignore clicks on taken tiles or if game has ended
    if board[index] != "" or not game_active:
        return

    # Mark the tile
    board[index] = current_player
    buttons[index].config(
        text=current_player,
        fg="#00d2d3" if current_player == "X" else "#ff6b6b"
    )

    # 1. Check for a winner
    winner, winning_combo = check_winner()
    if winner:
        game_active = False
        scores[winner] += 1
        update_scoreboard()
        for idx in winning_combo:
            buttons[idx].config(bg="#1dd1a1", fg="#ffffff")  # Highlight winning line
        status_label.config(text=f"🎉 Player {winner} Wins!", fg="#1dd1a1")
        return

    # 2. Check for a tie
    if "" not in board:
        game_active = False
        scores["Ties"] += 1
        update_scoreboard()
        status_label.config(text="🤝 It's a Tie!", fg="#feca57")
        return

    # 3. Switch turn
    current_player = "O" if current_player == "X" else "X"
    status_label.config(
        text=f"Turn: Player {current_player}",
        fg="#00d2d3" if current_player == "X" else "#ff6b6b"
    )

def check_winner():
    """Checks the 8 possible winning lines."""
    for a, b, c in WINNING_LINES:
        if board[a] == board[b] == board[c] != "":
            return board[a], (a, b, c)
    return None, None

def reset_round():
    """Clears the board for a new round while keeping scores."""
    global current_player, board, game_active
    board = [""] * 9
    game_active = True
    current_player = "X"
    status_label.config(text="Turn: Player X", fg="#00d2d3")
    for btn in buttons:
        btn.config(text="", bg="#2f3542", fg="#ffffff")

def reset_all():
    """Resets scores and starts fresh."""
    global scores
    scores = {"X": 0, "O": 0, "Ties": 0}
    update_scoreboard()
    reset_round()

def update_scoreboard():
    score_label.config(
        text=f"X: {scores['X']}   |   O: {scores['O']}   |   Ties: {scores['Ties']}"
    )

root = tk.Tk()
root.title("Tic-Tac-Toe")
root.configure(bg="#1e1e2e")
root.resizable(False, False)

# 1. Live Scoreboard
score_label = tk.Label(
    root,
    text=f"X: 0   |   O: 0   |   Ties: 0",
    font=("Segoe UI", 12, "bold"),
    bg="#1e1e2e",
    fg="#a4b0be",
    pady=8
)
score_label.pack()

# 2. Turn / Result Status
status_label = tk.Label(
    root,
    text="Turn: Player X",
    font=("Segoe UI", 16, "bold"),
    bg="#1e1e2e",
    fg="#00d2d3"
)
status_label.pack(pady=4)

# 3. 3x3 Button Grid
grid_frame = tk.Frame(root, bg="#1e1e2e")
grid_frame.pack(padx=16, pady=10)

buttons = []
for i in range(9):
    btn = tk.Button(
        grid_frame,
        text="",
        font=("Segoe UI", 24, "bold"),
        width=4,
        height=2,
        bg="#2f3542",
        fg="#ffffff",
        activebackground="#57606f",
        relief="flat",
        cursor="hand2",
        command=lambda idx=i: handle_click(idx)
    )
    # i // 3 calculates row (0, 1, 2), i % 3 calculates column (0, 1, 2)
    btn.grid(row=i // 3, column=i % 3, padx=4, pady=4)
    buttons.append(btn)

# 4. Action Buttons (New Round & Reset All)
btn_frame = tk.Frame(root, bg="#1e1e2e")
btn_frame.pack(pady=14)

new_round_btn = tk.Button(
    btn_frame,
    text="New Round",
    font=("Segoe UI", 10, "bold"),
    bg="#575fcf",
    fg="white",
    relief="flat",
    padx=12,
    pady=4,
    cursor="hand2",
    command=reset_round
)
new_round_btn.grid(row=0, column=0, padx=6)

reset_all_btn = tk.Button(
    btn_frame,
    text="Reset All",
    font=("Segoe UI", 10, "bold"),
    bg="#ff4757",
    fg="white",
    relief="flat",
    padx=12,
    pady=4,
    cursor="hand2",
    command=reset_all
)
reset_all_btn.grid(row=0, column=1, padx=6)

if __name__ == "__main__":
    root.mainloop()
