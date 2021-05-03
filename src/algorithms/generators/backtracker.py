from src.algorithms.generators.generator import Generator


class Backtracker(Generator):

    def __init__(self, board):
        self.board = board
        self.current = self.choose_start(board)
        self.initial = self.current
        self.stack = []


    def choose_start(self, board):
        tiles = self.board.get_tiles()
        return tiles[0][0]


    def make_step(self):
        self.current.make_visited()

        neighbour = self.current.choose_next(self.board.get_tiles())
        if neighbour:
            neighbour.make_visited()

            self.stack.append(self.current)

            self.board.remove_walls(self.current, neighbour)

            self.current = neighbour
        elif len(self.stack) > 0:
            self.current = self.stack.pop()

        self.current.highlight()

    def is_done(self):
        return len(self.current.get_neighbours(self.board.get_tiles())) == 0 and len(self.stack) == 0
