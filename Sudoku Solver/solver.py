def print_board(bo):
    for i in range(len(bo)):
        if i%3==0 and i!=0:
            print("- - - - - - - - - - - - -")        # Print this after every 3 rows

        for j in range(len(bo[0])):                  # Length of rows
            if j%3==0 and j!=0:
                print(" | ", end="")

            if j==8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if(bo[i][j]==0):
                return (i, j)           # Return position of the empty place

    return None                     # Return None if no empty squares found

def valid(bo, num, pos):
    # Check Row(horizontally)
    for i in range(len(bo[0])):             # iterate through each column in the row
        if(bo[pos[0]][i] == num and pos[1]!=i):                # pos = (row, column) => pos[0] = row index
            return False                                # pos[1]!=i => not checking the position we just inserted 'num' into

    # Check Column(Vertically)
    for i in range(len(bo)):
        if(bo[i][pos[1]] == num and pos[1]!=i):
            return False

    # Check which box we are in(1 of nine boxes(big boxes))
    box_x = pos[1]//3                   # Gives values 0, 1 or 2
    box_y = pos[0]//3

    # loop through all 9 elements in a box(big)
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3+3):
            if(bo[i][j]==num and (i, j)!=pos):         # Check if any other element in box is equal to one we just added making
                return False                           # sure not to check same position we added in
    return True

# Function for Backtrack - Recursive Function
# If we reach the end of the board => Solution found
def solve(bo):
    # print(bo)
    find = find_empty(bo)
    if not find:
        return True             # We have found the solution
    else:
        row, col = find

    for i in range(1, 10):          # Loop through the values 1-9
        if valid(bo, i, (row, col)):          # Check if we will get a valid solution by adding them to the board
            bo[row][col] = i            # If valid => we will add the number to the board

            if solve(bo):               # Recursively try to finish the solution by calling solve() on new board with
                return True             # new value added
            bo[row][col] = 0        # if solve() is not True, we will backtrack, reset the last element we added back to 0,
                                    # try diff value and repeat process recursively

    return False                    # if we loop through all of the numbers and none of them are valid, we return False
