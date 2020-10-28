import pygame
from network import Network
from player import Player

width = 500
height = 500
FPS = 60
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

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

    p = n.getP()

    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        p2 = n.send(p)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        redrawWindow(win, p, p2)

main()
