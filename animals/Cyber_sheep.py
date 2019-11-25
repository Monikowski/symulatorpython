from parents.Animal import Animal
from enums.enums import Breeding, Strength, Density, ID, Initiative, Spread, Symbol, Background, Foreground
from parents.Organism import Field


class Cyber_sheep(Animal):

    density = Density.cyber_sheep.value
    id = ID.cyber_sheep.value
    initiative = Initiative.cyber_sheep.value
    symbol = Symbol.cyber_sheep.value
    breeding = Breeding.cyber_sheep.value
    background = Background.cyber_sheep.value
    foreground = Foreground.cyber_sheep.value

    def __init__(self, world, x, y, cd, strength):
        super().__init__(world, x, y, cd, strength)

    def action(self):
        h = self.find_hogweed()
        if h != -1:
            if h.x != self.x or h.y != self.y:
                if self.world.organisms_board[h.x][h.y].occupied:
                    self.fight(self.world.organisms_board[h.x][h.y].organism, h.x, h.y)
                if (not self.dead) and (not self.world.organisms_board[h.x][h.y].occupied):
                    self.world.organisms_board[self.x][self.y].occupied = False
                    self.world.organisms_board[h.x][h.y].organism = self
                    self.world.organisms_board[h.x][h.y].occupied = True
                    self.x += (h.x - self.x)
                    self.y += (h.y - self.y)
        else:
            self.move(1)

    def find_hogweed(self):
        closest_hogweed = None
        for x in self.world.organisms_list:
            if x.id == ID.hogweed.value:
                if closest_hogweed is not None:
                    if (max(abs(self.x - x.x), abs(self.y - x.y))) < max((abs(self.x - closest_hogweed.x)
                                                                          , abs(self.y - closest_hogweed.y))):
                        closest_hogweed = x
                else:
                    closest_hogweed = x
        if closest_hogweed is not None:
            return Field(self.x + self.dist_x_y(closest_hogweed.x, self.x),
                         self.y + self.dist_x_y(closest_hogweed.y, self.y))
        else:
            return -1

    def breed(self, x1, y1, x2, y2, other):
        f = self.breed_field(x1, y1, x2, y2, other)
        if f != -1:
            Cyber_sheep(self.world, f.x, f.y, Breeding.cyber_sheep, Strength.cyber_sheep)

    def dist_x_y(self, x, y):
        if x - y != 0:
            return (x - y)//abs(x - y)
        else:
            return 0
