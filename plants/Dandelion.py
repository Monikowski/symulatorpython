from parents.Plant import Plant
from enums.enums import Breeding, Strength, Density, ID, Initiative, Spread, Symbol, Foreground
import random


class Dandelion(Plant):

    density = Density.dandelion.value
    id = ID.dandelion.value
    initiative = Initiative.plant.value
    symbol = Symbol.dandelion.value
    breeding = Breeding.dandelion.value
    foreground = Foreground.dandelion.value

    def __init__(self, world, x, y, cd, strength):
        super().__init__(world, x, y, cd, strength)

    def action(self):
        tries = 0
        while tries < 3:
            x = random.randint(0, 100)
            if x <= self.breeding:
                self.spread()
            tries += 1

    def spread(self):
        f = self.random_field()
        if not self.world.organisms_board[f.x][f.y].occupied:
            Dandelion(self.world, f.x, f.y, Breeding.plant_cd, Strength.dandelion)
