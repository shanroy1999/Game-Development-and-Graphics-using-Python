# Interact with the board, checkers, etc
# Responsible for Handling the game
# Who's turn is it, did we select the piece, can we move the piece here and there

import pygame
from .constants import *
from checkers.board import Board

class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    # Update pygame display using this method
    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    # Initilizing => private method init
    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = RED

        # dictionary of valid possible moves that can be taken from a position
        self.valid_moves = {}

    # Reset the game
    def reset(self):
        self._init()

    # When select something => call the select method, tell the row and col selected and do something based on that
    def select(self, row, col):

        # Move the already selected piece to the desired row,col
        if self.selected:
            result = self._move(row, col)

            # If incorrect/invalid move => reset the selection and reselect row and col
            if not result:
                self.selected = None
                self.select(row, col)

        piece = self.board.get_piece(row, col)

        # not selecting an empty piece and the color of the piece is same as the turn
        if piece!=0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True

        return False

    # Move currently selected piece to the row and col
    def _move(self, row, col):
        piece = self.board.get_piece(row, col)

        # If we have selected something and the piece that we selected is empty and the row, col is a valid move then we can move it
        if self.selected and piece==0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False

        return True

    # Change the turn after the move
    def change_turn(self):
        self.valid_moves = []
        if self.turn==RED:
            self.turn = WHITE
        else:
            self.turn = RED

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE, (col*SQUARE_SIZE + SQUARE_SIZE//2, row*SQUARE_SIZE + SQUARE_SIZE//2), 15)

    def winner(self):
        return self.board.winner()
