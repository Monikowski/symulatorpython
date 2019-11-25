from parents.Animal import Animal, Field
from enums.enums import Breeding, Strength, Density, ID, Initiative, Spread, Symbol, Background, Foreground
import random


class Antelope(Animal):

    density = Density.antelope.value
    id = ID.antelope.value
    initiative = Initiative.antelope.value
    symbol = Symbol.antelope.value
    breeding = Breeding.antelope.value
    background = Background.antelope.value
    foreground = Foreground.antelope.value

    def __init__(self, world, x, y, cd, strength):
        super().__init__(world, x, y, cd, strength)

    def action(self):
        self.move(2)

    def collision(self, attacker):
        old_x = self.x
        old_y = self.y
        f = self.random_field_escape()
        self.world.organisms_board[self.x][self.y].occupied = False
        self.world.organisms_board[f.x][f.y].occupied = True
        self.world.organisms_board[f.x][f.y].organism = self
        self.x += (f.x - self.x)
        self.y += (f.y - self.y)
        if old_x == f.x and old_y == f.y:
            return True
        else:
            return False

    def random_field_escape(self):
        new_x = self.x
        new_y = self.y
        tries_all = 0
        while self.world.organisms_board[new_x][new_y].occupied and tries_all < 25:
            while True:
                new_x = self.x + random.randint(-1, 1)
                if (new_x >= 0) and (new_x < self.world.width):
                    break
            while True:
                new_y = self.y + random.randint(-1, 1)
                if (new_y >= 0) and (new_y < self.world.height):
                    break
            tries_all += 1
        return Field(new_x, new_y)

    def breed(self, x1, y1, x2, y2, other):
        f = self.breed_field(x1, y1, x2, y2, other)
        if f != -1:
            Antelope(self.world, f.x, f.y, Breeding.antelope, Strength.antelope)
