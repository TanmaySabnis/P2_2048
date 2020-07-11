# First step is to start the game with creating a 4x4 matrix and initialising
# all cells to be 0.
import random

def start_game():
    mat = []
    for i in range(4):
        mat.append([0]*4)
    return mat

# Our matrix 'mat' is thus created
# Next logic is to add 2's randomly

def add_new_2(mat):
    
    # The logic is to add a new 2 add every empty cell also with a random
    # position
    # The range of adding a new 2 is (0,3) for rows and (0,3) for columns
    # After selecting a random cell ex: (1,2), check if its empty
    # if yes, then add 2
    # The random cell is decidded by using the 'Random' library in python
    
    r = random.randint(0,3) # Selecting random cell for row
    c = random.randint(0,3) # Selecting random cell for columns
    while(mat[r][c]!=0):
        r = random.randint(0,3)
        c = random.randint(0,3)
    mat[r][c] = 2

# Initialising the reverse matrix function
def reverse(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[i][3-j])
    
    return new_mat

# Initialising the transpose function
def transpose(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        
        for j in range(4):
            new_mat[i].append(mat[j][i])
    
    return new_mat
    
    
# Initialising the merge Function
def merge(mat):
    changed = False
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j+1] and mat[i][j]!=0:
                mat[i][j] = mat[i][j]*2
                mat[i][j+1] = 0
                changed = True
    return mat,changed

                
# Initialising the Compression function which takes care of the 0's in between.
# fill in th enon-zero element
def compress(mat):
    changed = False
    new_mat = []
    for i in range(4):
        new_mat.append([0]*4)
        
    for i in range(4):
        pos = 0
        for j in range(4):
            if mat[i][j]!=0:
                new_mat[i][pos] = mat[i][j]
                if j!= pos:
                    changed = True
                pos += 1
                
    return new_mat,changed
        
# Code for all moves

def move_up(grid):
    transposed_grid = transpose(grid)
    new_grid,changed1 = compress(transposed_grid)
    new_grid,changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid,temp = compress(new_grid)
    final_grid = transpose(new_grid)
    
    return final_grid,changed

def move_down(grid):
    transposed_grid = transpose(grid)
    reversed_grid = reverse(transposed_grid)
    new_grid,changed1 = compress(reversed_grid)
    new_grid,changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid,temp = compress(new_grid)
    reversed_grid = reverse(new_grid)
    final_grid = transpose(reversed_grid)
    
    return final_grid,changed
    

def move_right(grid):
    reversed_grid = reverse(grid)
    new_grid,changed1 = compress(reversed_grid)
    new_grid,changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid,temp = compress(new_grid)
    final_grid = reverse(new_grid)
    
    return final_grid,changed

def move_left(grid):
    new_grid,changed1 = compress(grid)
    new_grid,changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid,temp = compress(new_grid)
    
    return new_grid,changed
    
# To check current state of game
def get_current_state(mat):
    # Anywhere 2048 is present
    for i in range(4):
        for j in range(4):
            if (mat[i][j] == 2048): #Win condition
                return "Congratulations, you won the game."
            
    # Anywhere 0 is present
    for i in range(4):
        for j in range(4):
            if (mat[i][j] == 0): # Not over yet condition
                return 'Game not over'
    
    # Every Row and Column except last row and last column
    for i in range(3):
        for j in range(3): # Range is 3 here because we are checking for (i+1) and (j+1)
            if(mat[i][j] == mat[i+1][j] or mat[i][j] == mat[i][j+1]):
                return 'Game not over'
            
    # for last row        
    for j in range(3):
        if mat[3][j] == mat[3][j+1]:
            return 'Game not over'
        
    # Last Column
    for i in range(3):
        if mat[i][3] == mat[i+1][3]:
            return 'Game not over'
    
    # If all the above conditions fail, it means we lost.
    return 'Lost'  