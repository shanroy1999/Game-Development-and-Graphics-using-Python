# A* => informed search algorithm => We dont just apply brute force and find every single path
# Heuristic function => help find optimal path
# Only consider optimal paths => highest priority
# Open Set => like a priority queue => keep track of the nodes which we want to consider next
# Start by putting start node in the open set along with distance to that node(F-score) => (Start node, distance)
# H-score => H(n) => gives absolute distance between node 'n' and the end node => just guess the score
# G-score => G(n) => gives the current shortest distance to from start node to the node 'n'

# F-score = G-score + H-score => F(n) = G(n) + H(n)

# At start node => G-score = 0, H-score=0, F-score = 0
# At rest of the nodes => G-score = infinity, H-score = infinity, F-score = infinity => initially
# Look at the neighbors of the starting node => compare the distance between start node and neighbor node with the g-score of neighbor node
# ---------- -----------------
# |        ||                 |
# A ------ C ------- B ------ D
# Start Node => A, End node => D
# distances AC => 1 and 2, distance CB => 3, distance CD => 2, distance BD => 1

# OpenSet => Open = {(A, 0)} => Always start by putting start node in the open set
#                            => F score for A(start node) => 0 (distance between start node(A) and node A = 0)

# Initially :-
# Node  |  F-score  | G-score  | H-score  | Last
# -------------------------------------------------
#  A    |     0     |    0     |    0     |  -      => no last node as node 'A' is the starting node
#  B    | infinity  | infinity | infinity |
#  C    | infinity  | infinity | infinity |
#  D    | infinity  | infinity | infinity |

# Neighbors of node A => Only node C => 2 edges => edge 1' => distance 1 and edge 2' => distance 2
# compare edge 1' with the G-score of node C => check if this current distance is shorter than the current G-score of node C
# edge 1' => distance = 1 < infinity(=G-score of node C) => update G-score of node C => 1

# Node  |  F-score  | G-score  | H-score  | Last
# -------------------------------------------------
#  A    |     0     |    0     |    0     |  -
#  B    | infinity  | infinity | infinity |
#  C    | infinity  |    1     | infinity |
#  D    | infinity  | infinity | infinity |

# Best path to go from node A to node C => taking edge 1' of distance 1
# Now we update the H-score of node C => guess the H-score as 1 and update it => F-score for node C = G-score + H-score = 1 + 1 = 2

# Node  |  F-score  | G-score  | H-score  | Last
# -------------------------------------------------
#  A    |     0     |    0     |    0     |
#  B    | infinity  | infinity | infinity |
#  C    |     2     |    1     |    1     |  A      => (Last = A) as we came to node C from A => what node we came from to obtain these scores
#  D    | infinity  | infinity | infinity |

# Take node A out of the open set => done with it => Open Set => {}
# Add node C into the open set(as it was the only neighbor of node A) and its F-score => Open Set => {(C, 2)}

# Look at the neighbors of node C => node B and node D
# Considering node B => G-score = 1(distance AC) + 3(distance CB) = 4 => G-score for C to B = 4
# Compare the distance '4' with G-score of node B => 4 < infinity => update the G-score of B
# H-score from node B to node D => guess = 2
# F-score for node B => G-score + H-score = 4+2 = 6

# Node  |  F-score  | G-score  | H-score  | Last
# -------------------------------------------------
#  A    |     0     |    0     |    0     |  -
#  B    |     6     |    4     |    2     |  C
#  C    |     2     |    1     |    1     |  A
#  D    | infinity  | infinity | infinity |

# Take node C out of the openset => done with it => Open Set = {}
# Add node B into the open set(as it was a neighbor of node C) and its F-score => Open Set => {(B, 6)}

# Look at the other neighbor of node C => node D(end node)
# Considering node D => G-score = 1(distance AC) + 2(distance CD) = 3 => G-score for C to D = 3
# Compare the distance '3' with G-score of node D => 3 < infinity => update the G-score of D = 3
# H-score from node D to node D => guess = 0
# F-score for node B => G-score + H-score = 3+0 = 3

# Node  |  F-score  | G-score  | H-score  | Last
# -------------------------------------------------
#  A    |     0     |    0     |    0     |  -
#  B    |     6     |    4     |    2     |  C
#  C    |     2     |    1     |    1     |  A
#  D    |     3     |    3     |    0     |  C

