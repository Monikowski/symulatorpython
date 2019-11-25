from parents.Animal import Animal, Field
from enums.enums import Breeding, Strength, Density, ID, Initiative, Spread, Symbol, Background, Foreground
import random


class Fox(Animal):

    density = Density.fox.value
    id = ID.fox.value
    initiative = Initiative.fox.value
    symbol = Symbol.fox.value
    breeding = Breeding.fox.value
    background = Background.fox.value
    foreground = Foreground.fox.value

    def __init__(self, world, x, y, cd, strength):
        super().__init__(world, x, y, cd, strength)

    def random_field(self, move_range):
        new_x = self.x
        new_y = self.y
        tries_all = 0
        while self.world.organisms_board[new_x][new_y].occupied\
                and (((new_x == self.x) and (new_y == self.y))
                     or (self.world.organisms_board[new_x][new_y].organism.strength > self.strength and
                     self.world.organisms_board[new_x][new_y].organism.id != self.id)) and tries_all < 25:
            while True:
                new_x = self.x + random.randint(-move_range, move_range)
                if (new_x >= 0) and (new_x < self.world.width):
                    break
            while True:
                new_y = self.y + random.randint(-move_range, move_range)
                if (new_y >= 0) and (new_y < self.world.height):
                    break
            tries_all += 1
        return Field(new_x, new_y)

    def breed(self, x1, y1, x2, y2, other):
        f = self.breed_field(x1, y1, x2, y2, other)
        if f != -1:
            Fox(self.world, f.x, f.y, Breeding.fox, Strength.fox)
