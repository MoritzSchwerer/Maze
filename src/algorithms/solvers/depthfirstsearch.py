import random

from src.main.constants import *


class Depthfirstsearch():

    def __init__(self, board):

        self.board = board
        self.tiles = board.get_tiles()
        self.stack = []
        self.current = board.start
        self.start = board.start
        self.end = board.end
        self.checks = 0


    def choose_current(self):
        rx = random.randint(0,COLS-1)
        ry = random.randint(0,COLS-1)
        tile = self.tiles[rx][ry]
        return tile


    def choose_end(self):
        rx = random.randint(0,COLS-1)
        ry = random.randint(0,COLS-1)
        tile = self.tiles[rx][ry]
        return tile


    def give_path_to_board(self):
        list = []
        for tile in self.stack:
            list.append(tile)
        self.board.path = list
        return len(list)


    def make_step(self):
        self.checks+=1
        self.current.make_visited()

        neighbour = self.current.choose_next_search(self.board.get_tiles())

        if not neighbour == None:
            neighbour.make_visited()

            self.stack.append(self.current)

            self.current = neighbour

        elif len(self.stack) > 0:
            self.current = self.stack.pop()

        self.current.draw()
        self.current.draw_walls()
        #self.current.highlight()


    def is_done(self):
        return self.current == self.end


    def get_checks(self):
        return self.checks
