import time

import pygame
from sys import exit
from random import randint

pygame.init()
pygame.font.init()

#Check if a number inputed into a theoretical board is valid
def check_valid(bo, num, location):     #location = [4,2]
    #duplicates in row
    for index, cell in enumerate(bo[location[0]]):
        if cell == num and index != location[1]:
            return False
        else:
            pass

    #duplicates in col
    col_array = []
    for row in bo:
        col_array.append(row[location[1]])

    for index, cell in enumerate(col_array):
        if cell == num and index != location[0]:
            return False
        else:
            pass

    #duplicates in sec
    sec_row = location[0] // 3
    sec_col = location[1] // 3


    for i in range(sec_row * 3, sec_row * 3 + 3):
        for j in range(sec_col * 3, sec_col * 3 +3):
            if bo[i][j] == num and [i,j] != location:
                return False

    return True

#Find a cell that is empty in the theoretical board
def find_empty(bo):  #find the position of the first empty cell of the board
    for row in range(9):
        for col in range(9):
            if bo[row][col] == 0:
                return [row,col]
    return False

#Use a backtracking algo (involving recursion) to create a valid theoretical board given an incomplete board (must be able to be solved)
def sudoku_solver(bo):
    if find_empty(bo) == False:
        return True

    else:
        location = find_empty(bo)
        for i in range(1,10):
            check_valid(bo, i, location)
            if check_valid(bo, i, location):
                bo[location[0]][location[1]] = i
                if sudoku_solver(bo):
                    return True

                else:
                    bo[location[0]][location[1]] = 0

        return False

#Generate random values for a theoretical board while ensuring it can still be solved in order to create a valid theoretical sudoku board using previous functions
def generate_valid_board():
    bo = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
]
    ran1 = randint(1,9)
    ran1_x = randint(0,2)
    ran1_y = randint(0,2)
    bo[ran1_y][ran1_x] = ran1

    ran2 = randint(1, 9)
    ran2_x = randint(3, 5)
    ran2_y = randint(3, 5)
    bo[ran2_y][ran2_x] = ran2

    ran3 = randint(1, 9)
    ran3_x = randint(6, 8)
    ran3_y = randint(6, 8)
    bo[ran3_y][ran3_x] = ran3

    sudoku_solver(bo)
    return bo



#KEY VARIABLES
WIDTH = 800
HEIGHT = 800
BOARD_WIDTH = 612
BOARD_HEIGHT = 612
CELL_SIZE = 68
COLS = 9
ROWS = 9
BLACK = (0,0,0)
POINTER_LOC = [0,0]
FONT_SIZE = 24
LOADING_FONT_SIZE = 50
MY_FONT = pygame.font.SysFont('arial',FONT_SIZE)
LOADING_FONT = pygame.font.SysFont('ヒラキノ角コシックw8', LOADING_FONT_SIZE)
GAME_WON = False
SOLVE_PRESSED = False
EASY = False
MEDIUM = False
HARD = False
max_num = 1

#This is used to input values into cells and nums because the pointer_loc variable continuously changes but these values remain fixed
co_ords = [[0,0], [0,1], [0,2], [0,3], [0,4], [0,5], [0,6], [0,7], [0,8],
           [1,0], [1,1], [1,2], [1,3], [1,4], [1,5], [1,6], [1,7], [1,8],
           [2,0], [2,1], [2,2], [2,3], [2,4], [2,5], [2,6], [2,7], [2,8],
           [3,0], [3,1], [3,2], [3,3], [3,4], [3,5], [3,6], [3,7], [3,8],
           [4,0], [4,1], [4,2], [4,3], [4,4], [4,5], [4,6], [4,7], [4,8],
           [5,0], [5,1], [5,2], [5,3], [5,4], [5,5], [5,6], [5,7], [5,8],
           [6,0], [6,1], [6,2], [6,3], [6,4], [6,5], [6,6], [6,7], [6,8],
           [7,0], [7,1], [7,2], [7,3], [7,4], [7,5], [7,6], [7,7], [7,8],
           [8,0], [8,1], [8,2], [8,3], [8,4], [8,5], [8,6], [8,7], [8,8]]


SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sudoku')
clock = pygame.time.Clock()


