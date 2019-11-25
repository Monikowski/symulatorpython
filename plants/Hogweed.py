from parents.Plant import Plant
from enums.enums import Breeding, Strength, Density, ID, Initiative, Spread, Symbol, Foreground
import random


class Hogweed(Plant):
    density = Density.hogweed.value
    id = ID.hogweed.value
    initiative = Initiative.plant.value
    symbol = Symbol.hogweed.value
    breeding = Breeding.hogweed.value
    foreground = Foreground.hogweed.value

    def __init__(self, world, x, y, cd, strength):
        super().__init__(world, x, y, cd, strength)

    def collision(self, attacker):
        if attacker.id < 6:
            self.death(attacker)
            attacker.death(self)
            return False
        else:
            self.death(attacker)
            return False

    def action(self):
        con_x = -1
        while con_x < 2:
            con_y = -1
            while con_y < 2:
                if (((self.x + con_x) > -1) and ((self.x + con_x) < self.world.width)
                        and ((self.y + con_y) > -1) and ((self.y + con_y) < self.world.height)):
                    if self.world.organisms_board[self.x + con_x][self.y + con_y].occupied\
                            and self.world.organisms_board[self.x + con_x][self.y + con_y].organism.id < 6:
                        self.world.organisms_board[self.x + con_x][self.y + con_y].organism.death(self)
                con_y += 1
            con_x += 1
        x = random.randint(0, 100)
        if x <= self.breeding:
            self.spread()

    def spread(self):
        f = self.random_field()
        if not self.world.organisms_board[f.x][f.y].occupied:
            Hogweed(self.world, f.x, f.y, Breeding.plant_cd, Strength.hogweed)
