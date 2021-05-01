from src.algorithms.generators.backtracker import *
from src.algorithms.generators.rndmgenerator import Rndmgenerator
from src.algorithms.solvers.breathfirstsearch import *
from src.algorithms.solvers.depthfirstsearch import *
from src.main.constants import *
from src.main.tile import Board

pygame.init()

WIN = pygame.display.set_mode([WIDTH,HEIGHT])


def main():


    # initialize board
    print("> initializing board...")
    board = Board(WIN)


    # initialize backtracking variables
    print("> initializing variables for backtracking...")
    generator = None


    # initialize search
    searcher = None

    # initializing informational variables
    print("> initializing informational variables...")
    moves = 0
    checks = 0
    path_length = 0


    # initalize font
    medium = pygame.font.Font('freesansbold.ttf', 32)
    small = pygame.font.Font('freesansbold.ttf', 20)


    # initialize buttons
    backtracking_button = pygame.Rect(30,200,200,60)
    rndmgeneration_button = pygame.Rect(30,300,200,60)
    resetmaze_button = pygame.Rect(30,400,200,60)
    breadthfirstsearch_button = pygame.Rect(WIDTH-225,200,200,60)
    depthfirstsearch_button = pygame.Rect(WIDTH-225,300,200,60)
    newstartandend_button = pygame.Rect(WIDTH-225,400,200,60)
    resetsearch_button = pygame.Rect(WIDTH-225,500,200,60)

    backtracking_text = small.render('Backtracking', True, BLACK)
    rndmgeneration_text = small.render('Rndmgeneration', True, BLACK)
    resetmaze_text = small.render('reset maze', True, BLACK)
    breadthfirstsearch_text = small.render('Breadth first search', True, BLACK)
    depthfirstsearch_text = small.render('Depth first search', True, BLACK)
    newstartandend_text = small.render('new start/end', True, BLACK)
    resetsearch_text = small.render('reset search', True, BLACK)


    # main loop
    print("> starting main loop...")
    running = True
    generator_has_run = False


    while running:


        WIN.fill((235,235,235))

        board.draw_board()
        board.draw_start_and_end()
        board.display_path()
        board.draw_walls()

        text = medium.render('Moves: {}'.format(moves), True, BLACK)
        WIN.blit(text, (35,10))
        text = medium.render('Checks: {}'.format(checks), True, BLACK)
        WIN.blit(text, (WIDTH-225,10))
        text = medium.render('Path length: {}'.format(path_length), True, BLACK)
        WIN.blit(text, (WIDTH-245,70))




        # backtracking for maze generation
        if generator:
            generator.make_step()
            moves += 1
            if generator.is_done():
                generator_has_run = True
                generator = None
                # init searching algorithm
                board.make_everything_unvisited()


        elif searcher:
            searcher.make_step()
            checks = searcher.get_checks()
            if searcher.is_done():
                path_length = searcher.give_path_to_board()
                searcher = None



        # drawing and event handeling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = event.pos
                #board.make_everything_unvisited()
                #searcher = Breathfirstsearch(board)
                #searching = True
                #checks = 0
                if not generator and backtracking_button.collidepoint(mouse_pos):
                    print("> backtracking enabled")
                    moves = 0
                    generator = Backtracker(board)

                if not generator and rndmgeneration_button.collidepoint(mouse_pos):
                    print("> rndmgeneration enabled")
                    moves = 0
                    generator = Rndmgenerator(board)

                if resetmaze_button.collidepoint(mouse_pos):
                    print("> reseting maze")
                    checks = 0
                    path_length = 0
                    moves = 0
                    generator = None
                    board = Board(WIN)
                    generator_has_run = False

                if not searcher and breadthfirstsearch_button.collidepoint(mouse_pos) and generator_has_run:
                    print("> breathfirstsearch enabled")
                    board.make_everything_unvisited()
                    board.path = []
                    if not board.start:
                        board.generate_start_and_end()
                    searcher = Breathfirstsearch(board)

                if not searcher and depthfirstsearch_button.collidepoint(mouse_pos) and generator_has_run:
                    print("> depthfirstsearch enabled")
                    board.make_everything_unvisited()
                    board.path = []
                    if not board.start:
                        board.generate_start_and_end()
                    searcher = Depthfirstsearch(board)

                if not generator and resetsearch_button.collidepoint(mouse_pos):
                    print("> reseting search")
                    board.make_everything_unvisited()
                    board.path = []
                    searcher = None

                if not generator and not searcher and newstartandend_button.collidepoint(mouse_pos) and generator_has_run:
                    print("> new start and end")
                    board.make_everything_unvisited()
                    board.path = []
                    board.generate_start_and_end()
                    searcher = None


            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                main()
                running = False

        pygame.draw.rect(WIN, LBLUE, backtracking_button)
        pygame.draw.rect(WIN, LBLUE, rndmgeneration_button)
        pygame.draw.rect(WIN, LBLUE, depthfirstsearch_button)
        pygame.draw.rect(WIN, LBLUE, breadthfirstsearch_button)
        pygame.draw.rect(WIN, LBLUE, resetmaze_button)
        pygame.draw.rect(WIN, LBLUE, newstartandend_button)
        pygame.draw.rect(WIN, LBLUE, resetsearch_button)

        WIN.blit(backtracking_text, (57,220))
        WIN.blit(rndmgeneration_text, (45,320))
        WIN.blit(resetmaze_text, (70,420))
        WIN.blit(breadthfirstsearch_text, (WIDTH-220,220))
        WIN.blit(depthfirstsearch_text, (WIDTH-210,320))
        WIN.blit(newstartandend_text, (WIDTH-190,420))
        WIN.blit(resetsearch_text, (WIDTH-190,520))

        pygame.display.flip()
        pygame.display.update()


    print("> quitting simulation...")
    pygame.quit()


#####################################
############   Start    #############
#####################################

# initialize board

# run main loop
main()
