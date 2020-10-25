# Create all the Pieces on the board
# White pieces => move down
# Red pieces => move up
# King => can move in backward direction

import pygame
from .constants import *

class Piece:
    # padding for the checker circle in the middle of the squares
    PADDING = 15

    # outline of the circle
    BORDER = 2

    # which row, column the piece is located and what is the color of that piece
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

        # Tell whether the piece is a king or not
        self.king = False

        self.x = 0
        self.y = 0
        self.cal_pos()

    # Calculate x and y position based on row and column we are in
    def cal_pos(self):
        # Middle of the square
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE//2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE//2

    # Convert the checker into a King if possible
    def make_king(self):
        self.king = True

    # Draw the checker piece inside the square
    def draw(self, win):
        radius = SQUARE_SIZE//2 - self.PADDING

        # Draw circle on window 'win' of color grey and x,y as center of circle with a 'radius' and a border around
        # Larger circle -> slightly outside the inner circle
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.BORDER)

        # Small Circle inside the larger circle
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)

        # Draw the king image on the piece
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2))

    # internal representation of the object => replace the output "<object at 0xlocation...>"
    def __repr__(self):
        return str(self.color)

    def move(self, row, col):
        self.row = row
        self.col = col
        self.cal_pos()


