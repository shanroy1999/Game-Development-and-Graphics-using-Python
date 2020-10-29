import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

# Cubes that build up the snake
# List of cubes => build up the snake body
class cube(object):
    rows = 20
    w = 500
    def __init__(self, start, dirx=1, diry=0, color=(255, 0, 0)):
        self.pos = start
        self.dirx = 1                               # Initially start moving in the x-direction automatically
        self.diry = 0
        self.color = color

    def move(self, dirx, diry):
        self.dirx = dirx
        self.diry = diry
        self.pos = (self.pos[0] + self.dirx, self.pos[1] + self.diry)


    def draw(self, surface, eyes=False):
        blockSize = self.w // self.rows
        i = self.pos[0]                         # row
        j = self.pos[1]                         # column

        # Draw the cube => should not overlap with the grid lines => +1, -2 => white lines of grids should be visible
        pygame.draw.rect(surface, self.color, (i*blockSize+1, j*blockSize+1, blockSize-2, blockSize-2))

        # Draw the eyes of head
        if eyes:
            centre = blockSize//2
            radius = 3
            circleMiddle = (i*blockSize + centre - radius, j*blockSize+8)
            circleMiddle2 = (i*blockSize + blockSize - radius*2, j*blockSize+8)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle, radius)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle2, radius)


# The main snake object
class snake(object):
    body = []                                               # Ordered List of cubes that builds the snake body
    turns = {}
    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)                               # Head of the snake => a cube at the given the position(starting position)
        self.body.append(self.head)                         # Append the head in the body
        self.dirx = 0                                       # Direction for x (either of -1, 1, 0)
        self.diry = 1                                       # Direction for y (either of -1, 1, 0)

        # If direction in y is 1 or -1 => direction in x will be 0 and
        # if direction in x is 1 or -1 => direction in y will be 0
        # Move in only one direction at a time

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()                 # Dictionary which has all the key values
            for key in keys:
                if keys[pygame.K_LEFT]:                     # make x -ve to move more towards zero
                    self.dirx = -1
                    self.diry = 0
                    self.turns[self.head.pos[:]] = [self.dirx, self.diry]

                    # turns => dictionary => add a key denoting the current position of the head of snake
                    # value => what direction we turned

                elif keys[pygame.K_RIGHT]:
                    self.dirx = 1
                    self.diry = 0
                    self.turns[self.head.pos[:]] = [self.dirx, self.diry]

                elif keys[pygame.K_UP]:
                    self.dirx = 0
                    self.diry = -1
                    self.turns[self.head.pos[:]] = [self.dirx, self.diry]

                elif keys[pygame.K_DOWN]:
                    self.dirx = 0
                    self.diry = 1
                    self.turns[self.head.pos[:]] = [self.dirx, self.diry]

        # Look through the list of positions
        # self.body => made up of cube objects
        # i => index, c => cube object
        # all cube objects => have position
        for i, c in enumerate(self.body):

            # for each cube object => grab the position
            p = c.pos[:]                    # [:] => Make a copy => do that not changing the position of the snake

            # check if the position in turn list
            if p in self.turns:
                turn = self.turns[p]        # Grab the direction value(x, y) at that position index
                c.move(turn[0], turn[1])    # Give the cube the x and y direction and move it
                if i == len(self.body)-1:   # When we are on the last cube => remove the turn
                    self.turns.pop(p)       # If we don't remove that turn from the list => it will automatically change dir on that position

            # If position not in the turns list => snake will still be moving
            else:
                # Check whether we reached the edge of the screen
                if c.dirx == -1 and c.pos[0] <= 0:                          # Moving left and x position of cube<=0(left edge of screen)
                    c.pos = (c.rows-1, c.pos[1])                            # Change position for snake to move to right side of screen
                elif c.dirx == 1 and c.pos[0] >= c.rows-1:                  # Moving right and x position of cube>=rows-1(right edge of screen)
                    c.pos = (0, c.pos[1])                                   # Change position for snake to move to left side of screen
                elif c.diry == 1 and c.pos[1] >= c.rows-1:                  # Moving down and y position of cube>=rows-1(down edge of screen)
                    c.pos = (c.pos[0], 0)                                   # Change position for snake to move to upper side
                elif c.diry == -1 and c.pos[1] <= 0:                        # Moving up and y position of cube<=rows-1(upper edge of screen)
                    c.pos = (c.pos[0], c.rows-1)                            # Change position for snake to move to down side
                else:
                    c.move(c.dirx, c.diry)                                  # Not at any edge of screen => continue moving in same dir

    # Reset the snake on collision
    def reset(self, pos):
        self.head = cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirx = 0
        self.diry = 1

    def addCube(self):
        # figure out where the tail of the snake is
        tail = self.body[-1]
        dx, dy = tail.dirx, tail.diry

        if dx == 1 and dy==0:                                               # Add cube to left when moving towards right
            self.body.append(cube((tail.pos[0]-1, tail.pos[1])))
        elif dx == -1 and dy == 0:                                          # Add cube to right when moving towards left
            self.body.append(cube((tail.pos[0]+1, tail.pos[1])))
        elif dx == 0 and dy == 1:                                           # Add cube to up when moving towards down
            self.body.append(cube((tail.pos[0], tail.pos[1]-1)))
        elif dx == 0 and dy == -1:                                          # Add cube to down when moving towards up
            self.body.append(cube((tail.pos[0], tail.pos[1]+1)))

        # New cube at the end of the snake => will move in the direction of the tail
        self.body[-1].dirx = dx
        self.body[-1].diry = dy

    def draw(self, surface):
        for i,c in enumerate(self.body):
            if i==0:
                c.draw(surface, True)                       # True => draw the eyes to distinguish head of the snake
            else:
                c.draw(surface)

