from meme.Organisms import Organisms
from animals import Antelope, Cyber_sheep, Fox, Human, Sheep, Turtle, Wolf
from plants import Belladonna, Dandelion, Grass, Guarana, Hogweed
from parents.Organism import Field
import random
from enums.enums import Breeding, Strength
import pickle


class World:

    def __init__(self, width, height, org_board=None, org_list=None):
        if org_board is not None and org_list is not None:
            self.human_alive = False
            self.human_cd = 0
            self.__width = width
            self.__height = height
            self.organisms_board = [[Organisms() for _ in range(width)] for _ in range(height)]
            self.organisms_list = []
            for x in org_list:
                self.add_list(x)
                if x.id == 0:
                    self.human_alive = True
                    self.human_cd = x.cd
                    self.human_x = x.x
                    self.human_y = x.y
            self.txt = ""
            self.human_move = 0

        else:
            self.__width = width
            self.__height = height
            self.organisms_board = [[Organisms() for _ in range(width)] for _ in range(height)]
            self.organisms_list = []
            self.human_x = 0
            self.human_y = 0
            self.__spawn()
            self.txt = ""
            self.human_alive = True
            self.human_cd = 0
            self.human_move = 0


    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    def add_list(self, organism):
        place = 0
        if len(self.organisms_list) > 0:
            for x in self.organisms_list:
                if x.initiative < organism.initiative:
                    self.organisms_list.insert(place, organism)
                    break
                place += 1
            else:
                self.organisms_list.append(organism)
        else:
            self.organisms_list.append(organism)
        self.organisms_board[organism.x][organism.y].occupied = True
        self.organisms_board[organism.x][organism.y].organism = organism
        organism.world = self

    def next_turn(self):
        self.txt = ""
        for x in self.organisms_list:
            x.add_age()
        for x in self.organisms_list:
            if x.age > 0 and not x.dead:
                x.action()
        i = len(self.organisms_list) - 1
        while i >= 0:
            if self.organisms_list[i].dead:
                self.organisms_list.pop(i)
            i += -1

    def __spawn(self):
        tiles = self.width*self.height
        x = 0
        while x < tiles*Antelope.Antelope.density:
            f = self.empty_field()
            Antelope.Antelope(self, f.x, f.y, Breeding.antelope, Strength.antelope)
            x += 1
        x = 0
        while x < tiles * Cyber_sheep.Cyber_sheep.density:
            f = self.empty_field()
            Cyber_sheep.Cyber_sheep(self, f.x, f.y, Breeding.cyber_sheep, Strength.cyber_sheep)
            x += 1
        x = 0
        while x < tiles * Fox.Fox.density:
            f = self.empty_field()
            Fox.Fox(self, f.x, f.y, Breeding.fox, Strength.fox)
            x += 1
        x = 0
        while x < tiles * Sheep.Sheep.density:
            f = self.empty_field()
            Sheep.Sheep(self, f.x, f.y, Breeding.sheep, Strength.sheep)
            x += 1
        x = 0
        while x < tiles * Turtle.Turtle.density:
            f = self.empty_field()
            Turtle.Turtle(self, f.x, f.y, Breeding.turtle, Strength.turtle)
            x += 1
        x = 0
        while x < tiles * Wolf.Wolf.density:
            f = self.empty_field()
            Wolf.Wolf(self, f.x, f.y, Breeding.wolf, Strength.wolf)
            x += 1
        x = 0
        while x < tiles * Belladonna.Belladonna.density:
            f = self.empty_field()
            Belladonna.Belladonna(self, f.x, f.y, Breeding.belladonna, Strength.belladonna)
            x += 1
        x = 0
        while x < tiles * Grass.Grass.density:
            f = self.empty_field()
            Grass.Grass(self, f.x, f.y, Breeding.grass, Strength.grass)
            x += 1
        x = 0
        while x < tiles * Dandelion.Dandelion.density:
            f = self.empty_field()
            Dandelion.Dandelion(self, f.x, f.y, Breeding.dandelion, Strength.dandelion)
            x += 1
        x = 0
        while x < tiles * Guarana.Guarana.density:
            f = self.empty_field()
            Guarana.Guarana(self, f.x, f.y, Breeding.guarana, Strength.guarana)
            x += 1
        x = 0
        while x < tiles * Hogweed.Hogweed.density:
            f = self.empty_field()
            Hogweed.Hogweed(self, f.x, f.y, Breeding.hogweed, Strength.hogweed)
            x += 1
        f = self.empty_field()
        Human.Human(self, f.x, f.y, Breeding.human, Strength.human)

    def empty_field(self):
        while True:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if not self.organisms_board[x][y].occupied:
                return Field(x, y)

