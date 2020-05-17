import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600
car_width = 73

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('RACEY RACE')

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
bright_red = (255,0,0)
green = (0,200,0)
bright_green = (0,255,0)
blue = (0,0,255)
block_color = (53,115,255)

clock = pygame.time.Clock()
carImg = pygame.image.load(r'C:\Users\Lenovo\Desktop\New folder\python\Small Projects\Game Development and Graphics\racecar.jpg')
pygame.display.set_icon(carImg)

def car(x,y):
    gameDisplay.blit(carImg, (x,y))

def things(tx, ty, tw, th, color):
    if(tx+tw<=display_width and tx+tw>=0):
        pygame.draw.rect(gameDisplay, color, [tx,ty,tw,th])

def things_dodged(count):
    font = pygame.font.SysFont("comicsans",50)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text, (0,0))

def text_objects(text, style):
    textSurface = style.render(text, True, blue)
    return textSurface, textSurface.get_rect()

def message_display(text):
    font = pygame.font.SysFont("comicsans",50)
    TextSurf, TextRect = text_objects(text, font)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    time.sleep(2)
    game_loop()

def crash():
    font = pygame.font.SysFont("comicsans",100)
    TextSurf, TextRect = text_objects("YOU CRASHED", font)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    while True:
        for event in pygame.event.get():
            if(event.type==pygame.QUIT):
                pygame.quit()
                quit()
        #gameDisplay.fill(white)

        button("PLAY AGAIN",200,400,150,50,green,bright_green,"play")
        button("QUIT",500,400,100,50,red,bright_red,"quit")

        pygame.display.update()
        clock.tick(15)


def button(msg,x,y,w,h,inactive,active,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if(x+w>mouse[0]>x and y+h>mouse[1]>y):
        pygame.draw.rect(gameDisplay, active, (x,y,w,h))
        if(click[0]==1 and action!="None"):
            if(action=="play"):
                game_loop()
            elif(action=="quit"):
                pygame.quit()
                quit()
            elif(action=="continue"):
                unpause()
    else:
        pygame.draw.rect(gameDisplay, inactive, (x,y,w,h))

    font = pygame.font.SysFont("comicsans",25)
    TextSurf, TextRect = text_objects(msg, font)
    TextRect.center = ((x+(w/2)),(y+(h/2)))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

def quitgame():
    pygame.quit()
    quit()

def unpause():
    global pause
    pause = False

def paused():

    font = pygame.font.SysFont("comicsans",100)
    TextSurf, TextRect = text_objects("PAUSED", font)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    while pause:
        for event in pygame.event.get():
            if(event.type==pygame.QUIT):
                pygame.quit()
                quit()
        #gameDisplay.fill(white)

        button("CONTINUE",200,400,150,50,green,bright_green,"continue")
        button("QUIT",500,400,100,50,red,bright_red,"quit")

        pygame.display.update()
        clock.tick(15)

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if(event.type==pygame.QUIT):
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        font = pygame.font.SysFont("comicsans",100)
        TextSurf, TextRect = text_objects("RACEY RACE", font)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("LETS GO!",200,400,100,50,green,bright_green,"play")
        button("QUIT",500,400,100,50,red,bright_red,"quit")

        pygame.display.update()
        clock.tick(15)


def game_loop():
    global pause

    x =  (display_width * 0.45)
    y = (display_height * 0.8)
    crashed = False
    x_change = 0
    car_speed = 0
    tx_start = random.randrange(0,display_width)
    ty_start = -600
    t_speed = 10
    t_width = 100
    t_height = 100
    dodged = 0

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -15
                elif event.key == pygame.K_RIGHT:
                    x_change = 15
                if event.key == pygame.K_SPACE:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        gameDisplay.fill(white)

        things(tx_start,ty_start,t_width,t_height,block_color)
        ty_start += t_speed
        car(x,y)
        things_dodged(dodged)

        if(x>display_width-car_width or x<0):
            crash()

        if(ty_start>display_height):
            ty_start = 0 - t_height
            tx_start = random.randrange(0,display_width-car_width)
            dodged+=1
            t_speed+=1
            t_width+=(dodged*1.2)

        if(y<ty_start+t_height):
            if((x>tx_start) and (x<tx_start+t_width) or (x+car_width>tx_start) and (x+car_width<tx_start+t_width)):
                crash()

        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()