# Draw grid of width 'w' and no of rows = rows on the window "surface"
def drawGrid(w, rows, surface):
    blockSize = w // rows                                   # Gap between each line of the grid
    x = 0
    y = 0
    for l in range(rows):
        x+=blockSize
        y+=blockSize

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))            # Draw white vetical lines at equal distances
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))            # Draw white horizontal lines at equal distances

def redrawWindow(surface):
    global rows, width, s, snack
    surface.fill((0, 0, 0))                                 # Fill the screen with black color
    s.draw(surface)
    snack.draw(surface)
    drawGrid(width, rows, surface)                          # Draw grid on the window
    pygame.display.update()                                 # Keep updating the display

def randomSnack(rows, item):
    positions = item.body                                   # item => snake object, positions => list of positions
    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)

        # check length of list of a filtered list and see if any of positions is same as current position of the snake head
        # Do not put snack on the top of the snake
        if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:
            continue
        else:
            break

    return (x,y)

# Show the message box on completion of game
def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass

# Main game loop
def main():
    global width, rows, height, s, snack
    width = 500
    height = 500
    rows = 20                                               # Number of rows => divide width evenly
    win = pygame.display.set_mode((width, height))          # Set the window
    s = snake((255, 0, 0), (10, 10))                        # Snake object => color -> red and position => (10, 20)
    snack = cube(randomSnack(rows, s), color=(0, 255, 0))
    run = True
    clock = pygame.time.Clock()

    while run:
        pygame.time.delay(50)                           # Delay 50 miliseconds, lesser delay => faster game
        clock.tick(FPS)                                 # Snake => run 60 blocks in 1 second, higher FPS => faster game
        s.move()                                        # Check whether a key is pressed every time we run the loop and move accordingly

        # Check if head of the snake has hit the snack
        if s.body[0].pos == snack.pos:
            s.addCube()                                 # add a cube to the snake and increase its length
            snack = cube(randomSnack(rows, s), color=(0, 255, 0))           # Generate another snack at some other position

        # Check for collision of the snake
        for x in range(len(s.body)):
            # Loop through every cube in the snake body and check if the position is in the list of all the positions of cubes after it
            if s.body[x].pos in list(map(lambda z:z.pos, s.body[x+1:])):
                print("Score: ", len(s.body))
                message_box("You Lost!", "Play Again...")
                s.reset((10, 10))                       # Reset the position of the snake to starting position and length=1 and break the loop
                break

        redrawWindow(win)



FPS = 60

main()
