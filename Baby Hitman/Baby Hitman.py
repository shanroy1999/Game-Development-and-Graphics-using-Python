import pygame
import os
pygame.init()

win = pygame.display.set_mode((500, 480))
pygame.display.set_caption("Game")

screenwidth = 500
score=0

path = r"C:\Users\Lenovo\Desktop\New folder\python\Small Projects\Game Development and Graphics\Baby Hitman"
walkRight = [pygame.image.load(os.path.join(path, 'R1.png')),
            pygame.image.load(os.path.join(path, 'R2.png')),
            pygame.image.load(os.path.join(path, 'R3.png')),
            pygame.image.load(os.path.join(path, 'R4.png')),
            pygame.image.load(os.path.join(path, 'R5.png')),
            pygame.image.load(os.path.join(path, 'R6.png')),
            pygame.image.load(os.path.join(path, 'R7.png')),
            pygame.image.load(os.path.join(path, 'R8.png')),
            pygame.image.load(os.path.join(path, 'R9.png'))]


walkLeft = [pygame.image.load(os.path.join(path, 'L1.png')),
            pygame.image.load(os.path.join(path, 'L2.png')),
            pygame.image.load(os.path.join(path, 'L3.png')),
            pygame.image.load(os.path.join(path, 'L4.png')),
            pygame.image.load(os.path.join(path, 'L5.png')),
            pygame.image.load(os.path.join(path, 'L6.png')),
            pygame.image.load(os.path.join(path, 'L7.png')),
            pygame.image.load(os.path.join(path, 'L8.png')),
            pygame.image.load(os.path.join(path, 'L9.png'))]


bg = pygame.image.load(os.path.join(path, "bg.jpg"))
char = pygame.image.load(os.path.join(path, "standing.png"))
clock = pygame.time.Clock()
#bulletSound = pygame.mixer.Sound(os.path.join(path, 'bullet.mp3'))
#hitSound  = pygame.mixer.Sound(os.path.join(path, 'hit.mp3'))
music = pygame.mixer.music.load(os.path.join(path, 'music.mp3'))
pygame.mixer.music.play(-1)

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.walkCount = 0
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.isJump = False
        self.standing = True
        self.hitbox = (self.x+17, self.y+11, 29, 52)

    def draw(self, win):
        if self.walkCount + 1 >= 54:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//6], (self.x,self.y))
                self.walkCount += 1

            elif self.right:
                win.blit(walkRight[self.walkCount//6], (self.x,self.y))
                self.walkCount += 1

        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x+17, self.y+11, 29, 52)
        #pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

    def hit(self):
        self.isJump = False
        self.jumpCount = 10
        self.x = 60
        self.y = 410
        self.walkCount = 0
        font_1 = pygame.font.SysFont("comicsans",60)
        text = font_1.render("-5", 1, (255,0,0))
        win.blit(text, (250 - (text.get_width()/2), 240))
        pygame.display.update()
        i = 0
        while i<20:
            pygame.time.delay(10)
            i+=1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()

class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8*facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)