#Very crucial variable; each element is a list which contains 2 elemtns: a sub-list that contains co-ords of the board and the value within that cell
#Note - the co-ords are in the form Col, Row as opposed to Row, Col
cells_and_nums = [[[0, 0], '0'], [[0, 1], '0'], [[0, 2], '0'], [[0, 3], '0'], [[0, 4], '0'], [[0, 5], '0'], [[0, 6], '0'], [[0, 7], '0'], [[0, 8], '0'], [[1, 0], '0'], [[1, 1], '0'], [[1, 2], '0'], [[1, 3], '0'], [[1, 4], '0'], [[1, 5], '0'], [[1, 6], '0'], [[1, 7], '0'], [[1, 8], '0'], [[2, 0], '0'], [[2, 1], '0'], [[2, 2], '0'], [[2, 3], '0'], [[2, 4], '0'], [[2, 5], '0'], [[2, 6], '0'], [[2, 7], '0'], [[2, 8], '0'], [[3, 0], '0'], [[3, 1], '0'], [[3, 2], '0'], [[3, 3], '0'], [[3, 4], '0'], [[3, 5], '0'], [[3, 6], '0'], [[3, 7], '0'], [[3, 8], '0'], [[4, 0], '0'], [[4, 1], '0'], [[4, 2], '0'], [[4, 3], '0'], [[4, 4], '0'], [[4, 5], '0'], [[4, 6], '0'], [[4, 7], '0'], [[4, 8], '0'], [[5, 0], '0'], [[5, 1], '0'], [[5, 2], '0'], [[5, 3], '0'], [[5, 4], '0'], [[5, 5], '0'], [[5, 6], '0'], [[5, 7], '0'], [[5, 8], '0'], [[6, 0], '0'], [[6, 1], '0'], [[6, 2], '0'], [[6, 3], '0'], [[6, 4], '0'], [[6, 5], '0'], [[6, 6], '0'], [[6, 7], '0'], [[6, 8], '0'], [[7, 0], '0'], [[7, 1], '0'], [[7, 2], '0'], [[7, 3], '0'], [[7, 4], '0'], [[7, 5], '0'], [[7, 6], '0'], [[7, 7], '0'], [[7, 8], '0'], [[8, 0], '0'], [[8, 1], '0'], [[8, 2], '0'], [[8, 3], '0'], [[8, 4], '0'], [[8, 5], '0'], [[8, 6], '0'], [[8, 7], '0'], [[8, 8], '0']]

#This contains the coords of cells that are not empty
filled_cells = []



#This is important - used for the check_solved function that continously runs
game_grid = [
    [0,0,0,0,0,0,0,0,0], #TL
    [0,0,0,0,0,0,0,0,0], #TM
    [0,0,0,0,0,0,0,0,0], #TR
    [0,0,0,0,0,0,0,0,0], #ML
    [0,0,0,0,0,0,0,0,0], #MM
    [0,0,0,0,0,0,0,0,0], #MR
    [0,0,0,0,0,0,0,0,0], #BL
    [0,0,0,0,0,0,0,0,0], #BM
    [0,0,0,0,0,0,0,0,0] #BR
]

solver_grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],  # R1    #GOES BY ROW THEN COLUMN
    [0, 0, 0, 0, 0, 0, 0, 0, 0],  # R2
    [0, 0, 0, 0, 0, 0, 0, 0, 0],  # R3
    [0, 0, 0, 0, 0, 0, 0, 0, 0],  # R4
    [0, 0, 0, 0, 0, 0, 0, 0, 0],  # R5
    [0, 0, 0, 0, 0, 0, 0, 0, 0],  # R6
    [0, 0, 0, 0, 0, 0, 0, 0, 0],  # R7
    [0, 0, 0, 0, 0, 0, 0, 0, 0],  # R8
    [0, 0, 0, 0, 0, 0, 0, 0, 0]   # R9
]

#THIS IS KEY VARIABLE - this will be the solution board for each game
valid_board = generate_valid_board()





#Print the solution board onto the pygame board
def handle_solve_button(valid_board):
    global SOLVE_PRESSED, cells_and_nums
    SOLVE_PRESSED = True
    cells_and_nums = []
    for index, row in enumerate(valid_board):
        for index2, cell in enumerate(row):
            cells_and_nums.append([ [index2, index], str(cell)])





#Draw the solve button onto the screen
def draw_solve_button(mouse_pos):
    global solve_surface_rect
    solve_surface = MY_FONT.render('Solve Board', False, BLACK)
    solve_surface_rect = solve_surface.get_rect(topleft=(20,20))
    SCREEN.blit(solve_surface, solve_surface_rect)

    if solve_surface_rect.collidepoint(mouse_pos):
        solve_surface = MY_FONT.render('Solve Board', False, 'Red')
        solve_surface_rect = solve_surface.get_rect(topleft=(20, 20))
        SCREEN.blit(solve_surface, solve_surface_rect)



def draw_clear_button(mouse_pos):
    global clear_surface_rect
    clear_surface = MY_FONT.render('Clear Board', False, BLACK)
    clear_surface_rect = clear_surface.get_rect(topleft=(300,20))
    SCREEN.blit(clear_surface, clear_surface_rect)

    if clear_surface_rect.collidepoint(mouse_pos):
        clear_surface = MY_FONT.render('Clear Board', False, 'Red')
        clear_surface_rect = clear_surface.get_rect(topleft=(300, 20))
        SCREEN.blit(clear_surface, clear_surface_rect)


#E.g [ [[0, 0], '0'], [[0, 1], '0'], [[0, 2], '0'] ... ]
def handle_clear_button():
    global cells_and_nums, filled_cells
    for cell_num in cells_and_nums:
        if isinstance(cell_num[1], str):
            cell_num[1] = '0'
            filled_cells = []
            for cell_num in cells_and_nums:
                if cell_num[1] not in ['0', 0]:  # Only append the cells into filled cells if cell_num[1] != 0
                    filled_cells.append(cell_num[0])
        else:
            pass


