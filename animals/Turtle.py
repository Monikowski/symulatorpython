from parents.Animal import Animal
from enums.enums import Breeding, Strength, Density, ID, Initiative, Spread, Symbol, Background, Foreground
import random


class Turtle(Animal):

    density = Density.turtle.value
    id = ID.turtle.value
    initiative = Initiative.turtle.value
    symbol = Symbol.turtle.value
    breeding = Breeding.turtle.value
    background = Background.turtle.value
    foreground = Foreground.turtle.value

    def __init__(self, world, x, y, cd, strength):
        super().__init__(world, x, y, cd, strength)

    def collision(self, attacker):
        if attacker.strength < 5:
            return False
        else:
            return True

    def action(self):
        x = random.randint(0, 3)
        if x == 0:
            self.move(1)

    def breed(self, x1, y1, x2, y2, other):
        f = self.breed_field(x1, y1, x2, y2, other)
        if f != -1:
            Turtle(self.world, f.x, f.y, Breeding.turtle, Strength.turtle)