# Open set => {(B, 6), (D, 3)}
# Select the node in the open set which has the shortest F-score => (3, D) => pop out of the open set
# Open set => {(B, 6)} => took the end node out of the open set => Algorithm Completed

# Shortest Path => [A -> C -> D] (looking at the 'last' column of the table)
# For node D => last = node C and for node C => last = node A => path -> (A -> C -> D)

import pygame
import math
from queue import PriorityQueue

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Path Finding Algorithm")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

# Main visualization tool
class Spot:
    # Spot => keep track of different values => (row, column) position, width of itself(the cubes), neighbors, colors
    # Create a huge grid => (50, 50)
    # In the grid => we will have a bunch of cubes/spots
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row*width
        self.y = col*width
        self.color = WHITE # initially => all cubes -> white color
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    # Get positions of the cubes
    def get_pos(self):
        return self.row, self.col

    # if color = RED => we have already looked at it
    # if color = WHITE => have not looked at it/visited it
    # if color = BLACK => its a barrier
    # if color = ORANGE => start node
    # if color = PURPLE => end node

    # Check if we have already considered / looked at it
    def is_closed(self):
        return self.color == RED

    # Check if the cube is in the open set
    def is_open(self):
        return self.color == GREEN

    # Check if the cube is a barrier
    def is_barrier(self):
        return self.color == BLACK

    # Check if the cube is a start node
    def is_start(self):
        return self.color == ORANGE

    # Check if the cube is an end node
    def is_end(self):
        return self.color == TURQUOISE

    # Reset the cubes => change the color to white
    def reset(self):
        self.color = WHITE

    # Make the cube red if we have already visited
    def make_closed(self):
        self.color = RED

    # Make the cube green if we have added the cube in the open set
    def make_open(self):
        self.color = GREEN

    # Make the cube black if its a barrier
    def make_barrier(self):
        self.color = BLACK

    # Make the cube orange if its an end node
    def make_start(self):
        self.color = ORANGE

    # Make the cube turquoise if its an end node
    def make_end(self):
        self.color = TURQUOISE

    # Make the cube purple if its a path
    def make_path(self):
        self.color = PURPLE

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    # Check around the spot and check if the neighbors are barriers or not
    # If not barriers => add them to the neighbors list
    def update_neighbors(self, grid):
        self.neighbors = []
        # check if the row we are currently at is less than (total rows-1) => GOING DOWN THE ROWS
        # if we are at square 49 and go at square 50 which doesn't exist => crash the program
        if self.row < self.total_rows-1 and not grid[self.row+1][self.col].is_barrier():
            self.neighbors.append(grid[self.row+1][self.col])           # Append the next row down

        # GOING UP THE ROWS
        if self.row > 0 and not grid[self.row-1][self.col].is_barrier():
            self.neighbors.append(grid[self.row-1][self.col])

        # GOING TO THE RIGHT
        if self.col < self.total_rows-1 and not grid[self.row][self.col+1].is_barrier():
            self.neighbors.append(grid[self.row][self.col+1])

        # GOING TO THE LEFT
        if self.col > 0 and not grid[self.row][self.col-1].is_barrier():
            self.neighbors.append(grid[self.row][self.col-1])

    # lt => stands for "less than"
    # What happens if we compare some spot to other spot
    def __lt__(self, other):
        return False

# Define the heuristic function for the algorithm => H-score
# p1, p2 => point 1 and point 2 => figure out the distance between point 1 and point 2 and return it
# distance => Manhattan distance(L distance) => The distance between two points measured along axes at right angles.
# if p1 => (x1, y1) and p2 => (x2, y2) => manhattan distance = |x1 - x2| + |y1 - y2|
def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

# Make the grid
# Data structure that can manipulate the spots to make/use/traverse them
# List => hold all of the spots defined in the grid
# width => width of entire grid, rows => no of rows in the grid
def make_grid(rows, width):
    grid = []                           # 2D list => contain the spots in each row
    gap = width//rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)                    # Append spot in row i of the grid

    return grid

# Draw the grid lines to differentiate among the spots
def draw_grid_lines(win, rows, width):
    gap = width//rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i*gap), (width, i*gap))     # Draw the horizontal lines for each of the rows
        for j in range(rows):
            pygame.draw.line(win, GREY, (j*gap, 0), (j*gap, width))     # Draw the vertical lines for each of the rows