#DRAW THE 9X9 BOARD
def draw_board():
    for i in range(COLS+1):
        if i in [0, 3, 6, 9]:
            pygame.draw.line(SCREEN, BLACK, (94 + (i * CELL_SIZE), 94), (94 + (i * CELL_SIZE), 612 + 94), 5)
        else:
            pygame.draw.line(SCREEN, BLACK, (94 + (i*CELL_SIZE), 94), (94 + (i*CELL_SIZE), 612+94))

    for i in range(ROWS+1):
        if i in [0,3,6,9]:
            pygame.draw.line(SCREEN, BLACK, (94, 94 + (i * CELL_SIZE)), (612 + 94, 94 + (i * CELL_SIZE)), 5)
        else:
            pygame.draw.line(SCREEN, BLACK, (94, 94 + (i*CELL_SIZE)), (612+94, 94 +  (i*CELL_SIZE)))


#DRAW NUMBERS - uses cells and nums ,
def draw_numbers(cells_and_nums):
    for cell_num in cells_and_nums:
        if cell_num[1] in ['1','2','3','4','5','6','7','8','9',1,2,3,4,5,6,7,8,9]:
            text_surf = MY_FONT.render(str(cell_num[1]), False, 'Black')
            text_coords = ((94 + (cell_num[0][0] * CELL_SIZE))+CELL_SIZE/2) , (94 + (cell_num[0][1] * CELL_SIZE) + CELL_SIZE/2)
            text_rect = text_surf.get_rect(center = text_coords)
            SCREEN.blit(text_surf, text_rect)
        else:
            pass


