from enum import Enum


class Density(Enum):
    wolf = 0.035
    sheep = 0.09
    fox = 0.04
    turtle = 0.03
    antelope = 0.07
    cyber_sheep = 0.01
    grass = 0.07
    dandelion = 0.04
    guarana = 0.06
    belladonna = 0.017
    hogweed = 0.01


class Breeding(Enum):
    human = 0
    wolf = 4
    sheep = 3
    fox = 4
    turtle = 2
    antelope = 4
    cyber_sheep = 6
    grass = 20
    dandelion = 10
    guarana = 14
    belladonna = 12
    hogweed = 5
    plant_cd = 0

class ID(Enum):
    human = 0
    wolf = 1
    sheep = 2
    fox = 3
    turtle = 4
    antelope = 5
    cyber_sheep = 6
    grass = 7
    dandelion = 8
    guarana = 9
    belladonna = 10
    hogweed = 11


class Initiative(Enum):
    human = 4
    wolf = 5
    sheep = 4
    fox = 7
    turtle = 1
    antelope = 4
    plant = 0
    cyber_sheep = 4


class Spread(Enum):
    grass = 20
    dandelion = 15
    guarana = 17
    belladonna = 12
    hogweed = 10


class Strength(Enum):
    human = 5
    wolf = 9
    sheep = 4
    fox = 3
    turtle = 2
    antelope = 4
    cyber_sheep = 11
    grass = 0
    dandelion = 0
    guarana = 0
    belladonna = 99
    hogweed = 10


class Symbol(Enum):
    human = '@'
    wolf = 'W'
    sheep = 'S'
    fox = 'F'
    turtle = 'T'
    antelope = 'A'
    cyber_sheep = 'C'
    grass = '#'
    dandelion = '^'
    guarana = '+'
    belladonna = '$'
    hogweed = '%'


class Background(Enum):
    human = '#cc24be'
    wolf = '#000000'
    sheep = '#3657c4'
    fox = '#596366'
    turtle = '#596366'
    antelope = '#f18723'
    cyber_sheep = '#c91212'
    plant = '#58ce27'


class Foreground(Enum):
    human = '#1221c9'
    wolf = '#ffffff'
    sheep = '#ffffff'
    fox = '#c62525'
    turtle = '#e29c9c'
    antelope = '#ffffff'
    cyber_sheep = '#ffffff'
    grass = '#08cc18'
    dandelion = '#fffa00'
    guarana = '#c10f0f'
    belladonna = '#ba20bc'
    hogweed = '#ffffff'

class Human_moves(Enum):
    up = 1
    right = 2
    down = 3
    left = 4
    super = 99
