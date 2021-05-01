from src.algorithms.generators.generator import *
import random
from src.main.constants import *
class Rndmgenerator(Generator):

    def __init__(self, board, percent=0.5):
        self.board = board
        self.tiles = board.get_tiles()
        self.percent = percent
        self.count = int((COLS * COLS) * percent) * 4


    def choose_start(self, board):
        pass

    def make_step(self):
        rx = random.randint(0, COLS-1)
        ry = random.randint(0, COLS-1)
        tile = self.tiles[rx][ry]
        rn = random.randint(0,7)
        if rn == 0:
            self.board.remove_walls_tuples((rx,ry), (rx,ry+1))
        elif rn == 1:
            self.board.remove_walls_tuples((rx,ry), (rx,ry-1))
        elif rn == 2:
            self.board.remove_walls_tuples((rx,ry), (rx-1,ry))
        elif rn == 3:
            self.board.remove_walls_tuples((rx,ry), (rx+1,ry))
        elif rn == 4:
            self.board.remove_walls_tuples((rx+1,ry), (rx,ry))
        elif rn == 5:
            self.board.remove_walls_tuples((rx-1,ry), (rx,ry))
        elif rn == 6:
            self.board.remove_walls_tuples((rx,ry+1), (rx,ry))
        else:
            self.board.remove_walls_tuples((rx,ry-1), (rx,ry))
        self.count-=1


    def is_done(self):
        return self.count <= 0
