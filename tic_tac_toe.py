import tkinter as tk
import tkinter.messagebox

class TicTacToe:
    def __init__(self, window):
        self.window = window
        self.window.title('Tic Tac Toe')
        self.create_widgets()
        self.player_turn = 1
        self.moves = 0

    def create_widgets(self):
        self.frame = tk.Frame(master=self.window)
        self.frame.pack(pady=10)
        
        self.label = tk.Label(master=self.frame, text="Tic Tac Toe", font=("Arial", 15))
        self.label.pack()

        self.frame1 = tk.Frame(master=self.window, borderwidth=2, relief=tk.RAISED, bg='#dadec3')
        self.frame1.pack(padx=10, pady=10)

        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = tk.Button(master=self.frame1, text='', width=10, height=5, bg='white', command=lambda row=i, col=j: self.button_click(row, col))
                button.grid(row=i, column=j, padx=5, pady=5)
                self.buttons.append(button)

        self.frame2 = tk.Frame(master=self.window, border=2, relief=tk.SUNKEN, bg='#dadec3')
        self.frame2.pack()

        self.label1 = tk.Label(master=self.frame2, text="Player 1 --> X\nPlayer 2 --> O", width=10)
        self.label1.grid(row=0, column=0, padx=5)
        
        self.button_restart = tk.Button(master=self.frame2, text="Restart", width=10, height=3, relief=tk.GROOVE, command=self.restart_game)
        self.button_restart.grid(row=0, column=1, padx=10, pady=10)
        
        self.label2 = tk.Label(master=self.frame2, text='Player-1 Turn', bg="skyblue", width=10, height=3, relief=tk.SUNKEN)
        self.label2.grid(row=0, column=2, padx=5)

    def button_click(self, row, col):
        button_index = row * 3 + col
        button = self.buttons[button_index]

        if button['text'] == '':
            if self.player_turn == 1:
                symbol = 'X'
                self.label2.config(text='Player-2 Turn', bg="#e8956f")
            else:
                symbol = 'O'
                self.label2.config(text='Player-1 Turn', bg="skyblue")

            button.config(text=symbol, bg='skyblue' if symbol == 'X' else '#e8956f')
            self.player_turn = 3 - self.player_turn  # Alternating between player 1 (1) and player 2 (2)
            self.moves += 1

            if self.check_winner(symbol):
                self.disable_buttons()
                winner = "Player 1" if symbol == 'X' else "Player 2"
                tkinter.messagebox.showinfo("Tic Tac Toe", f"Winner is {winner}")
            elif self.moves == 9:
                self.disable_buttons()
                tkinter.messagebox.showinfo("Tic Tac Toe", "Match is Draw.")

    def check_winner(self, symbol):
        winning_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
            [0, 4, 8], [2, 4, 6]              # Diagonal
        ]

        for condition in winning_conditions:
            if all(self.buttons[i]['text'] == symbol for i in condition):
                return True
        return False

    def restart_game(self):
        self.player_turn = 1
        self.moves = 0
        self.label2.config(text='Player-1 Turn', bg="skyblue")
        for button in self.buttons:
            button.config(text='', bg='white', state=tk.NORMAL)

    def disable_buttons(self):
        for button in self.buttons:
            button.config(state=tk.DISABLED)
window = tk.Tk()
game = TicTacToe(window)
window.mainloop()