import tkinter as tk
import Tkinter.ScrTxt as scrtxt
import Tkinter.Middle as middle
import Tkinter.Buttons as buttons
from meme.World import World
import pickle
from enums.enums import Human_moves
from parents.Organism import Field
from Tkinter.Entry_save import Entry_save
from Tkinter.Entry_load import Entry_load


class Win:

    def __init__(self, x, y, org_board=None, org_list=None):
        self.world = World(x, y, org_board, org_list)
        self.root = tk.Tk()
        self.root.geometry("1000x600")
        self.scrtxt = scrtxt.ScrTxt(self.root)

        self.middle = middle.Middle(self.root, self)

        self.buttons = buttons.Buttons(self.root, self)

        self.draw()
        self.root.bind('<Left>', self.leftKey)
        self.root.bind('<Right>', self.rightKey)
        self.root.bind('<Up>', self.upKey)
        self.root.bind('<Down>', self.downKey)
        self.root.bind('<x>', self.xKey)
        if not self.world.human_alive:
            self.buttons.next_turn.config(status=tk.NORMAL)
        self.root.mainloop()

    def draw(self):
        for x in range(len(self.world.organisms_board)):
            for y in range(len(self.world.organisms_board[0])):
                if self.world.organisms_board[x][y].occupied:
                    self.middle.button_board[x][y].config(text=str(self.world.organisms_board[x][y].organism.symbol)
                                                          , fg=self.world.organisms_board[x][y].organism.foreground,
                                                          bg=self.world.organisms_board[x][y].organism.background)
                else:
                    self.middle.button_board[x][y].config(text="O", fg='#4c723c', bg='#4c723c')

    def next_turn(self):
        self.scrtxt.editArea.delete('1.0', tk.END)
        self.world.next_turn()
        self.draw()
        self.scrtxt.update_text(self.world.txt)
        if not self.world.human_alive:
            self.buttons.next_turn.config(state=tk.NORMAL)

    def load(self):
        Entry_load(self)

    def save(self):
        Entry_save(self)

    def new(self, x, y, board, org_list):
        Win(x, y, board, org_list)

    def leftKey(self, event):
        if self.world.human_alive:
            if self.world.human_x > 0:
                self.world.human_move = Field(self.world.human_x - 1, self.world.human_y)
                self.next_turn()

    def rightKey(self, event):
        if self.world.human_alive:
            if self.world.human_x < self.world.width - 1:
                self.world.human_move = Field(self.world.human_x + 1, self.world.human_y)
                self.next_turn()

    def upKey(self, event):
        if self.world.human_alive:
            if self.world.human_y > 0:
                self.world.human_move = Field(self.world.human_x, self.world.human_y - 1)
                self.next_turn()

    def downKey(self, event):
        if self.world.human_alive:
            if self.world.human_y < self.world.height - 1:
                self.world.human_move = Field(self.world.human_x, self.world.human_y + 1)
                self.next_turn()

    def xKey(self, event):
        if self.world.human_alive:
            if self.world.human_cd == 0:
                self.world.human_move = 99
                self.next_turn()


