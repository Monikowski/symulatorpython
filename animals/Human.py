from parents.Animal import Animal, Field
from enums.enums import Breeding, Strength, Density, ID, Initiative, Spread, Symbol, Background, Foreground


class Human(Animal):

    id = ID.human.value
    initiative = Initiative.human.value
    symbol = Symbol.human.value
    breeding = Breeding.human.value
    background = Background.human.value
    foreground = Foreground.human.value

    def __init__(self, world, x, y, cd, strength):
        super().__init__(world, x, y, cd, strength)
        self.world.human_x = x
        self.world.human_y = y
        self.__age = 0

    @property
    def age(self):
        return self.__age

    def action(self):
        self.move(self.world.human_move)

    def move(self, f):
        if f == 99:
            self.cd += 15
            self.strength += 10
            self.world.human_cd = 15

        else:
            new_x = f.x
            new_y = f.y

            if new_x != self.x or new_y != self.y:
                if self.world.organisms_board[new_x][new_y].occupied:
                    self.fight(self.world.organisms_board[new_x][new_y].organism, new_x, new_y)

                if (not self.dead) and (not self.world.organisms_board[new_x][new_y].occupied):
                    self.world.organisms_board[self.x][self.y].occupied = False
                    self.world.organisms_board[new_x][new_y].organism = self
                    self.world.organisms_board[new_x][new_y].occupied = True
                    self.x += (new_x - self.x)
                    self.y += (new_y - self.y)
        self.world.human_x = self.x
        self.world.human_y = self.y

    def add_age(self):
        self.__age += 1
        if self.cd > 5:
            self.strength += -1
        if self.cd > 0:
            self.cd += -1
            self.world.human_cd += -1

    def death(self, killer):
        self.world.organisms_board[self.x][self.y].occupied = False
        self.dead = True
        text = type(self).__name__ + " x: " + str(self.x) + " y: " + str(self.y) + " killed by "\
            + type(killer).__name__ + "\n"
        self.world.txt += text
        self.world.human_alive = False
