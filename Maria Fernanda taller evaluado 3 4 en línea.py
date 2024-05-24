import numpy as np

# Constantes
ROWS = 6
COLS = 7
PLAYER1 = 1
PLAYER2 = 2

# Crear el tablero
def create_board():
    return np.zeros((ROWS, COLS), dtype=int)

# Imprimir el tablero
def print_board(board):
    print(np.flip(board, 0))

# Verificar si la ubicación es válida para una pieza normal
def is_valid_location(board, col):
    return board[ROWS-1][col] == 0

# Obtener la siguiente fila abierta
def get_next_open_row(board, col):
    for r in range(ROWS):
        if board[r][col] == 0:
            return r

# Verificar si la ubicación es válida para una pieza en L
def is_valid_L_location(board, row, col, shape):
    if shape == '3x1':
        return row >= 2 and col < COLS - 1 and board[row][col] == 0 and board[row-1][col] == 0 and board[row-2][col] == 0 and board[row-2][col+1] == 0
    elif shape == '2x2':
        return row >= 1 and col < COLS - 1 and board[row][col] == 0 and board[row][col+1] == 0 and board[row-1][col] == 0
    elif shape == '1x3':
        return row >= 1 and col < COLS - 2 and board[row][col] == 0 and board[row][col+1] == 0 and board[row][col+2] == 0 and board[row-1][col+2] == 0
    return False

# Colocar pieza en forma de L
def drop_L_piece(board, row, col, piece, shape):
    if shape == '3x1':
        for r in range(3):
            board[row-r][col] = piece
        board[row-2][col+1] = piece
    elif shape == '2x2':
        for r in range(2):
            board[row-r][col] = piece
        board[row-1][col+1] = piece
    elif shape == '1x3':
        for c in range(3):
            board[row][col+c] = piece
        board[row-1][col+2] = piece

# Colocar pieza normal
def drop_piece(board, row, col, piece):
    board[row][col] = piece

# Verificar condiciones de victoria
def winning_move(board, piece):
    # Verificar ubicaciones horizontales
    for c in range(COLS-3):
        for r in range(ROWS):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
    
    # Verificar ubicaciones verticales
    for c in range(COLS):
        for r in range(ROWS-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
    
    # Verificar diagonales con pendiente positiva
    for c in range(COLS-3):
        for r in range(ROWS-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Verificar diagonales con pendiente negativa
    for c in range(COLS-3):
        for r in range(3, ROWS):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True
    
    return False

# Bucle principal del juego
board = create_board()
print_board(board)
game_over = False
turn = 0

while not game_over:
    # Pedir la entrada del jugador
    if turn == 0:
        col = int(input("Jugador 1, haga su selección (0-6): "))
        piece_shape = input("Elija la forma de la pieza (1: normal, 2: L 3x1, 3: L 2x2, 4: L 1x3): ")
        
        if piece_shape == '1':
            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, PLAYER1)
                
                if winning_move(board, PLAYER1):
                    print("¡Jugador 1 gana!")
                    game_over = True
        else:
            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                if piece_shape == '2' and is_valid_L_location(board, row, col, '3x1'):
                    drop_L_piece(board, row, col, PLAYER1, '3x1')
                elif piece_shape == '3' and is_valid_L_location(board, row, col, '2x2'):
                    drop_L_piece(board, row, col, PLAYER1, '2x2')
                elif piece_shape == '4' and is_valid_L_location(board, row, col, '1x3'):
                    drop_L_piece(board, row, col, PLAYER1, '1x3')
                if winning_move(board, PLAYER1):
                    print("¡Jugador 1 gana!")
                    game_over = True
    
    else:
        col = int(input("Jugador 2, haga su selección (0-6): "))
        piece_shape = input("Elija la forma de la pieza (1: normal, 2: L 3x1, 3: L 2x2, 4: L 1x3): ")
        
        if piece_shape == '1':
            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, PLAYER2)
                
                if winning_move(board, PLAYER2):
                    print("¡Jugador 2 gana!")
                    game_over = True
        else:
            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                if piece_shape == '2' and is_valid_L_location(board, row, col, '3x1'):
                    drop_L_piece(board, row, col, PLAYER2, '3x1')
                elif piece_shape == '3' and is_valid_L_location(board, row, col, '2x2'):
                    drop_L_piece(board, row, col, PLAYER2, '2x2')
                elif piece_shape == '4' and is_valid_L_location(board, row, col, '1x3'):
                    drop_L_piece(board, row, col, PLAYER2, '1x3')
                if winning_move(board, PLAYER2):
                    print("¡Jugador 2 gana!")
                    game_over = True
    
    print_board(board)
    
    turn += 1
    turn = turn % 2

