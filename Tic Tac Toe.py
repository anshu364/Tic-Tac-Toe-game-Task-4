import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("300x350")
root.resizable(False, False)

current_player = "X"
buttons = [[None for _ in range(3)] for _ in range(3)]

# Check for win or draw
def check_winner():
    for i in range(3):
        # Check rows
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True
        # Check columns
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return True

    # Check diagonals
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True

    return False

def check_draw():
    for row in buttons:
        for btn in row:
            if btn["text"] == "":
                return False
    return True

# Button click event
def on_click(row, col):
    global current_player
    if buttons[row][col]["text"] == "":
        buttons[row][col]["text"] = current_player
        if check_winner():
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            reset_game()
        elif check_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"
            status_label["text"] = f"Player {current_player}'s Turn"

# Reset the game
def reset_game():
    global current_player
    current_player = "X"
    status_label["text"] = "Player X's Turn"
    for row in buttons:
        for btn in row:
            btn["text"] = ""

# UI Layout
status_label = tk.Label(root, text="Player X's Turn", font=("Arial", 16))
status_label.pack(pady=10)

frame = tk.Frame(root)
frame.pack()

# Create 3x3 grid buttons
for i in range(3):
    for j in range(3):
        button = tk.Button(frame, text="", width=8, height=4,
                           font=("Arial", 18), command=lambda i=i, j=j: on_click(i, j))
        button.grid(row=i, column=j)
        buttons[i][j] = button

# Reset Button
reset_btn = tk.Button(root, text="Reset", font=("Arial", 14), command=reset_game)
reset_btn.pack(pady=10)

root.mainloop()