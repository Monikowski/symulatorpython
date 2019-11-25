import tkinter as tk
from animals import Antelope, Cyber_sheep, Fox, Sheep, Turtle, Wolf
from plants import Belladonna, Dandelion, Grass, Guarana, Hogweed
from enums.enums import Breeding, Strength


class New_organism:

    def __init__(self, x, y, caller):
        self.caller = caller
        self.root = tk.Tk()
        self.root.geometry("600x600")
        self.x = x
        self.y = y

        self.add_antelope = tk.Button(self.root, command=lambda: self.new_antelope(), text="Antelope")
        self.add_cyber_sheep = tk.Button(self.root, command=lambda: self.new_cyber_sheep(), text="Cyber sheep")
        self.add_fox = tk.Button(self.root, command=lambda: self.new_fox(), text="Fox")
        self.add_sheep = tk.Button(self.root, command=lambda: self.new_sheep(), text="Sheep")
        self.add_turtle = tk.Button(self.root, command=lambda: self.new_turtle(), text="Turtle")
        self.add_wolf = tk.Button(self.root, command=lambda: self.new_wolf(), text="Wolf")
        self.add_belladonna = tk.Button(self.root, command=lambda: self.new_belladonna(), text="Belladonna")
        self.add_grass = tk.Button(self.root, command=lambda: self.new_grass(), text="Grass")
        self.add_guarana = tk.Button(self.root, command=lambda: self.new_guarana(), text="Guarana")
        self.add_dandelion = tk.Button(self.root, command=lambda: self.new_dandelion(), text="Dandelion")
        self.add_hogweed = tk.Button(self.root, command=lambda: self.new_hogweed() , text="Hogweed")

        self.add_antelope.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.add_cyber_sheep.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.add_fox.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.add_sheep.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.add_turtle.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.add_wolf.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.add_belladonna.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.add_dandelion.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.add_grass.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.add_guarana.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.add_hogweed.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        self.root.mainloop()

    def new_antelope(self):
        Antelope.Antelope(self.caller.win.world, self.x, self.y, Breeding.antelope, Strength.antelope)
        self.draw_self()
        self.root.destroy()

    def new_cyber_sheep(self):
        Cyber_sheep.Cyber_sheep(self.caller.win.world, self.x, self.y, Breeding.cyber_sheep, Strength.cyber_sheep)
        self.draw_self()
        self.root.destroy()

    def new_fox(self):
        Fox.Fox(self.caller.win.world, self.x, self.y, Breeding.fox, Strength.fox)
        self.draw_self()
        self.root.destroy()

    def new_sheep(self):
        Sheep.Sheep(self.caller.win.world, self.x, self.y, Breeding.sheep, Strength.sheep)
        self.draw_self()
        self.root.destroy()

    def new_turtle(self):
        Turtle.Turtle(self.caller.win.world, self.x, self.y, Breeding.turtle, Strength.turtle)
        self.draw_self()
        self.root.destroy()

    def new_wolf(self):
        Wolf.Wolf(self.caller.win.world, self.x, self.y, Breeding.wolf, Strength.wolf)
        self.draw_self()
        self.root.destroy()

    def new_belladonna(self):
        Belladonna.Belladonna(self.caller.win.world, self.x, self.y, Breeding.belladonna, Strength.belladonna)
        self.draw_self()
        self.root.destroy()

    def new_dandelion(self):
        Dandelion.Dandelion(self.caller.win.world, self.x, self.y, Breeding.dandelion, Strength.dandelion)
        self.draw_self()
        self.root.destroy()

    def new_grass(self):
        Grass.Grass(self.caller.win.world, self.x, self.y, Breeding.grass, Strength.grass)
        self.draw_self()
        self.root.destroy()

    def new_guarana(self):
        Guarana.Guarana(self.caller.win.world, self.x, self.y, Breeding.guarana, Strength.guarana)
        self.draw_self()
        self.root.destroy()

    def new_hogweed(self):
        Hogweed.Hogweed(self.caller.win.world, self.x, self.y, Breeding.hogweed, Strength.hogweed)
        self.draw_self()
        self.root.destroy()

    def draw_self(self):
        self.caller.win.middle.button_board[self.x][self.y].config(text
                                                                   =str(self.caller.win.world.organisms_board
                                                                        [self.x][self.y].organism.symbol)
                                                                   , fg=self.caller.win.world.organisms_board[self.x][
                                                                        self.y].organism.foreground,
                                                                   bg=self.caller.win.world.organisms_board[self.x][
                                                                       self.y].organism.background)