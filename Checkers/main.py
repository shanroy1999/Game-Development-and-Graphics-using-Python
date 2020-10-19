import pygame

# import all the constants from the constants package
from checkers.constants import *

# import the class "Board"
from checkers.board import Board
from checkers.game import Game

# Frames per second => for rendering and drawing the game
FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Name of the game displayed on bar
pygame.display.set_caption("Checkers")

# Take position of our mouse and based on that position will tell us which row/column we are in
def get_row_col_from_mouse(pos):
    x, y = pos
    row = y//SQUARE_SIZE
    col = x//SQUARE_SIZE
    return row, col

# function to actually run the game
def main():
    run = True

    # Make sure game doesn't run too fast or too slow
    clock = pygame.time.Clock()

    # Create a Game object which will control the board for us
    game = Game(WIN)

    # Create an event loop while the game is running
    while run:
        clock.tick(FPS)

        if game.winner() != None:
            print(game.winner())
            run = False

        # Check for any events happening at current time
        for event in pygame.event.get():

            # End the game and get rid of window by clicking the cross
            if event.type == pygame.QUIT:
                run = False

            # If we press any button on mouse, we first get the row, column we are in
            # Then we will select the piece on that location and move that to wherever we want to move
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()

    pygame.quit()

main()
