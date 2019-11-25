from parents.Animal import Animal
from enums.enums import Breeding, Strength, Density, ID, Initiative, Spread, Symbol, Background, Foreground


class Sheep(Animal):

    density = Density.sheep.value
    id = ID.sheep.value
    initiative = Initiative.sheep.value
    symbol = Symbol.sheep.value
    breeding = Breeding.sheep.value
    background = Background.sheep.value
    foreground = Foreground.sheep.value

    def __init__(self, world, x, y, cd, strength):
        super().__init__(world, x, y, cd, strength)

    def breed(self, x1, y1, x2, y2, other):
        f = self.breed_field(x1, y1, x2, y2, other)
        if f != -1:
            Sheep(self.world, f.x, f.y, Breeding.sheep, Strength.sheep)

