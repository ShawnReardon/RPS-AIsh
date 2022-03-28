import enum
class Moves(enum.Enum):
    exit = 0
    rock = 1
    paper = 2
    scissors = 3
class Results(enum.Enum):
    P1_WIN = 1
    P2_WIN = 2
    DRAW = 3