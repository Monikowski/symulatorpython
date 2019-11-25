from parents.Organism import Organism, Field
import random


class Animal(Organism):

    def __init__(self, world, x, y, cd, strength):
        super().__init__(world, x, y, cd, strength)

    def action(self):
        self.move(1)

    def breed_field(self, x1, y1, x2, y2, other):
        if (self.cd == 0) and (other.cd == 0):
            self.cd += self.breeding
            other.cd += other.breeding
            breeding_list = [[] for _ in range(8)]
            counter = 0
            counter += self.check_breeding(breeding_list, x1, y1, counter)
            counter += self.check_breeding(breeding_list, x2, y2, counter)
            if counter > 0:
                index = random.randint(0, counter - 1)
                new_x = 0
                new_y = 0
                new_x += breeding_list[index][0]
                new_y += breeding_list[index][1]
                return Field(new_x, new_y)
            else:
                return -1
        return -1

    def fight(self, opponent, new_x, new_y):
        if self.id == opponent.id:
            self.breed(self.x, self.y, new_x, new_y, opponent)
        elif opponent.collision(self):
            if self.strength >= opponent.strength:
                opponent.death(self)
            else:
                self.death(opponent)

    def check_breeding(self, moves_list, x1, y1, ctr):
        counter = ctr
        how_many = 0
        if (x1 + 1) < self.world.width and (not self.world.organisms_board[x1 + 1][y1].occupied):
            moves_list[counter + how_many].append(x1+1)
            moves_list[counter + how_many].append(y1)
            how_many += 1
        if (x1 - 1) > -1 and (not self.world.organisms_board[x1 - 1][y1].occupied):
            moves_list[counter + how_many].append(x1-1)
            moves_list[counter + how_many].append(y1)
            how_many += 1
        if (y1 - 1) > -1 and (not self.world.organisms_board[x1][y1 - 1].occupied):
            moves_list[counter + how_many].append(x1)
            moves_list[counter + how_many].append(y1 - 1)
            how_many += 1
        if (y1 + 1) < self.world.height and (not self.world.organisms_board[x1][y1 + 1].occupied):
            moves_list[counter + how_many].append(x1)
            moves_list[counter + how_many].append(y1 + 1)
            how_many += 1
        return how_many

    def move(self, move_range):
        f = self.random_field(move_range)
        new_x = f.x
        new_y = f.y

        if new_x != self.x or new_y != self.y:
            if self.world.organisms_board[new_x][new_y].occupied:
                self.fight(self.world.organisms_board[new_x][new_y].organism, new_x, new_y)

            if (not self.dead) and (not self.world.organisms_board[new_x][new_y].occupied):
                self.world.organisms_board[self.x][self.y].occupied = False
                self.world.organisms_board[new_x][new_y].organism = self
                self.world.organisms_board[new_x][new_y].occupied = True
                self.x += (new_x - self.x)
                self.y += (new_y - self.y)

    def random_field(self, move_range):
        new_x = self.x
        new_y = self.y
        while (new_x == self.x) and (new_y == self.y):
            while True:
                new_x = self.x + random.randint(-move_range, move_range)
                if (new_x >= 0) and (new_x < self.world.width):
                    break
            while True:
                new_y = self.y + random.randint(-move_range, move_range)
                if (new_y >= 0) and (new_y < self.world.height):
                    break
        return Field(new_x, new_y)