#CONVERT CELLS AND NUMS INTO THE GAME GRID IN ORDER TO CHECK IF THE GAME BOARD HAS BEEN SOLVED OR NOT
def convert_game_grid(cells_and_nums):
    for cell_num in cells_and_nums:

            if cell_num[0][0] == 0:  #IN FIRST COLUMN

                if cell_num[0][1] == 0:
                    if cell_num[1] == 0:
                        game_grid[0][0] = 0
                    else:
                        game_grid[0][0] = cell_num[1]

                if cell_num[0][1] == 1:
                    if cell_num[1] == 0:
                        game_grid[0][3] = 0
                    else:
                        game_grid[0][3] = cell_num[1]


                if cell_num[0][1] == 2:
                    if cell_num[1] == 0:
                        game_grid[0][6] = 0
                    else:
                        game_grid[0][6] = cell_num[1]


                if cell_num[0][1] == 3:
                    if cell_num[1] == 0:
                        game_grid[3][0] = 0
                    else:
                        game_grid[3][0] = cell_num[1]


                if cell_num[0][1] == 4:
                    if cell_num[1] == 0:
                        game_grid[3][3] = 0
                    else:
                        game_grid[3][3] = cell_num[1]


                if cell_num[0][1] == 5:
                    if cell_num[1] == 0:
                        game_grid[3][6] = 0
                    else:
                        game_grid[3][6] = cell_num[1]


                if cell_num[0][1] == 6:
                    if cell_num[1] == 0:
                        game_grid[6][0] = 0
                    else:
                        game_grid[6][0] = cell_num[1]


                if cell_num[0][1] == 7:
                    if cell_num[1] == 0:
                        game_grid[6][3] = 0
                    else:
                        game_grid[6][3] = cell_num[1]


                if cell_num[0][1] == 8:
                    if cell_num[1] == 0:
                        game_grid[6][6] = 0
                    else:
                        game_grid[6][6] = cell_num[1]


            elif cell_num[0][0] == 1: #SECOND COL

                if cell_num[0][1] == 0:
                    if cell_num[1] == 0:
                        game_grid[0][1] = 0
                    else:
                        game_grid[0][1] = cell_num[1]


                if cell_num[0][1] == 1:
                    if cell_num[1] == 0:
                        game_grid[0][4] = 0
                    else:
                        game_grid[0][4] = cell_num[1]


                if cell_num[0][1] == 2:
                    if cell_num[1] == 0:
                        game_grid[0][7] = 0
                    else:
                        game_grid[0][7] = cell_num[1]


                if cell_num[0][1] == 3:
                    if cell_num[1] == 0:
                        game_grid[3][1] = 0
                    else:
                        game_grid[3][1] = cell_num[1]


                if cell_num[0][1] == 4:
                    if cell_num[1] == 0:
                        game_grid[3][4] = 0
                    else:
                        game_grid[3][4] = cell_num[1]


                if cell_num[0][1] == 5:
                    if cell_num[1] == 0:
                        game_grid[3][7] = 0
                    else:
                        game_grid[3][7] = cell_num[1]


                if cell_num[0][1] == 6:
                    if cell_num[1] == 0:
                        game_grid[6][1] = 0
                    else:
                        game_grid[6][1] = cell_num[1]


                if cell_num[0][1] == 7:
                    if cell_num[1] == 0:
                        game_grid[6][4] = 0
                    else:
                        game_grid[6][4] = cell_num[1]


                if cell_num[0][1] == 8:
                    if cell_num[1] == 0:
                        game_grid[6][7] = 0
                    else:
                        game_grid[6][7] = cell_num[1]


            elif cell_num[0][0] == 2: #THIRD COL

                if cell_num[0][1] == 0:
                    if cell_num[1] == 0:
                        game_grid[0][2] = 0
                    else:
                        game_grid[0][2] = cell_num[1]


                if cell_num[0][1] == 1:
                    if cell_num[1] == 0:
                        game_grid[0][5] = 0
                    else:
                        game_grid[0][5] = cell_num[1]

                if cell_num[0][1] == 2:
                    if cell_num[1] == 0:
                        game_grid[0][8] = 0
                    else:
                        game_grid[0][8] = cell_num[1]

                if cell_num[0][1] == 3:
                    if cell_num[1] == 0:
                        game_grid[3][2] = 0
                    else:
                        game_grid[3][2] = cell_num[1]

                if cell_num[0][1] == 4:
                    if cell_num[1] == 0:
                        game_grid[3][5] = 0
                    else:
                        game_grid[3][5] = cell_num[1]

                if cell_num[0][1] == 5:
                    if cell_num[1] == 0:
                        game_grid[3][8] = 0
                    else:
                        game_grid[3][8] = cell_num[1]

                if cell_num[0][1] == 6:
                    if cell_num[1] == 0:
                        game_grid[6][2] = 0
                    else:
                        game_grid[6][2] = cell_num[1]

                if cell_num[0][1] == 7:
                    if cell_num[1] == 0:
                        game_grid[6][5] = 0
                    else:
                        game_grid[6][5] = cell_num[1]

                if cell_num[0][1] == 8:
                    if cell_num[1] == 0:
                        game_grid[6][8] = 0
                    else:
                        game_grid[6][8] = cell_num[1]


            elif cell_num[0][0] == 3: #FOURTH COL

                if cell_num[0][1] == 0:
                    if cell_num[1] == 0:
                        game_grid[1][0] = 0
                    else:
                        game_grid[1][0] = cell_num[1]

                if cell_num[0][1] == 1:
                    if cell_num[1] == 0:
                        game_grid[1][3] = 0
                    else:
                        game_grid[1][3] = cell_num[1]

                if cell_num[0][1] == 2:
                    if cell_num[1] == 0:
                        game_grid[1][6] = 0
                    else:
                        game_grid[1][6] = cell_num[1]

                if cell_num[0][1] == 3:
                    if cell_num[1] == 0:
                        game_grid[4][0] = 0
                    else:
                        game_grid[4][0] = cell_num[1]

                if cell_num[0][1] == 4:
                    if cell_num[1] == 0:
                        game_grid[4][3] = 0
                    else:
                        game_grid[4][3] = cell_num[1]

                if cell_num[0][1] == 5:
                    if cell_num[1] == 0:
                        game_grid[4][6] = 0
                    else:
                        game_grid[4][6] = cell_num[1]

                if cell_num[0][1] == 6:
                    if cell_num[1] == 0:
                        game_grid[7][0] = 0
                    else:
                        game_grid[7][0] = cell_num[1]

                if cell_num[0][1] == 7:
                    if cell_num[1] == 0:
                        game_grid[7][3] = 0
                    else:
                        game_grid[7][3] = cell_num[1]

                if cell_num[0][1] == 8:
                    if cell_num[1] == 0:
                        game_grid[7][6] = 0
                    else:
                        game_grid[7][6] = cell_num[1]


            elif cell_num[0][0] == 4: #FIFTH COL

                if cell_num[0][1] == 0:
                    if cell_num[1] == 0:
                        game_grid[1][1] = 0
                    else:
                        game_grid[1][1] = cell_num[1]

                if cell_num[0][1] == 1:
                    if cell_num[1] == 0:
                        game_grid[1][4] = 0
                    else:
                        game_grid[1][4] = cell_num[1]

                if cell_num[0][1] == 2:
                    if cell_num[1] == 0:
                        game_grid[1][7] = 0
                    else:
                        game_grid[1][7] = cell_num[1]

                if cell_num[0][1] == 3:
                    if cell_num[1] == 0:
                        game_grid[4][1] = 0
                    else:
                        game_grid[4][1] = cell_num[1]

                if cell_num[0][1] == 4:
                    if cell_num[1] == 0:
                        game_grid[4][4] = 0
                    else:
                        game_grid[4][4] = cell_num[1]

                if cell_num[0][1] == 5:
                    if cell_num[1] == 0:
                        game_grid[4][7] = 0
                    else:
                        game_grid[4][7] = cell_num[1]

                if cell_num[0][1] == 6:
                    if cell_num[1] == 0:
                        game_grid[7][1] = 0
                    else:
                        game_grid[7][1] = cell_num[1]

                if cell_num[0][1] == 7:
                    if cell_num[1] == 0:
                        game_grid[7][4] = 0
                    else:
                        game_grid[7][4] = cell_num[1]

                if cell_num[0][1] == 8:
                    if cell_num[1] == 0:
                        game_grid[7][7] = 0
                    else:
                        game_grid[7][7] = cell_num[1]

            elif cell_num[0][0] == 5: #SIXTH COL

                if cell_num[0][1] == 0:
                    if cell_num[1] == 0:
                        game_grid[1][2] = 0
                    else:
                        game_grid[1][2] = cell_num[1]

                if cell_num[0][1] == 1:
                    if cell_num[1] == 0:
                        game_grid[1][5] = 0
                    else:
                        game_grid[1][5] = cell_num[1]

                if cell_num[0][1] == 2:
                    if cell_num[1] == 0:
                        game_grid[1][8] = 0
                    else:
                        game_grid[1][8] = cell_num[1]

                if cell_num[0][1] == 3:
                    if cell_num[1] == 0:
                        game_grid[4][2] = 0
                    else:
                        game_grid[4][2] = cell_num[1]

                if cell_num[0][1] == 4:
                    if cell_num[1] == 0:
                        game_grid[4][5] = 0
                    else:
                        game_grid[4][5] = cell_num[1]

                if cell_num[0][1] == 5:
                    if cell_num[1] == 0:
                        game_grid[4][8] = 0
                    else:
                        game_grid[4][8] = cell_num[1]

                if cell_num[0][1] == 6:
                    if cell_num[1] == 0:
                        game_grid[7][2] = 0
                    else:
                        game_grid[7][2] = cell_num[1]

                if cell_num[0][1] == 7:
                    if cell_num[1] == 0:
                        game_grid[7][5] = 0
                    else:
                        game_grid[7][5] = cell_num[1]

                if cell_num[0][1] == 8:
                    if cell_num[1] == 0:
                        game_grid[7][8] = 0
                    else:
                        game_grid[7][8] = cell_num[1]

            elif cell_num[0][0] == 6: #SEVENTH COL

                if cell_num[0][1] == 0:
                    if cell_num[1] == 0:
                        game_grid[2][0] = 0
                    else:
                        game_grid[2][0] = cell_num[1]

                if cell_num[0][1] == 1:
                    if cell_num[1] == 0:
                        game_grid[2][3] = 0
                    else:
                        game_grid[2][3] = cell_num[1]

                if cell_num[0][1] == 2:
                    if cell_num[1] == 0:
                        game_grid[2][6] = 0
                    else:
                        game_grid[2][6] = cell_num[1]

                if cell_num[0][1] == 3:
                    if cell_num[1] == 0:
                        game_grid[5][0] = 0
                    else:
                        game_grid[5][0] = cell_num[1]

                if cell_num[0][1] == 4:

                    if cell_num[1] == 0:
                        game_grid[5][3] = 0
                    else:
                        game_grid[5][3] = cell_num[1]

                if cell_num[0][1] == 5:
                    if cell_num[1] == 0:
                        game_grid[5][6] = 0
                    else:
                        game_grid[5][6] = cell_num[1]

                if cell_num[0][1] == 6:
                    if cell_num[1] == 0:
                        game_grid[8][0] = 0
                    else:
                        game_grid[8][0] = cell_num[1]

                if cell_num[0][1] == 7:
                    if cell_num[1] == 0:
                        game_grid[8][3] = 0
                    else:
                        game_grid[8][3] = cell_num[1]

                if cell_num[0][1] == 8:
                    if cell_num[1] == 0:
                        game_grid[8][6] = 0
                    else:
                        game_grid[8][6] = cell_num[1]


            elif cell_num[0][0] == 7: #EIGHTH COL

                if cell_num[0][1] == 0:
                    if cell_num[1] == 0:
                        game_grid[2][1] = 0
                    else:
                        game_grid[2][1] = cell_num[1]

                if cell_num[0][1] == 1:
                    if cell_num[1] == 0:
                        game_grid[2][4] = 0
                    else:
                        game_grid[2][4] = cell_num[1]

                if cell_num[0][1] == 2:
                    if cell_num[1] == 0:
                        game_grid[2][7] = 0
                    else:
                        game_grid[2][7] = cell_num[1]

                if cell_num[0][1] == 3:
                    if cell_num[1] == 0:
                        game_grid[5][1] = 0
                    else:
                        game_grid[5][1] = cell_num[1]

                if cell_num[0][1] == 4:
                    if cell_num[1] == 0:
                        game_grid[5][4] = 0
                    else:
                        game_grid[5][4] = cell_num[1]

                if cell_num[0][1] == 5:
                    if cell_num[1] == 0:
                        game_grid[5][7] = 0
                    else:
                        game_grid[5][7] = cell_num[1]

                if cell_num[0][1] == 6:
                    if cell_num[1] == 0:
                        game_grid[8][1] = 0
                    else:
                        game_grid[8][1] = cell_num[1]

                if cell_num[0][1] == 7:
                    if cell_num[1] == 0:
                        game_grid[8][4] = 0
                    else:
                        game_grid[8][4] = cell_num[1]

                if cell_num[0][1] == 8:
                    if cell_num[1] == 0:
                        game_grid[8][7] = 0
                    else:
                        game_grid[8][7] = cell_num[1]

            elif cell_num[0][0] == 8: #NINTH COL

                if cell_num[0][1] == 0:
                    if cell_num[1] == 0:
                        game_grid[2][2] = 0
                    else:
                        game_grid[2][2] = cell_num[1]

                if cell_num[0][1] == 1:
                    if cell_num[1] == 0:
                        game_grid[2][5] = 0
                    else:
                        game_grid[2][5] = cell_num[1]

                if cell_num[0][1] == 2:
                    if cell_num[1] == 0:
                        game_grid[2][8] = 0
                    else:
                        game_grid[2][8] = cell_num[1]

                if cell_num[0][1] == 3:
                    if cell_num[1] == 0:
                        game_grid[5][2] = 0
                    else:
                        game_grid[5][2] = cell_num[1]

                if cell_num[0][1] == 4:
                    if cell_num[1] == 0:
                        game_grid[5][5] = 0
                    else:
                        game_grid[5][5] = cell_num[1]

                if cell_num[0][1] == 5:
                    if cell_num[1] == 0:
                        game_grid[5][8] = 0
                    else:
                        game_grid[5][8] = cell_num[1]

                if cell_num[0][1] == 6:
                    if cell_num[1] == 0:
                        game_grid[8][2] = 0
                    else:
                        game_grid[8][2] = cell_num[1]

                if cell_num[0][1] == 7:
                    if cell_num[1] == 0:
                        game_grid[8][5] = 0
                    else:
                        game_grid[8][5] = cell_num[1]

                if cell_num[0][1] == 8:
                    if cell_num[1] == 0:
                        game_grid[8][8] = 0
                    else:
                        game_grid[8][8] = cell_num[1]



