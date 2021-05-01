import pygame

from src.main.constants import *


class Breathfirstsearch():

    def __init__(self, board):
        self.board = board
        self.tiles = board.get_tiles()
        self.queue = []
        self.current = board.start
        self.last_added = []
        self.end = board.end
        self.start = board.start
        self.queue.append(self.current)
        self.checks = 0


    def give_path_to_board(self):
        pass


    def make_step(self):
        self.last_added = []

        if len(self.queue) > 0:
            self.current = self.queue.pop(0)
            self.current.make_visited()
            childs = self.current.get_neighbours_search(self.tiles)
            for tile in childs:
                self.checks+=1
                tile.make_visited()
                self.last_added.append(tile)
                self.queue.append(tile)


    def is_done(self):
        if len(self.queue) == 0: return True
        for tile in self.last_added:
            if tile == self.end: return True
        return False

    def draw_start_and_end(self, WIN):
        pygame.draw.rect(WIN, STARTCOLOR, (self.start.x, self.start.y, TILESIZE, TILESIZE))
        pygame.draw.rect(WIN, ENDCOLOR, (self.end.x, self.end.y, TILESIZE, TILESIZE))


    def get_checks(self):
        return self.checks-1
