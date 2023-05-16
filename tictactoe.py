X_CHAR = 'X'
O_CHAR = 'O'
def print_board(board):
    print(f"""---------
| {board[0][0]} {board[0][1]} {board[0][2]} |
| {board[1][0]} {board[1][1]} {board[1][2]} |
| {board[2][0]} {board[2][1]} {board[2][2]} |
---------""")


def is_winner(board, character):
    # check vertically
    for row in board:
        row_character_count = sum([1 for c in row if c == character])
        if row_character_count == 3:
            return True
    # check horizontally

    for i in range(3):
        count = 0
        count += int(board[0][i] == character)
        count += int(board[1][i] == character)
        count += int(board[2][i] == character)
        if count == 3:
            return True

    # check cross
    if board[0][0] == character and board[1][1] == character and board[2][2] == character:
        return True
    if board[0][2] == character and board[1][1] == character and board[2][0] == character:
        return True

    return False


def is_draw(board):
    sign_count = sum([1 for row in board for c in row if c == X_CHAR or c == O_CHAR])
    return sign_count == 9


def check_coordinates(cord_x, cord_y) -> bool:
    if not cord_x.isdigit() or not cord_y.isdigit():
        print("You should enter numbers!")
        return False
    cord_x = int(cord_x)
    cord_y = int(cord_y)
    if not cord_x in range(0, 4) or not cord_y in range(0, 4):
        print("Coordinates should be from 1 to 3!")
        return False
    return True


def is_cell_empty(board, x, y):
    if board[x][y] == X_CHAR or board[x][y] == O_CHAR:
        print("This cell is occupied! Choose another one!")
        return False
    return True


def insert_char(board, character, x, y):
    ls = list(board[x])
    ls[y] = character
    board[x] = ls
    return board


game_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
player = X_CHAR
print_board(game_board)
run = True
while run:
    move = input().split(" ")
    move_ok = check_coordinates(move[0], move[1])

    if not move_ok:
        continue

    cell_ok = is_cell_empty(game_board, int(move[0]) - 1, int(move[1]) - 1)
    if not cell_ok:
        continue

    game_board = insert_char(game_board, player, int(move[0]) - 1, int(move[1]) - 1)
    print_board(game_board)

    if is_winner(game_board, X_CHAR):
        print("X wins")
        run = False
    elif is_winner(game_board, O_CHAR):
        print("O wins")
        run = False
    elif is_draw(game_board):
        print("Draw")
        run = False

    if player == X_CHAR:
        player = O_CHAR
    else:
        player = X_CHAR






