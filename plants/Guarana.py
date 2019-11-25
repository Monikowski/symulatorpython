from parents.Plant import Plant
from enums.enums import Breeding, Strength, Density, ID, Initiative, Spread, Symbol, Foreground


class Guarana(Plant):
    density = Density.guarana.value
    id = ID.guarana.value
    initiative = Initiative.plant.value
    symbol = Symbol.guarana.value
    breeding = Breeding.guarana.value
    foreground = Foreground.guarana.value

    def __init__(self, world, x, y, cd, strength):
        super().__init__(world, x, y, cd, strength)

    def collision(self, attacker):
        attacker.strength += 3
        return True

    def spread(self):
        f = self.random_field()
        if not self.world.organisms_board[f.x][f.y].occupied:
            Guarana(self.world, f.x, f.y, Breeding.plant_cd, Strength.guarana)