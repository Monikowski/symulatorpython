from parents.Animal import Animal
from enums.enums import Breeding, Strength, Density, ID, Initiative, Spread, Symbol, Background, Foreground


class Wolf(Animal):

    density = Density.wolf.value
    id = ID.wolf.value
    initiative = Initiative.wolf.value
    symbol = Symbol.wolf.value
    breeding = Breeding.wolf.value
    background = Background.wolf.value
    foreground = Foreground.wolf.value

    def __init__(self, world, x, y, cd, strength):
        super().__init__(world, x, y, cd, strength)

    def breed(self, x1, y1, x2, y2, other):
        f = self.breed_field(x1, y1, x2, y2, other)
        if f != -1:
            Wolf(self.world, f.x, f.y, Breeding.wolf, Strength.wolf)
