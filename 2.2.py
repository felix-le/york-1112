# introduce constants here
ROWS = 6
COLUMNS = 7
PLAYER = 0
OPPONENT = 1
EMPTY = 2
CONNECTED = 4

def empty_row():
    row = []
    for _ in range(COLUMNS):
        row.append(EMPTY)
    return row

def print_row(row):
    symbols = ["0", "1", "."]
    for cell in row:
        print(symbols[cell], end="")
    print()

def is_row_full(row):
    is_full = True
    for cell in row:
        is_full = is_full and cell != EMPTY
    return is_full

def copy_row(row):
    copy = []
    for cell in row:
        copy.append(cell)
    return copy

def empty_board():    
    board = []
    for _ in range(ROWS):
        board.append(empty_row())
    return board

def print_board(board):
    for row_index in range(ROWS - 1, -1, -1):
        print_row(board[row_index])

def is_board_full(board):
    is_full = True
    for row in board:
        is_full = is_full and is_row_full(row)
    return is_full

def copy_board(board):
    copy = []
    for row in board:
        copy.append(copy_row(row))
    return copy

def drop(board, column_index, player):
    success = True
    row_index = 0
    while row_index < ROWS and board[row_index][column_index] != EMPTY:
        row_index += 1
    if row_index == ROWS:
        success = False
    else:
        board[row_index][column_index] = player
    return success

def has_won_horizontal(board, player):
    has_won = False
    for row in board:
        connected = 0
        for cell in row:
            if cell == player:
                connected += 1
                if connected == CONNECTED:
                    has_won = True
            else:
                connected = 0
    return has_won

def has_won(board, player):
    for row_index in range(ROWS):
        for column_index in range(COLUMNS):
            if board[row_index][column_index] != player:
                continue
            directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
            for row_step, column_step in directions:
                connected = 1
                next_row = row_index + row_step
                next_column = column_index + column_step
                while (0 <= next_row < ROWS
                       and 0 <= next_column < COLUMNS
                       and board[next_row][next_column] == player):
                    connected += 1
                    if connected == CONNECTED:
                        return True
                    next_row += row_step
                    next_column += column_step
    return False


if __name__ == "__main__":
    board = empty_board()
    drop(board, 1, PLAYER)
    drop(board, 2, OPPONENT)
    print_board(board)