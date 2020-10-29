# Hold all the information for the game
class Game:
    def __init__(self, id):
        # Whether player 1 or player 2 have made a move
        self.p1went = False
        self.p2went = False
        self.ready = False
        self.id = id            # Each game => has an id => to see which player is part of which game
        self.moves = [None, None]   # Keep track of the players moves
        self.wins = [0, 0]      # Keep track of the wins
        self.tie = 0

    # Get the moves of the specified player
    # p => [0, 1] => player1->0 and player2->1
    def get_player_move(self, p):
        return self.moves[p]

    # which player has to make which move
    def play(self, player, move):
        self.moves[player] = move
        if player==0:
            self.p1went = True
        else:
            self.p2went = True

    # Check if two players are currently connected to the game
    def connected(self):
        return self.ready

    # Check whether both the players have made their moves
    def bothWent(self):
        return self.p1went and self.p2went

    # Check which player has won the game
    def winner(self):
        p1 = self.moves[0].upper()[0]           # Get the first letter of the moves => 'Rock'/'Paper'/'Scissor'
        p2 = self.moves[1].upper()[0]

        winner = -1                             # Could be a tie
        if p1 == "R" and p2 == "S":
            winner = 0
        elif p1 == "S" and p2 == "R":
            winner = 1
        elif p1 == "P" and p2 == "R":
            winner = 0
        elif p1 == "R" and p2 == "P":
            winner = 1
        elif p1 == "S" and p2 == "P":
            winner = 0
        elif p1 == "P" and p2 == "S":
            winner = 1

        return winner

    # Reset the game
    def reset(self):
        self.p1went = False
        self.p2went = False
