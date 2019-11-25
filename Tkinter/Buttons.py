import tkinter as tk


class Buttons:

    def __init__(self, master, win):
        self.frame = tk.Frame(master=master)
        self.frame.pack(side=tk.LEFT)
        self.next_turn = tk.Button(master=self.frame, text="Next turn", command=lambda: win.next_turn(),
                                   state=tk.DISABLED)
        self.next_turn.pack(side=tk.TOP)
        self.save_game = tk.Button(master=self.frame, text="Save game", command=lambda: win.save())
        self.save_game.pack(side=tk.TOP)
        self.load_game = tk.Button(master=self.frame, text="Load game", command=lambda: win.load())
        self.load_game.pack(side=tk.TOP)
