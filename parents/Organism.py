from abc import ABC, abstractmethod


class Field:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Organism(ABC):

    def __init__(self, world, x, y, cd, strength):
        self.world = world
        self.x = x
        self.y = y
        self.cd = cd.value
        self.strength = strength.value
        self.dead = False
        self.__killer = None
        self.__age = 0
        self.world.add_list(self)

    @property
    def world(self):
        return self.__world

    @world.setter
    def world(self, value):
        self.__world = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def cd(self):
        return self.__cd

    @cd.setter
    def cd(self, value):
        self.__cd = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    @property
    def age(self):
        return self.__age

    def add_age(self):
        self.__age += 1
        if self.cd > 0:
            self.cd += -1

    @property
    def dead(self):
        return self.__dead

    @dead.setter
    def dead(self, value):
        self.__dead = value

    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, value):
        self.__strength = value

    def set_killer(self, killer):
        self.__killer = killer

    def collision(self, attacker):
        return True

    def death(self, killer):
        self.world.organisms_board[self.x][self.y].occupied = False
        self.dead = True
        text = type(self).__name__ + " x: " + str(self.x) + " y: " + str(self.y) + " killed by "\
            + type(killer).__name__ + "\n"
        self.world.txt += text

    @abstractmethod
    def action(self):
        pass
