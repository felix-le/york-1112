import random
# introduce constants here
ROWS = 6
COLUMNS = 7
PLAYER = 0
OPPONENT = 1
EMPTY = 2

def empty_row():
    row = []
    for _ in range(COLUMNS):
        # row.append(EMPTY)
        row += [EMPTY]
    return row

def print_row(row):
    # symbols = ["0","1","."]
    # for cell in row:
    #     print(symbols[cell], end="")
    # print()
    for cell in row:
        if cell == EMPTY:
            print (".", end="")
        else:
            print (cell, end="")
    print()

def is_row_full(row):
    is_full = True
    for cell in row:
        if cell == EMPTY:
            return False
        # is_full = is_full and cell != EMPTY
    return is_full

def copy_row(row):
    copy = []
    # add your code here
    for cell in row:
        copy.append(cell)
    return copy

def empty_board():    
    board = []
    # add your code here
    for _ in range(ROWS):
        board.append(empty_row)
    return board

def print_board(board):
    for row_index in range(ROWS - 1, -1, -1):
        print_row(board[row_index])
    # for i in range(len(board)):
    #     print_row(board[ROWS - 1])

def is_board_full(board):
    is_Full = True
    for row in board:
        is_Full = is_Full and is_row_full(row)
    return is_Full

def copy_board(board):
    copy = []
    for row in board:
        copy.append(copy_row(row))
    return copy

def drop(board, column_index, player):
    success = True
    # add your code here
    row_index = 0
    while row_index < ROWS and board[row_index][column_index] != EMPTY:
        row_index +=1
    else:
        board[row_index][column_index] = player
    return success

def valid_columns(board):
    valid = []
    for col in range(COLUMNS):
        if board[ROWS - 1][col]== EMPTY:
            valid.append(col)
    return valid

def random_drop(board):
    isValid = valid_columns(board)
    index = random.choice(isValid)
    # drop
    # while row_index < ROWS and board[row_index][row_index] != EMPTY:
    #     row_index += 1
    # else:
    #     board

def has_won_horizontal(board, player):
    has_won = False
    # add your code here
    return has_won

row = empty_row()
row[1] = PLAYER
row[2] = OPPONENT
print_row(row)