# Main draw function which draws everything
def draw(win, grid, rows, width):
    win.fill(WHITE)
    for row in grid:
        for spot in row:
            spot.draw(win)

    # Draw grid lines on the top
    draw_grid_lines(win, rows, width)
    pygame.display.update()

# Draw the line showing the shortest path
def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()

# Take mouse position and figure out what cube/spot we are on
# Translate the mouse position to a (row, col) position
def get_click_position(pos, rows, width):
    gap = width//rows
    y, x = pos
    row = y//gap
    col = x//gap
    return row, col

# Function for implementing the algorithm
def algorithm(draw, grid, start, end):
    count = 0

    # Priority Queue => helps getting the smallest element out of the queue everytime
    open_set = PriorityQueue()      # Store in order => (f-score, count, node)

    # Add the start node with its F-score(=0) in the open set
    # count => keep track of when we inserted the items into the queue
    # if we have two things inside the queue with the same F-score => consider the one which was inserted first
    open_set.put((0, count, start))

    # "Last" column of the table
    # What nodes came from where
    came_from = {}

    # Dictionary to store all of the g-scores => initialized to infinity
    # Current shortest distance to get from start node to this node
    g_score = {spot : float('inf') for row in grid for spot in row}

    # g-score of start node = 0
    g_score[start] = 0

    # f_score => keeps track of predicted distance from this node to the end node
    # f-score = g_score + h_score
    f_score = {spot : float('inf') for row in grid for spot in row}

    # f-score of start node = heuristic
    f_score[start] = h(start.get_pos(), end.get_pos())

    # Open set hash => keep track of all the items in the priority queue and the items not in the priority queue
    # We Can remove an item from the priority queue but can't check whether something is in the priority queue
    # Open set hash => can check whether something is in the priority queue or not
    open_set_hash = {start}

    while not open_set.empty():
    # If open set is empty => we have considered every single possible node and still if we have not found the path => path doesn't exist
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]     # Take the node in the open set associated with the minimum f-score
        open_set_hash.remove(current)   # prevent any duplication

        # If the node that we popped out is the end node => we found the shortest path => reconstruct the path and draw it
        if current==end:
            reconstruct_path(came_from, end, draw)
            end.make_end()              # will draw purple on top of the end node if we dont do this
            start.make_start()
            return True

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1

            # If we found a better way to reach the neighbor => update the score
            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
                if neighbor not in open_set_hash:
                    count+=1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)

                    # Know that we already considered the neighbor and have put it in the open set
                    neighbor.make_open()

        draw()

        # If the node that we just looked at is not the start node => make it RED and close it off
        # as we have already considered it and it will not be added back in the open set
        if current != start:
            current.make_closed()

    # if we did not find the path
    return False

# Main function
def main(win, width):
    ROWS = 50

    # Generate the grid and give the 2D list of spots
    grid = make_grid(ROWS, width)

    # Start position and the end position
    start = None
    end = None

    run = True                      # Keep track of start of game loop
    started = False                 # Keep track of start of the actual algorithm

    while run:
        draw(win, grid, ROWS, width)        # Draw the grid in every loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # Check which mouse button was pressed
            # Left Mouse button
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()            # Get (x,y) coordinate position of the mouse

                # Get (row, col) position of the spot in the 2D grid we clicked on
                # Translate the mouse position (x, y) into (row, col) position
                row, col = get_click_position(pos, ROWS, width)
                spot = grid[row][col]

                # If we have not yet placed/decided the start position => make them whenever we press next
                if not start and spot!=end:
                    start = spot
                    start.make_start()

                # If we have not yet placed/decided the end position => make them whenever we press next
                elif not end and spot!=start:
                    end = spot
                    end.make_end()

                # If we have already defined start and end positions
                elif spot != end and spot != start:
                    spot.make_barrier()

            # Right mouse button
            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = get_click_position(pos, ROWS, width)
                spot = grid[row][col]

                # Reset the spot color to WHITE
                spot.reset()

                # Reset the start and end positions and change their color to WHITE on right click
                if spot == start:
                    start = None
                elif spot == end:
                    end = None

            # If we pressed a key of the keyboard
            if event.type == pygame.KEYDOWN:
                # if the key pressed is a space bar and the algorithm has not started
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors(grid)             # Update the neighbors

                    # Call the algorithm
                    algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)

                # Clear the screen and start again
                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)

    pygame.quit()

main(WIN, WIDTH)