class Enemy(object):
    walkRight = [pygame.image.load(os.path.join(path, 'R1E.png')),
            pygame.image.load(os.path.join(path, 'R2E.png')),
            pygame.image.load(os.path.join(path, 'R3E.png')),
            pygame.image.load(os.path.join(path, 'R4E.png')),
            pygame.image.load(os.path.join(path, 'R5E.png')),
            pygame.image.load(os.path.join(path, 'R6E.png')),
            pygame.image.load(os.path.join(path, 'R7E.png')),
            pygame.image.load(os.path.join(path, 'R8E.png')),
            pygame.image.load(os.path.join(path, 'R9E.png')),
            pygame.image.load(os.path.join(path, 'R10E.png')),
            pygame.image.load(os.path.join(path, 'R11E.png'))]

    walkLeft = [pygame.image.load(os.path.join(path, 'L1E.png')),
            pygame.image.load(os.path.join(path, 'L2E.png')),
            pygame.image.load(os.path.join(path, 'L3E.png')),
            pygame.image.load(os.path.join(path, 'L4E.png')),
            pygame.image.load(os.path.join(path, 'L5E.png')),
            pygame.image.load(os.path.join(path, 'L6E.png')),
            pygame.image.load(os.path.join(path, 'L7E.png')),
            pygame.image.load(os.path.join(path, 'L8E.png')),
            pygame.image.load(os.path.join(path, 'L9E.png')),
            pygame.image.load(os.path.join(path, 'L10E.png')),
            pygame.image.load(os.path.join(path, 'L11E.png'))]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 6
        self.hitbox = (self.x+17, self.y+2, 31 ,57)
        self.health = 9
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 66:
                self.walkCount = 0

            if self.vel>0:
                win.blit(self.walkRight[self.walkCount//6], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount//6], (self.x, self.y))
                self.walkCount += 1

            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1]-20, 50, 10))
            pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1]-20, 50-(4.75*(9 - self.health)), 10))
            self.hitbox = (self.x+17, self.y+2, 31 ,57)
        #pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel *= -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel *= -1
                self.walkCount = 0

    def hit(self):
        if self.health>0:
            self.health -= 1
        else:
            self.visible = False
        print("HIT")


def redrawGameWindow():
    global walkCount
    win.blit(bg, (0,0))
    text = font.render("Score :"+str(score), 1, (255,0,0))
    win.blit(text, (350,10))
    man.draw(win)
    enemy.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()

font = pygame.font.SysFont("comicsans", 30, True)

man = player(300, 410, 64, 64)
enemy = Enemy(0, 410, 64, 64, 450)
bullets = []
shoot = 0

run = True
while run:
    clock.tick(54)

    if enemy.visible == True:
        if man.hitbox[1] < enemy.hitbox[1] + enemy.hitbox[3] and man.hitbox[1]+man.hitbox[3] > enemy.hitbox[1]:
            if man.hitbox[0] + man.hitbox[2] > enemy.hitbox[0] and man.hitbox[0] < enemy.hitbox[0]+enemy.hitbox[2]:
                man.hit()
                score -= 5
    else:
        text = font.render(f"Your Final score is {score}", 1, (255,0,0))
        win.blit(text, (100, 240))
        pygame.display.update()

    if shoot > 0:
        shoot += 1
    if shoot > 3:
        shoot = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.y - bullet.radius < enemy.hitbox[1] + enemy.hitbox[3] and bullet.y+bullet.radius > enemy.hitbox[1]:
            if bullet.x + bullet.radius > enemy.hitbox[0] and bullet.x - bullet.radius < enemy.hitbox[0]+enemy.hitbox[2]:
                #hitSound.play()
                enemy.hit()
                score += 1
                bullets.pop(bullets.index(bullet))

        if bullet.x<500 and bullet.x>0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    KEYS = pygame.key.get_pressed()

    if KEYS[pygame.K_SPACE] and shoot == 0:
        #bulletSound.play()
        if man.left:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 5:
            bullets.append(projectile(round(man.x + man.width//2), round(man.y + man.height//2), 6,(255,255,0), facing))

        shoot = 1

    if KEYS[pygame.K_LEFT] and man.x>man.vel:
        man.x-=man.vel
        man.left = True
        man.right = False
        man.standing = False

    elif KEYS[pygame.K_RIGHT] and man.x<500-man.width-man.vel:
        man.x+=man.vel
        man.right = True
        man.left = False
        man.standing = False

    else:
        man.standing = True
        man.walkCount = 0

    if not(man.isJump):
        if KEYS[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount>=-10:
            neg = 1
            if man.jumpCount<0:
                neg = -1
            man.y -= (man.jumpCount**2)*0.5*neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    redrawGameWindow()

pygame.quit()
