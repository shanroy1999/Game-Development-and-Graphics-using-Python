# Create and represent a checker board
# all of different pieces moving
# whose turn is it
# moving, deleting, drawing specific pieces on the board

import pygame

# relative import
from .constants import *
from .piece import Piece

class Board:
    def __init__(self):
        # Internal representation of the board
        # where red and white pieces are stored in a 2D list => tell which piece is where => 8 diff element inside each list
        self.board = []

        # Number of red and white pieces
        self.red_left = self.white_left = 12

        # red kings = white kings = 0
        self.red_kings = self.white_kings = 0
        self.create_board()

    # Draw red and black cubes on the window(win)
    def draw_squares(self, win):

        # fill entire window with black
        win.fill(BLACK)

        # Draw alternate red and black cubes on the board
        for row in range(ROWS):
            for col in range(row%2, COLS, 2):
                pygame.draw.rect(win, RED, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

        # row = 0 => row%2 = 0 => draw red square in column 0 => step by 2 => red square in column 2, 4, 6,..
        # row = 1 => row%2 = 1 => draw red square in column 1 => step by 2 => red square in column 3, 5, 7,...
        # row = 2 => row%2 = 0 => draw red square in column 0 => step by 2 => red square in column 2, 6, 6,...

    # Create the pieces on board and add them to the list for internal representation of board
    # White pieces at the top, Red pieces at the bottom
    def create_board(self):
        for row in range(ROWS):

            # interior list for each row => contains what each row will have
            self.board.append([])

            for col in range(COLS):
                # Draw the checkers alternatively
                if(col%2 == (row+1)%2):
                    if row<3:
                        self.board[row].append(Piece(row, col, WHITE))          # Draw the white pieces in rows 0,1,2
                    elif row>4:
                        self.board[row].append(Piece(row, col, RED))            # Draw the red pieces in rows 5, 6, 7
                    else:
                        self.board[row].append(0)                               # Blank seperators - seperate the pieces - blank square
                else:
                    self.board[row].append(0)

            # col = 0 and row = 0 => col%2 = 0 and (row+1)%2=1 => do not draw the piece on (0, 0)
            # col = 1 and row = 0 => col%2 = 1 and (row+1)%2=1 => draw the piece on (0, 1)
            # col = 0 and row = 1 => col%2 = 0 and (row+1)%2=0 => draw the piece on (1, 0)

    # Draw pieces and the squares on the window 'win'
    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]

                # if piece is 0 => do not draw anything
                if piece!=0:
                    piece.draw(win)

    # Swap the piece with other empty square
    # Which piece you want to move and which row, col you want to move it to
    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]

        # Move the piece to row,col
        piece.move(row, col)

        # Check if we moved into a position where we become a king i.e. are in last row/first row
        if row==ROWS-1 or row==0:
            piece.make_king()
            if piece.color == WHITE:
                self.white_kings+=1
            else:
                self.red_kings+=1

    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece!=0:
                if piece.color==RED:
                    self.red_left -= 1
                else:
                    self.white_left -= 1

    # need to pass a piece object to the move() method
    # write a method to get a piece
    def get_piece(self, row, col):
        return self.board[row][col]

    def get_valid_moves(self, piece):
        moves = {}                      # move => key, what place we can potentially move to as a (row, col)
                                        #      => value => list of moves to get to the final move

        # Diagonals to be considered
        # What is left and what is right
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        # moving the RED piece up the board
        if piece.color==RED or piece.king:
            # start => at row above the current row
            # stop => row-3 => at most 2 above the current row
            # step => -1 => move up when we increment/decrement the for loop
            moves.update(self._traverse_left(row-1, max(row-3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row-1, max(row-3, -1), -1, piece.color, right))

        # moving the White piece down the board
        if piece.color==WHITE or piece.king:
            # start => at row below the current row
            # stop => row+3 => at most 2 below the current row
            # step => 1 => move down when we increment/decrement the for loop
            moves.update(self._traverse_left(row+1, min(row+3, ROWS), 1, piece.color, left))
            moves.update(self._traverse_right(row+1, min(row+3, ROWS), 1, piece.color, right))

        return moves

    # _traverse_left and _traverse_right => returns a dictionary
    # move.update() => merges the dictionary with the current 'moves' dictionary to have as many things as we want

    # Move on the left diagonal
    # step => tells whether to go up or down while traversing through rows to the diagonals => top-left/top-right/bottom-left/bottom-right
    # left => tells where are we starting in terms of column when traversing through the left
    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}

        # last => piece that we would skip to move to wherever we wanna go
        last = []
        for r in range(start, stop, step):
            if left<0:                                  # Outside of the board
                break
            curr = self.board[r][left]

            # Empty square
            if(curr==0):
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last+skipped

                # if there is an empty space and last existed(had a value in it)
                else:
                    moves[(r, left)] = last

                # if there is empty square and last exist
                if last:
                    if step==-1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)

                    moves.update(self._traverse_left(r+step, row, step, color, left-1, skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, color, left+1, skipped=last))
                break

            # Same color piece as our current piece => then we cant move
            elif(curr.color==color):
                break
            else:
                # Other color => could potentially move over the top of it assuming empty square next
                last=[curr]
            left-=1

        return moves

    # Move on the right diagonal
    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}

        # last => piece that we would skip to move to wherever we wanna go
        last = []
        for r in range(start, stop, step):
            if right>=COLS:                                  # Outside of the board
                break
            curr = self.board[r][right]

            # Empty square
            if(curr==0):
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last+skipped

                # if there is an empty space and last existed(had a value in it)
                else:
                    moves[(r, right)] = last

                # if there is empty square and last exist
                if last:
                    if step==-1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)

                    moves.update(self._traverse_left(r+step, row, step, color, right-1, skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, color, right+1, skipped=last))
                break

            # Same color piece as our current piece => then we cant move
            elif(curr.color==color):
                break
            else:
                # Other color => could potentially move over the top of it assuming empty square next
                last=[curr]
            right+=1

        return moves

    def winner(self):
        if self.red_left<=0:
            return WHITE
        elif self.white_left <= 0:
            return RED

        return None
