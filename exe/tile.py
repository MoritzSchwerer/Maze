import pygame
import random
from src.main.constants import *
class Tile:


    def __init__ (self, x, y):

        self.color = TILECOLOR
        self.top_wall = True
        self.right_wall = True
        self.bottom_wall = True
        self.left_wall = True
        self.is_start = False
        self.is_end = False
        self.x = x * TILESIZE + BORDERRIGHTLEFT
        self.y = y * TILESIZE
        self.xInList = x
        self.yInList = y


    def get_neighbours(self, tiles):

        x = self.xInList
        y = self.yInList
        neighbours = []

        # top
        temp = tiles[x][y]
        if self.yInList > 0 and not tiles[x][y-1].is_visited():
            neighbours.append(tiles[x][y-1])

        # right
        if self.xInList < COLS-1 and not tiles[x+1][y].is_visited():
            neighbours.append(tiles[x+1][y])

        # bottom
        if self.yInList < ROWS-1 and not tiles[x][y+1].is_visited():
            neighbours.append(tiles[x][y+1])

        # left
        if self.xInList > 0 and not tiles[x-1][y].is_visited():
            neighbours.append(tiles[x-1][y])

        return neighbours


    def get_neighbours_search(self, tiles):

        x = self.xInList
        y = self.yInList
        neighbours = []


        # top
        temp = tiles[x][y]
        if self.yInList > 0 and not tiles[x][y-1].is_visited() and not temp.top_wall:
            neighbours.append(tiles[x][y-1])

        # right
        if self.xInList < COLS-1 and not tiles[x+1][y].is_visited() and not temp.right_wall:
            neighbours.append(tiles[x+1][y])

        # bottom
        if self.yInList < ROWS-1 and not tiles[x][y+1].is_visited() and not temp.bottom_wall:
            neighbours.append(tiles[x][y+1])

        # left
        if self.xInList > 0 and not tiles[x-1][y].is_visited() and not temp.left_wall:
            neighbours.append(tiles[x-1][y])

        return neighbours


    # get a random neighbour
    def choose_next(self, tiles):
        neighbours = self.get_neighbours(tiles)

        if len(neighbours) > 0:
            rndm = random.randint(0, len(neighbours) - 1)
            return neighbours[rndm]

        return None


    def choose_next_search(self, tiles):
        neighbours = self.get_neighbours_search(tiles)

        if len(neighbours) > 0:
            rndm = random.randint(0, len(neighbours) - 1)
            return neighbours[rndm]

        return None


    def highlight(self):
        self.color = DBLUE


    def remove_top_wall(self):
        self.top_wall = False


    def remove_right_wall(self):
        self.right_wall = False


    def remove_bottom_wall(self):
        self.bottom_wall = False


    def remove_left_wall(self):
        self.left_wall = False


    def make_path(self):
        self.color = PURPLE


    def make_visited(self):
        self.color = LIGHTPURPLE


    def is_visited(self):
        return self.color == LIGHTPURPLE


    def make_start(self):
        self.is_start = True
        self.color = BLUE


    def make_end(self):
        self.is_end = True
        self.color = BLACK


    def is_start(self):
        return self.is_start


    def is_end(self):
        return self.is_end


    def draw(self, WIN):
        pygame.draw.rect(WIN, self.color, (self.x, self.y, TILESIZE, TILESIZE))


    def draw_walls(self, WIN):
        if self.top_wall:
            pygame.draw.line(WIN, WALLCOLOR, (self.x, self.y), (self.x + TILESIZE, self.y), width=2)
        if self.right_wall:
            pygame.draw.line(WIN, WALLCOLOR, (self.x + TILESIZE, self.y), (self.x + TILESIZE, self.y + TILESIZE), width=2)
        if self.bottom_wall:
            pygame.draw.line(WIN, WALLCOLOR, (self.x, self.y + TILESIZE), (self.x + TILESIZE, self.y + TILESIZE), width=2)
        if self.left_wall:
            pygame.draw.line(WIN, WALLCOLOR, (self.x, self.y), (self.x, self.y + TILESIZE), width=2)


class Board:


    def __init__(self, WIN):
        self.tiles = self.initialize_tiles()
        self.WIN = WIN
        self.start = None
        self.end = None
        self.path = []


    def generate_start_and_end(self):
        self.start = self.choose_node()
        self.end = self.choose_node()


    def choose_node(self):
        rx = random.randint(0,COLS-1)
        ry = random.randint(0,COLS-1)
        tile = self.tiles[rx][ry]
        return tile


    def initialize_tiles(self):
        tiles = []
        for row in range(ROWS):
            temp = []

            for col in range(COLS):
                temp.append(Tile(row,col))

            tiles.append(temp)

        return tiles


    # first draw the tile colors and then the walls on top
    def draw_board(self):
        for row in self.tiles:
            for tile in row:
                tile.draw(self.WIN);


    def draw_walls(self):
        for row in self.tiles:
            for tile in row:
                tile.draw_walls(self.WIN);


    def get_tiles(self):
        return self.tiles


    def remove_walls(self, current , neighbour):
        x = current.xInList - neighbour.xInList
        y = current.yInList - neighbour.yInList

        if x == 1:
            current.remove_left_wall()
            neighbour.remove_right_wall()
        elif x == -1:
            current.remove_right_wall()
            neighbour.remove_left_wall()

        if y == 1:
            current.remove_top_wall()
            neighbour.remove_bottom_wall()
        elif y == -1:
            current.remove_bottom_wall()
            neighbour.remove_top_wall()


    def remove_walls_tuples(self, current , neighbour):
        x1,y1 = current
        x2,y2 = neighbour
        x = x1-x2
        y = y1-y2

        # go left
        if x == 1:
            if x2 >= 0 and x1 < COLS:
                self.tiles[x1][y1].remove_left_wall()
                self.tiles[x2][y2].remove_right_wall()
        # go right
        elif x == -1:
            if x2 < COLS and x1 >= 0:
                self.tiles[x1][y1].remove_right_wall()
                self.tiles[x2][y2].remove_left_wall()
        # go up
        if y == 1:
            if y2 >= 0 and y1 < COLS:
                self.tiles[x1][y1].remove_top_wall()
                self.tiles[x2][y2].remove_bottom_wall()
        # go down
        elif y == -1:
            if y2 < COLS and y1 >= 0:
                self.tiles[x1][y1].remove_bottom_wall()
                self.tiles[x2][y2].remove_top_wall()


    def make_everything_unvisited(self):
        for row in range(COLS):
            for col in range(COLS):
                self.tiles[row][col].color = TILECOLOR


    def draw_start_and_end(self):
        if self.start and self.end:
            pygame.draw.rect(self.WIN, STARTCOLOR, (self.start.x, self.start.y, TILESIZE, TILESIZE))
            pygame.draw.rect(self.WIN, ENDCOLOR, (self.end.x, self.end.y, TILESIZE, TILESIZE))


    def display_path(self):
        for tile in self.path:
            tile.make_path()
