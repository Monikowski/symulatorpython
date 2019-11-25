import tkinter as tk
import tkinter.scrolledtext as tkst


class ScrTxt:

    def __init__(self, master):
        self.frame = tk.Frame(master=master)
        self.frame.pack(side=tk.LEFT)
        self.editArea = tkst.ScrolledText(master=self.frame, wrap=tk.WORD, width=25, height=40)
        self.editArea.pack(padx=3, pady=3, fill='both', expand=True)

    def update_text(self, txt):
        self.editArea.insert(tk.INSERT, txt)