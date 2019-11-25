from parents.Plant import Plant
from enums.enums import Breeding, Strength, Density, ID, Initiative, Spread, Symbol, Foreground


class Grass(Plant):

    density = Density.grass.value
    id = ID.grass.value
    initiative = Initiative.plant.value
    symbol = Symbol.grass.value
    breeding = Breeding.grass.value
    foreground = Foreground.grass.value

    def __init__(self, world, x, y, cd, strength):
        super().__init__(world, x, y, cd, strength)

    def spread(self):
        f = self.random_field()
        if not self.world.organisms_board[f.x][f.y].occupied:
            Grass(self.world, f.x, f.y, Breeding.plant_cd, Strength.grass)