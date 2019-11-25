import tkinter as tk
from Tkinter.New_organism import New_organism

class Middle:

    def __init__(self, master, win):
        self.win = win
        self.frame = tk.Frame(master=master)
        self.frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.frame_board = [tk.Frame(master=self.frame) for _ in range(win.world.width)]
        self.button_board = [[tk.Button(master=self.frame_board[y], command=lambda x1=x, y1=y: self.open_win(x1, y1))
                              for x in range(win.world.width)] for y in range(win.world.height)]
        for x in range(win.world.width):
            for y in range(win.world.height):
                self.button_board[x][y].pack(side=tk.TOP, expand=True, fill=tk.BOTH)
            self.frame_board[x].pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

    def open_win(self, y, x):
        if self.win.world.organisms_board[x][y].occupied:
            print("x: ", x, " y: ", y, ", ", type(self.win.world.organisms_board[x][y].organism).__name__, ", str: ",
                  self.win.world.organisms_board[x][y].organism.strength, ", cd: ",
                  self.win.world.organisms_board[x][y].organism.cd)
        else:
            New_organism(x, y, self)
