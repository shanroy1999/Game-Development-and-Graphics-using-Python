import pygame
from network import Network
import pickle

pygame.font.init()

width = 600
height = 600
FPS = 60
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

class Button:
    def __init__(self, text, x, y, color):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = 150
        self.height = 50

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("comicsans", 40)
        text = font.render(self.text, 1, (255, 255, 255))
        win.blit(text, (self.x + round(self.width/2) - round(text.get_width()/2), self.y + round(self.height/2) - round(text.get_height()/2)))

    # check if we clicked on the button or not
    # pos => tuple (x, y) coordinate of mouse position => check whether it lies in the button or not
    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False

# Update display
def redrawWindow(win, game, p):
    win.fill((128, 128, 128))

    if not(game.connected()):
        font = pygame.font.SysFont("comicsans", 80)
        text = font.render("Waiting for player...", 1, (255, 0, 0), True)
        win.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
    else:
        font = pygame.font.SysFont("comicsans", 60)
        text = font.render("Your Move", 1, (0, 255, 255))
        win.blit(text, (50, 200))

        text = font.render("Opponent's", 1, (0, 255, 255))
        win.blit(text, (320, 200))

        # Get the moves of both the players
        move1 = game.get_player_move(0)
        move2 = game.get_player_move(1)

        # When both players have made the moves
        if game.bothWent():
            text1 = font.render(move1, 1, (0, 0, 0))
            text2 = font.render(move2, 1, (0, 0, 0))
        else:
            if game.p1went and p==0:
                text1 = font.render(move1, 1, (0, 0, 0))
            elif game.p1went:
                text1 = font.render("Locked In", 1, (0, 0, 0))
            else:
                text1 = font.render("Waiting...", 1, (0, 0, 0))

            if game.p2went and p==1:
                text2 = font.render(move2, 1, (0, 0, 0))
            elif game.p2went:
                text2 = font.render("Locked In", 1, (0, 0, 0))
            else:
                text2 = font.render("Waiting...", 1, (0, 0, 0))

        if p==1:
            win.blit(text2, (70, 350))
            win.blit(text1, (350, 350))
        else:
            win.blit(text1, (70, 350))
            win.blit(text2, (350, 350))

        for btn in btns:
            btn.draw(win)

    pygame.display.update()

# Buttons for Rock, Paper and Scissors
btns = [Button("Rock", 50, 500, (0, 0, 0)), Button("Paper", 250, 500, (255, 0, 0)), Button("Scissors", 450, 500, (0, 255, 0))]

# Main loop
def main():
    run = True
    clock = pygame.time.Clock()
    n = Network()
    player = int(n.getP())
    print("You are player", player)
    while run:
        clock.tick(FPS)
        try:
            game = n.send("get")
        # If we don't get response from the server => game doesn't exist
        except:
            run = False
            print("Couldn't get game")
            break

        # If both players are ready => see which one won the game
        if game.bothWent():
            redrawWindow(win, game, player)              # Make sure both players are ready
            pygame.time.delay(500)
            try:
                game = n.send("reset")      # Tell the server to reset the player move
            except:
                run = False
                print("Couldn't get game")
                break

            # Display text for which player won and which player lost
            font = pygame.font.SysFont("comcicsans", 70)
            if (game.winner() == 1 and player == 1) or (game.winner() == 0 and player == 0):
                text = font.render("You Won!", 1, (0, 255, 0))
            elif game.winner() == -1:
                text = font.render("Tie Game", 1, (255, 0, 0))
            else:
                text = font.render("You Lost...", 1, (255, 0, 0))

            win.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2 - 200))
            pygame.display.update()
            pygame.time.delay(2000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for btn in btns:
                    # If we click on it and the game is connected
                    if btn.click(pos) and game.connected():
                        if player==0:
                            # Check if player 1 has gone yet
                            if not game.p1went:
                                n.send(btn.text)
                        else:
                            # Check if player 2 has gone yet
                            if not game.p2went:
                                n.send(btn.text)

        redrawWindow(win, game, player)

def menu_screen():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        win.fill((128, 128, 128))
        font = pygame.font.SysFont("comicsans", 50)
        text = font.render("Click to Play!", 1, (255, 0, 0))
        win.blit(text, (210, 250))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False

    main()

while True:
    menu_screen()
