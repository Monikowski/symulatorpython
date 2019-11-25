from parents.Plant import Plant
from enums.enums import Breeding, Strength, Density, ID, Initiative, Spread, Symbol, Foreground


class Belladonna(Plant):
    density = Density.belladonna.value
    id = ID.belladonna.value
    initiative = Initiative.plant.value
    symbol = Symbol.belladonna.value
    breeding = Breeding.belladonna.value
    foreground = Foreground.belladonna.value

    def __init__(self, world, x, y, cd, strength):
        super().__init__(world, x, y, cd, strength)

    def collision(self, attacker):
        self.death(attacker)
        attacker.death(self)
        return False

    def spread(self):
        f = self.random_field()
        if not self.world.organisms_board[f.x][f.y].occupied:
            Belladonna(self.world, f.x, f.y, Breeding.plant_cd, Strength.belladonna)
