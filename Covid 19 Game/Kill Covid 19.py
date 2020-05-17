import pygame
import random
import math
from pygame import mixer

#initialize pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))

#Background
bg = pygame.image.load(r"C:\Users\Lenovo\Desktop\New folder\python\Small Projects\Game Development and Graphics\Covid 19\ind.png")

#Background Sound
mixer.music.load(r"C:\Users\Lenovo\Desktop\New folder\python\Small Projects\Game Development and Graphics\Covid 19\background.wav")
mixer.music.play(-1)

#Title and Icon
pygame.display.set_caption("Kill COVID19")
icon = pygame.image.load(r"C:\Users\Lenovo\Desktop\New folder\python\Small Projects\Game Development and Graphics\Covid 19\spaceship.png")
pygame.display.set_icon(icon)

#Add Player
playerimg = pygame.image.load(r'C:\Users\Lenovo\Desktop\New folder\python\Small Projects\Game Development and Graphics\Covid 19\space-invaders.png')

#Coordinates of Player
playerX = 370
playerY = 480
playerX_change = 0

#Add Multiple enemies
enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
n_enemies = 6

for i in range(n_enemies):
    enemyimg.append(pygame.image.load(r'C:\Users\Lenovo\Desktop\New folder\python\Small Projects\Game Development and Graphics\Covid 19\coronavirus.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

#Bullet
bulletimg = pygame.image.load(r'C:\Users\Lenovo\Desktop\New folder\python\Small Projects\Game Development and Graphics\Covid 19\bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"          #ready - Cant see the bullet on screen

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

over_font = pygame.font.Font('freesansbold.ttf', 64)

def game_over_text():
    over_text = font.render("GAME OVER", True, (0,0,0))
    screen.blit(over_text, (200,250))

def showscore(x,y):
    score = font.render("Score: "+str(score_value), True, (255,255,255))
    screen.blit(score, (x, y))
    creator = font.render("Created By: Shantanu Roy", True, (255,255,0))
    screen.blit(creator, (x, y+30))

def player(x,y):
    screen.blit(playerimg, (x, y))

def enemy(x,y,i):
    screen.blit(enemyimg[i], (x, y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"               #fire - bullet currently moving
    screen.blit(bulletimg, (x+16, y+10))            #Make sure bullet appear on center and above of spaceship

def isCollision(enemyX,enemyY,bulletX,bulletY):
    dist = math.sqrt((math.pow(enemyX-bulletX,2)) + (math.pow(enemyY-bulletY,2)))
    if dist<27:
        return True
    else:
        return False

#Game Loop
running = True

#Infinite Game Loop
while running:
    screen.fill((0,0,0))                #Background

    #Add background image
    screen.blit(bg, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke pressed => check R or L
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5               #Speed of spaceship
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound = mixer.Sound(r"C:\Users\Lenovo\Desktop\New folder\python\laser.wav")
                    bullet_sound.play()
                    #Get the current X coordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    #Boundary of Spaceship
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736


    for i in range(n_enemies):

        #Game Over
        if enemyY[i] > 400:
            for j in range(n_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

    #Enemy Movement
        enemyX[i] += enemyX_change[i]

        if enemyX[i] <= 0:
            enemyX_change[i] = 5
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -5
            enemyY[i] += enemyY_change[i]

        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            collision_sound = mixer.Sound(r"C:\Users\Lenovo\Desktop\New folder\python\Small Projects\Game Development and Graphics\Covid 19\explosion.wav")
            collision_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    #Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)                            #Load image on screen
    showscore(textX, textY)
    pygame.display.update()
