# Store all the constants and then access them using the checkers package

import pygame

# DIMENSIONS
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 8, 8               # Amount of rows and columns in our checkers board => standard size is 8x8
SQUARE_SIZE = WIDTH//COLS       # How big is one square of our checkers board = 75x75

# COLORS(RGB)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)

# load crown image for placing on the king piece => scale the image(keeping the aspect ratio reserved)
CROWN = pygame.transform.scale(pygame.image.load('assets/king.png'), (44, 25))
