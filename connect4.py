import numpy as np

WIN_NO = 4
ROWS = 6
COLUMNS = 7

def create_board():
    board = np.zeros(( ROWS, COLUMNS))
    return board

def print_board(board):
    print(np.flip(board, 0))

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[5][col] == 0

def get_next_open_row(board, col):
    for r in range(ROWS):
        if board[r][col] == 0 :
            return r

def winning_move(board, piece):
    count = 0

    #test of horizontal wining
    for x in range(ROWS):
        for y in range(COLUMNS):
            if board[x][y] == piece:
                count += 1
            else:
                count = 0
            if count == WIN_NO:
                return True
    
    #test of vertical wining
    for y in range(COLUMNS):
        for x in range(ROWS):
            if board[x][y] == piece:
                count += 1
            else:
                count = 0
            if count == WIN_NO:
                return True

    #test of diagonal right wining
    for x in range(ROWS-WIN_NO):
        for y in range(COLUMNS-WIN_NO):
            for r in range(WIN_NO):
                if board[x+r][y+r] == piece:
                    count += 1
            if count == WIN_NO:
                return True
            count = 0

    #test of diagonal left wining
    for x in range(ROWS - WIN_NO + 1):
        for y in range(WIN_NO-1, COLUMNS):
            for r in range(WIN_NO):
                if board[x+r][y-r] == piece:
                    count += 1
            if count == WIN_NO:
                return True
            count = 0
    
    return False
    



board = create_board()
game_over = False
turn = 0

while not game_over:
    print_board(board)
    #Player 1 turn
    if turn == 0:   
        col = int (input("Player 1 make your selection (0-6): "))
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, turn+1)
        if winning_move(board, 1):
            print_board(board)
            print("YOU WON!")
            game_over = True

    #Player 2 turn
    else:   
        col = int (input("Player 2 make your selection (0-6): "))
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, turn+1)
            if winning_move(board, 2):
                print_board(board)
                print("YOU WON!")
                game_over = True
    turn = (turn + 1) % 2