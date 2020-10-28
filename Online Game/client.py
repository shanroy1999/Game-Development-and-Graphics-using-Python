import pygame
from network import Network

width = 500
height = 500
FPS = 60
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clientNumber = 0

# Creating the player character
class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.vel = 3

    # Draw the rectangle to the screen/window
    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()        # Check which key pressed

        if keys[pygame.K_LEFT]:
            self.x-=self.vel

        if keys[pygame.K_RIGHT]:
            self.x+=self.vel

        if keys[pygame.K_UP]:
            self.y-=self.vel

        if keys[pygame.K_DOWN]:
            self.y+=self.vel

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)

def read_pos(s):
    str = s.split(",")
    return int(str[0]), int(str[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

# Update display
def redrawWindow(win, player, player2):
    win.fill((255, 255, 255))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()

# Main loop
def main():
    run = True
    # Connect to the server
    n = Network()
    startPos = read_pos(n.getPos())           # get the position from the server => eg: "45,67"

    # Create player 1
    p = Player(startPos[0], startPos[1], 100, 100, (0, 255, 0))       # Use the starting position to determine where we are starting

    # Create player 2
    p2 = Player(0, 0, 100, 100, (255, 0, 0))

    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)

        p2Pos = read_pos(n.send(make_pos((p.x, p.y))))
        p2.x = p2Pos[0]
        p2.y = p2Pos[1]
        p2.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        redrawWindow(win, p, p2)

main()
