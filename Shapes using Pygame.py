import pygame

pygame.init()

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)
white = (255,255,255)

win = pygame.display.set_mode((800,600))
win.fill(black)

pixel = pygame.PixelArray(win)
pixel[10][20] = red

pygame.draw.line(win, red, (100,200), (400,450), 5)
pygame.draw.rect(win, green, (400,450,50,25), 5)
pygame.draw.circle(win, blue, (500,500), 50)
pygame.draw.polygon(win, red, ((500,500),(120,200),(300,100)))

while True:
    for event in pygame.event.get():
        if(event.type==pygame.QUIT):
            pygame.quit()
            quit()

    pygame.display.update()
