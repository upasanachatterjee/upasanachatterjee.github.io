import tkinter as tk
from tkinter import font
from typing import List

class Board(tk.Tk):
    def __init__(self, board_size=3) -> None:
        super().__init__()
        self.title("Tic-Tac-Toe Board")
        self.size = board_size
        self.board = [0] * (self.size * self.size)
        self._create_board_display()
        self._create_board_grid(board_size)
        
        self.empty_spots = self.size * self.size

    """
    0 0 0
    0 0 0
    0 0 0
    """

    def get_value(self, x, y):
        return self.board[(self.size * y) + x]

    def set_value(self, x, y, value):
        self.board[(self.size * y) + x] = value

    def _create_board_display(self):
        display_frame = tk.Frame(master=self)
        display_frame.pack(fill=tk.X)
        self.display = tk.Label(
            master=display_frame,
            text="Ready?",
            font=font.Font(size=28, weight="bold"),
        )
        self.display.pack()

    def _create_board_grid(self, board_size):
        grid_frame = tk.Frame(master=self)
        grid_frame.pack()
        for row in range(board_size):
            self.rowconfigure(row, weight=1, minsize=50)
            self.columnconfigure(row, weight=1, minsize=75)
            for col in range(board_size):
                button = tk.Button(
                    master=grid_frame,
                    text="",
                    font=font.Font(size=36, weight="bold"),
                    fg="black",
                    width=3,
                    height=2,
                    highlightbackground="lightblue",
                )
                self.set_value(row, col, button)
                button.grid(
                    row=row,
                    column=col,
                    padx=5,
                    pady=5,
                    sticky="nsew"
                )

class Game:
    def __init__(self, board_size=3) -> None:
        self.game_over = False
        self.board = Board(board_size)
        self.player = None

    def _horizontal_win(self):
        for y in range(self.size):
            row = set([self.board.get_value(x, y) for x in range(self.board.size)])

            if len(row) == 1 and row.pop() == self.player:
                return True

    def _vertical_win(self):
        for x in range(self.size):
            column = set([self.board.get_value(x, y) for y in range(self.board.size)])

            if len(column) == 1 and column.pop() == self.player:
                return True

    def _diagonal_win(self, left_to_right=True):
        diagonal = set()
        for i in range(self.board.size):
            val = i if left_to_right else self.board.size - i - 1
            diagonal.add(self.board.get_value(val, val))

        if len(diagonal) == 1 and diagonal.pop() == self.player:
                return True

    def _end_game(self, winner=None):
        if winner:
            print(f"Game ended. Player {winner} won!")
        else:
            print("No winner. Game ended in a tie.")

    def _check_game_over(self):
        if (
            self._diagonal_win(True) or self._diagonal_win(False) or 
            self._vertical_win() or self._horizontal_win()
        ):
            self.game_over = True
            self._end_game(self.player)
        elif not self.board.empty_spots:
            self.game_over = True
            self._end_game()


    def make_move(self, player, x, y):
        if not self.board.get_value(x, y):
            self.player = player
            self.board.set_value(x, y, player)
            self._check_game_over()


'''
https://realpython.com/tic-tac-toe-python/
https://github.com/leonardyeoxl/pymongo-flask-web-app
'''