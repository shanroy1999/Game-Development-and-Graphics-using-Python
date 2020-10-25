from copy import deepcopy
# Shallow copy => creates a new copy which stores reference of original element => copies reference of nested objects
# Changing the original element => also changes the element in the shallow copy
# old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]] => [[1, 1, 1], [2, 'AA', 2], [3, 3, 3]]
# new_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]] => [[1, 1, 1], [2, 'AA', 2], [3, 3, 3]]

# Deep copy => create a new copy and recursively add copies of nested objects present in original element
# Changing the original element => no change to the element in the deep copy
# old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]] => [[1, 1, 1], [2, 'AA', 2], [3, 3, 3]]
# new_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]] => [[1, 1, 1], [2, 2, 2], [3, 3, 3]]

import pygame

RED = (255, 0, 0)
WHITE = (255, 255, 255)

# position => current position
# pass the current board in the minimax algorithm => get the best board after those positions
# depth => depth of the tree => how far extending the tree
# max_player => boolean => whether minimizing the value or maximizing the value
# game => game object
def minimax(position, depth, max_player, game):
    if depth==0 or position.winner() != None:               # depth = 0 => last node in the tree or game over => no need to continue
        return position.evaluate(), position

    # maximize the score
    if max_player:
        maxEval = float('-inf')
        best_move = None                # store the best move we can make

        # for every single move that we can potentially make => evaluate that move
        for move in get_all_moves(position, WHITE, game):
            evaluation = minimax(move, depth-1, False, game)[0]
            maxEval = max(maxEval, evaluation)          # is the move better than move that we already have
            if maxEval==evaluation:
                best_move = move
        return maxEval, best_move

    # minimize the score
    else:
        minEval = float('inf')
        best_move = None                # store the best move we can make

        # for every single move that we can potentially make => evaluate that move
        for move in get_all_moves(position, RED, game):
            evaluation = minimax(move, depth-1, True, game)[0]
            minEval = min(minEval, evaluation)          # is the move better than move that we already have
            if minEval==evaluation:
                best_move = move
        return minEval, best_move

def get_all_moves(board, color, game):
    moves = []                              # Store the new board
    # moves = [[new_board1, piece1], [new_board2, piece2]] => if we move the 'piece1' then the new board will be 'new_board1'....

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)          # get all the valid moves for that piece
        for move, skip in valid_moves.items():
            # valid_moves.items() => dictionary => (row, col) : [pieces] => pieces that we skip to move to the position (row, col)

            # Make copy every time => To determine what the new board will look like on moving to position
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)
            # if we move the 'piece' => new board will be 'new_board' => score that board and see which board is the best and return it

    return moves

# take the piece, take the move to make, take the temporary board and then make the move on it and return new board after that move
def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)
    return board