#DRAW POINTER
def draw_pointer(POINTER_LOC):
    POINTER_CORDS = [94 + ((POINTER_LOC[0])*CELL_SIZE), 94 + ((POINTER_LOC[1])*CELL_SIZE)]
    pointer_rect = pygame.Rect(POINTER_CORDS, (CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(SCREEN, 'Red', pointer_rect, 2)


#CHECK IF THE GAME GRID DISPLAYS A VALID SUDOKU BOARD
def check_solved(grid):


    #REQUIREMENTS
    cells_filled = False
    duplicate_in_sec = False
    duplicate_in_row = False
    duplicate_in_col = False


    #First condition - every cell is full with an int from 1-9
    valid_cells = 0
    for sec in grid:

        for cell in sec:
            if cell in ['1', '2', '3', '4', '5', '6', '7', '8', '9',1,2,3,4,5,6,7,8,9]:
                valid_cells+=1
    if valid_cells == 81:
        cells_filled = True


    #Second condition - no duplicates within each 9 sections
    valid_secs = 0
    for sec in grid:
        if len(sec) == len(set(sec)):
            valid_secs +=1

    if valid_secs == 9:
        duplicate_in_sec = True


    #Third condition - no duplicates within each 9 rows
    row1 = []
    row2 = []
    row3 = []
    row4 = []
    row5 = []
    row6 = []
    row7 = []
    row8 = []
    row9 = []
    all_rows = [row1, row2, row3, row4, row5, row6, row7, row8, row9]
    for sec in grid[0:3]:
        for cell in sec[0:3]:
            row1.append(cell)

    for sec in grid[0:3]:
        for cell in sec[3:6]:
            row2.append(cell)

    for sec in grid[0:3]:
        for cell in sec[6:9]:
            row3.append(cell)

    for sec in grid[3:6]:
        for cell in sec[0:3]:
            row4.append(cell)

    for sec in grid[3:6]:
        for cell in sec[3:6]:
            row5.append(cell)

    for sec in grid[3:6]:
        for cell in sec[6:9]:
            row6.append(cell)

    for sec in grid[6:9]:
        for cell in sec[0:3]:
            row7.append(cell)

    for sec in grid[6:9]:
        for cell in sec[3:6]:
            row8.append(cell)

    for sec in grid[6:9]:
        for cell in sec[6:9]:
            row9.append(cell)

    valid_rows = 0
    for row in all_rows:
        if len(row) == len(set(row)):
            valid_rows +=1

    if valid_rows == 9:
        duplicate_in_row = True


    #Fourth condition - no duplicates in columns

    col1 = []
    col2 = []
    col3 = []
    col4 = []
    col5 = []
    col6 = []
    col7 = []
    col8 = []
    col9 = []

    all_cols = [col1, col2, col3, col4, col5, col6, col7, col8, col9]

    for sec in grid[::3]:
        for cell in sec[::3]:
            col1.append(cell)

    for sec in grid[::3]:
        for cell in sec[1::3]:
            col2.append(cell)

    for sec in grid[::3]:
        for cell in sec[2::3]:
            col3.append(cell)

    for sec in grid[1::3]:
        for cell in sec[::3]:
            col4.append(cell)

    for sec in grid[1::3]:
        for cell in sec[1::3]:
            col5.append(cell)

    for sec in grid[1::3]:
        for cell in sec[2::3]:
            col6.append(cell)

    for sec in grid[2::3]:
        for cell in sec[::3]:
            col7.append(cell)

    for sec in grid[2::3]:
        for cell in sec[1::3]:
            col8.append(cell)

    for sec in grid[2::3]:
        for cell in sec[2::3]:
            col9.append(cell)


    valid_cols = 0
    for col in all_cols:
        if len(col) == len(set(col)):
            valid_cols +=1

    if valid_cols == 9:
        duplicate_in_col = True


    #CHECKING IF ALL CONDITIONS ARE TRUE


    if duplicate_in_col and duplicate_in_row and duplicate_in_sec and cells_filled:
        return True
    else:
        return False


#SHOW THE TIMER ONTO THE SCREEN
def show_timer(current_time, time_start):
    global SOLVE_PRESSED
    timer_surface = MY_FONT.render(str(int((current_time-time_start)/1000)) + ' Seconds', False, BLACK)
    timer_surface_rect = timer_surface.get_rect(topleft=(600, 20))
    SCREEN.blit(timer_surface, timer_surface_rect)









#DRAW THE LOADING SCREEN BUTTONS
def draw_buttons(mouse_pos1):
    global easy_surface_rect, medium_surface_rect, hard_surface_rect
    easy_surface = LOADING_FONT.render('EASY', False, 'Red')
    easy_surface_rect = easy_surface.get_rect(center=(400, 200))
    SCREEN.blit(easy_surface, easy_surface_rect)

    if easy_surface_rect.collidepoint(mouse_pos1):
        easy_surface = LOADING_FONT.render('EASY', False, 'Blue')
        easy_surface_rect = easy_surface.get_rect(center=(400, 200))
        SCREEN.blit(easy_surface, easy_surface_rect)

    medium_surface = LOADING_FONT.render('MEDIUM', False, 'Red')
    medium_surface_rect = medium_surface.get_rect(center=(400, 300))
    SCREEN.blit(medium_surface, medium_surface_rect)

    if medium_surface_rect.collidepoint(mouse_pos1):
        medium_surface = LOADING_FONT.render('MEDIUM', False, 'Blue')
        medium_surface_rect = medium_surface.get_rect(center=(400, 300))
        SCREEN.blit(medium_surface, medium_surface_rect)

    hard_surface = LOADING_FONT.render('HARD', False, 'Red')
    hard_surface_rect = hard_surface.get_rect(center=(400, 400))
    SCREEN.blit(hard_surface, hard_surface_rect)

    if hard_surface_rect.collidepoint(mouse_pos1):
        hard_surface = LOADING_FONT.render('HARD', False, 'Blue')
        hard_surface_rect = hard_surface.get_rect(center=(400, 400))
        SCREEN.blit(hard_surface, hard_surface_rect)




image = pygame.image.load('img.png')
image_scaled = pygame.transform.scale(image, (800, 800))



opening_screen = True
while opening_screen:
    mouse_pos1 = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if easy_surface_rect.collidepoint(event.pos):
                EASY = True
                opening_screen = False

            if medium_surface_rect.collidepoint(event.pos):
                MEDIUM = True
                opening_screen = False

            if hard_surface_rect.collidepoint(event.pos):
                HARD = True
                opening_screen = False

            time_start = pygame.time.get_ticks()




    SCREEN.fill('Black')
    SCREEN.blit(image_scaled, (0, 0))
    draw_buttons(mouse_pos1)
    clock.tick(60)
    pygame.display.update()












#This function is used input random cells of the solution board into cells_and_nums so it is displayed on the pygame board
#This is done to help the user of course to solve the board
#Note - the solution board is organised by row, col but cells and nums is organised by col, row so we had to account for this within the function

def generate_random_cells(bo, cells_and_nums, EASY, MEDIUM, HARD):


    generate_cells_num = 0
    if EASY:

        generate_cells_num += 150

    elif MEDIUM:
        generate_cells_num += 50

    elif HARD:
        generate_cells_num += 30

    cell_coords = []
    cell_values = []
    for i in range(generate_cells_num):

        num1 = randint(0,8)
        num2 = randint(0,8)
        cell_coords.append([num1,num2])
    for coord in cell_coords:
        cell_values.append(bo[coord[0]][coord[1]])

    updated_cell_coords = []
    for coord in cell_coords:
        updated_cell_coords.append(coord[::-1])

    for index, cell_num in enumerate(cells_and_nums):
        if cell_num[0] in updated_cell_coords:
            pos = updated_cell_coords.index(cell_num[0])
            cell_num[1] = (cell_values[pos])

generate_random_cells(valid_board, cells_and_nums, EASY, MEDIUM, HARD)

for cell_num in cells_and_nums:
    if cell_num[1] not in ['0', 0]:                                       #Only append the cells into filled cells if cell_num[1] != 0
        filled_cells.append(cell_num[0])  #This means only cells that have a value will be in filled cells










#MAIN GAME LOOP

run = True
while run:
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if solve_surface_rect.collidepoint(event.pos):
                handle_solve_button(valid_board)

            if clear_surface_rect.collidepoint(event.pos):
                handle_clear_button()


        if event.type == pygame.KEYDOWN and SOLVE_PRESSED!=True:

            #HANDLE ARROW KEY MOVEMENTS
            if event.key == pygame.K_UP:
                if POINTER_LOC[1] != 0:
                    POINTER_LOC[1] -=1

            if event.key == pygame.K_DOWN:
                if POINTER_LOC[1] != 8:
                    POINTER_LOC[1] +=1

            if event.key == pygame.K_LEFT:
                if POINTER_LOC[0] != 0:
                    POINTER_LOC[0] -=1

            if event.key == pygame.K_RIGHT:
                if POINTER_LOC[0] != 8:
                    POINTER_LOC[0] +=1

            #HANDLE NUMBER INPUTS
            if event.key == pygame.K_1:
                if POINTER_LOC not in filled_cells:
                    co_ord_index = co_ords.index(POINTER_LOC)
                    location = co_ords[co_ord_index]
                    for cell_num in cells_and_nums:
                        if cell_num[0] == location:
                            cell_num[1] = '1'

                    filled_cells.append(location)

            if event.key == pygame.K_2:
                if POINTER_LOC not in filled_cells:
                    co_ord_index = co_ords.index(POINTER_LOC)
                    location = co_ords[co_ord_index]
                    for cell_num in cells_and_nums:
                        if cell_num[0] == location:
                            cell_num[1] = '2'
                    filled_cells.append(location)

            if event.key == pygame.K_3:
                if POINTER_LOC not in filled_cells:
                    co_ord_index = co_ords.index(POINTER_LOC)
                    location = co_ords[co_ord_index]
                    for cell_num in cells_and_nums:
                        if cell_num[0] == location:
                            cell_num[1] = '3'
                    filled_cells.append(location)

            if event.key == pygame.K_4:
                if POINTER_LOC not in filled_cells:
                    co_ord_index = co_ords.index(POINTER_LOC)
                    location = co_ords[co_ord_index]
                    for cell_num in cells_and_nums:
                        if cell_num[0] == location:
                            cell_num[1] = '4'
                    filled_cells.append(location)

            if event.key == pygame.K_5:
                if POINTER_LOC not in filled_cells:
                    co_ord_index = co_ords.index(POINTER_LOC)
                    location = co_ords[co_ord_index]
                    for cell_num in cells_and_nums:
                        if cell_num[0] == location:
                            cell_num[1] = '5'
                    filled_cells.append(location)

            if event.key == pygame.K_6:
                if POINTER_LOC not in filled_cells:
                    co_ord_index = co_ords.index(POINTER_LOC)
                    location = co_ords[co_ord_index]
                    for cell_num in cells_and_nums:
                        if cell_num[0] == location:
                            cell_num[1] = '6'
                    filled_cells.append(location)

            if event.key == pygame.K_7:
                if POINTER_LOC not in filled_cells:
                    co_ord_index = co_ords.index(POINTER_LOC)
                    location = co_ords[co_ord_index]
                    for cell_num in cells_and_nums:
                        if cell_num[0] == location:
                            cell_num[1] = '7'
                    filled_cells.append(location)

            if event.key == pygame.K_8:
                if POINTER_LOC not in filled_cells:
                    co_ord_index = co_ords.index(POINTER_LOC)
                    location = co_ords[co_ord_index]
                    for cell_num in cells_and_nums:
                        if cell_num[0] == location:
                            cell_num[1] = '8'
                    filled_cells.append(location)

            if event.key == pygame.K_9:
                if POINTER_LOC not in filled_cells:
                    co_ord_index = co_ords.index(POINTER_LOC)
                    location = co_ords[co_ord_index]
                    for cell_num in cells_and_nums:
                        if cell_num[0] == location:
                            cell_num[1] = '9'
                    filled_cells.append(location)


            #HANDLE REMOVING NUMBERS

            if event.key == pygame.K_BACKSPACE and not check_solved(game_grid):

                if POINTER_LOC in filled_cells:

                        cells_only_from_cells_and_nums = []
                        for cell_num in cells_and_nums:                     #CHANGE THIS CELLS VALUE TO 0
                            cells_only_from_cells_and_nums.append(cell_num[0])
                        cell_index = cells_only_from_cells_and_nums.index(POINTER_LOC)
                        if isinstance(cells_and_nums[cell_index][1], int):
                            pass
                        else:
                            cells_and_nums[cell_index][1] = 0
                            filled_cell_index = filled_cells.index(POINTER_LOC)  #DELETE THIS CELL FROM FILLED CELLS
                            del filled_cells[filled_cell_index]




    #print(EASY, MEDIUM, HARD)
    #print(cells_and_nums)
    current_time = pygame.time.get_ticks()
    SCREEN.fill('White')
    draw_board()
    draw_pointer(POINTER_LOC)
    draw_numbers(cells_and_nums)
    convert_game_grid(cells_and_nums)
    for i in range(9):
        for j in range(9):
            game_grid[i][j] = int(game_grid[i][j])


    check_solved(game_grid)
    if check_solved(game_grid):
        if max_num == 1:
            winning_time = pygame.time.get_ticks()
            max_num +=1

    draw_solve_button(mouse_pos)
    draw_clear_button(mouse_pos)
    show_timer(current_time, time_start)
    clock.tick(60)



    if check_solved(game_grid) and SOLVE_PRESSED!=True:

        SCREEN.fill(BLACK)
        winning_text = MY_FONT.render('YOU WON :)   You Took ' + str((winning_time - time_start)/1000) + ' Seconds', False, 'White')
        SCREEN.blit(winning_text, (250, 380))

    pygame.display.update()

        #print('You win')
















































