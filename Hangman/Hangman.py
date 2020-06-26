import pygame
import math
import os
import random

# Set display
pygame.init()
WIDTH, HEIGHT = 1000, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")

# Image Directory
loc = r"C:\Users\Lenovo\Desktop\New folder\python\Small Projects\Game Development and Graphics\Hangman\images"

# load images
images = []
for i in range(7):
    image = pygame.image.load(os.path.join(loc, "hangman"+str(i)+".png"))       # Load images from the directory
    images.append(image)

print(images)           # gives us Surface(width x height x depth)
# Surface => collection of pixels that one wants to put on the pygame window

hangman_status = 0              # Tells which image(out of the 6) is to be drawn when

# List of Words to select randomly to be guessed by user
words = ["PREVARICATE", "PALATIAL", "INSINUATE", "BELABOR", "APPROBATION", "ENTICE", "EUPHORIA", "FIDELITY", "GALLANT", "INTRANSIGENCE"
"PERNICIOUS", "PERISH", "PUNGENT", "REMONSTRATE"]

word = random.choice(words)              # Randomly select word from the word list
guessed = []                    # Stores the letters guessed by user so far

FPS = 60     # Frame Per Second
clock = pygame.time.Clock()         # Make sure the gameloop runs at FPS=60
# clock object => count at 60 frames per second and keep track of time

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# font
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)

# for Buttons
RADIUS = 20
GAP = 15
letters = []                                    # Store the (x, y) coordinates of letter, cooresponding alphabets and a boolean value
startx = round((WIDTH - (RADIUS*2 + GAP)*13)/2)         # RADIUS * 2 + GAP => distance between each new button
starty = 400

A = 65              # ASCII code for letter 'A'

# Determine x and y positions of the letters
for i in range(26):                                         # i => tells us what button we are on
    x = startx + GAP*2 + ((RADIUS*2 + GAP) * (i % 13))      # 13 letters in each row, GAP*2 => gaps of first and last button on L,R sides
    y = starty + ((i//13)*(RADIUS*2 + GAP))
    letters.append([x, y, chr(A + i), True])                # List of all button coordinates and letters stored by each button
                                                            # stores the boolean value 'True' => tells whther button visible or invisible

def draw():
    win.fill(WHITE)                                         # Fill white color in the pygame window

    # draw the game title
    text = TITLE_FONT.render("HANGMAN", 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, 20))

    # draw word to be guessed
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (400, 200))

    for letter in letters:
        x, y, ltr, visible = letter        # Unpacking each (x, y) coordinates and letter character, visibility stored in the list 'letters'
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)   # Draw a Black Circle on the widow with radius = RADIUS, thickness = 3, centre=(x, y)
            text = LETTER_FONT.render(ltr, 1, BLACK)            # render() => Draw text on the Surface, antialiasing = 1
            win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

    win.blit(images[hangman_status], (150,100))             # blit(img, (x, y)) => draw image on the window at position(x, y)
    pygame.display.update()

def show_message(message):
    win.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)                 # Dont do anything for 3s(3000 ms)

run = True
while run:
    clock.tick(FPS)            # Make sure that the while loop runs at that speed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()               # x, y coordinates of the mouse
            for letter in letters:
                x, y, ltr, visible = letter
                if visible:
                    dist = math.sqrt((x-m_x)**2 + (y-m_y)**2)
                    if dist < RADIUS:
                        letter[3] = False                   # Make the letter invisible if clicked once
                        guessed.append(ltr)

                        if ltr not in word:
                            hangman_status += 1

    draw()

    # Check if the user won
    won = True
    for letter in word:
        if letter not in guessed:
            won = False

    if won:
        show_message("Congratualtions! YOU WON!")
        break

    if(hangman_status==6):
        show_message("Sorry! YOU LOST!")

pygame.quit()
