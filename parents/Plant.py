from parents.Organism import Organism, Field
from enums.enums import Background
import random


class Plant(Organism):
    background = Background.plant.value

    def __init__(self, world, x, y, cd, strength):
        super().__init__(world, x, y, cd, strength)

    def action(self):
        x = random.randint(0, 101)
        if x <= self.breeding:
            self.spread()

    def random_field(self):
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
