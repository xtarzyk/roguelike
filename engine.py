import random
import numpy

MIN_WALL_LEN = 30
MAX_WALL_LEN = 45
CLIFF = '\033[38;5;94m' + '\u25AE' + '\033[0m'

def create_board(width, height, frame = True):
    board = []

    for i in range(height):
        board.append([])

    for row in board:
        for i in range(width):
            row.append(" ")
        row[0] = CLIFF
        row[-1] = CLIFF

    for i in range(width):
        board[0][i] = CLIFF
        board[-1][i] = CLIFF

    if frame:
        board = random_walls(board,width)
        board = random_walls(board, width, top_side = False)

    return board



def random_walls(board,width, top_side = True):
    for j in range (5):
        a_1 = random.randint(1, width-MAX_WALL_LEN-1)
        b_1 = random.randint(MIN_WALL_LEN, MAX_WALL_LEN)

        for i in range(a_1, a_1 + b_1):
            board[1][i] = CLIFF

        lines = random.randint(2,10)

        for i in range(lines):
            offset = random.randint(1,3)
            a_1 = a_1 + offset
            b_1 = random.randint(b_1 - offset -5, b_1 - offset - 1)
            for n in range (a_1, a_1 + b_1):
                if top_side:
                    board[i+2][n] = CLIFF
                else:
                    board[-2-i][n] = CLIFF
        
    return board


def put_player_on_board(board, player):
    x = player['x']
    y = player['y']
    board[y][x] = player['avatar']
    board[15][99] = "#"


def put_gold_on_board(board):
    i = 0
    while i < 3:
        a = random.randint(1, 25)
        b = random.randint(1, 60)
        if board[a][b] == " ":
            board[a][b] = "G"
            i = i + 1

def create_enemies(board, enemy, numbers_of_enemies):
    i = 0
    while i < numbers_of_enemies:
        a = random.randint(1, len(board)-1)
        b = random.randint(1, len(board[0])-1)
        if board[a][b] == " ":
            board[a][b] = enemy
            i = i + 1


    
def move_enemies(board, enemy):
    for row_index in range(len(board)):
        for col_index in range(len(board[row_index])):
            element = board[row_index][col_index]
            if element == enemy:
                board[row_index][col_index] = ' '
                is_move = False
                while not is_move:
                    row_move = random.randint(-1,1)
                    col_move = random.randint(-1,1)
                    if board[row_index+row_move][col_index+col_move] == ' ':
                        board[row_index+row_move][col_index+col_move] = enemy
                        is_move = True
