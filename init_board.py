from random import choice, sample
from main import check_row, check_col, check_box


valid_set = [i for i in range(1,10)]

def init_board(level="easy"):

    if level == "easy":
        numbers = 9
    elif level == "medium":
        numbers = 6
    else:
        numbers = 3

    init_numbers = [choice(valid_set) for _ in range(numbers)]

    init_positions = sample([i for i in range(81)], numbers)

    return init_numbers, init_positions



def build_board():

    init_b = init_board()
    board = [0 for _ in range(81)]

    for index, number in enumerate(init_b[0]):
        board[init_b[1][index]] = number

    return board


valid_init_boards = []

while len(valid_init_boards) < 5:
    board = build_board()

    rows = [check_row(board, i) for i in range(9)]
    cols = [check_col(board, i) for i in range(9)]
    boxs = [check_box(board, i) for i in range(9)]

    if all(rows) & all(cols) & all(boxs):
        valid_init_boards.append(board)


for board in valid_init_boards:
    board_ = ''

    for index, item in enumerate(board):
        if index % 9 == 8:
            board_ += str(item) + '\n'
            if (index % 8 == 2) | (index % 8 == 5):
                board_ += str('---------------------') + '\n'
        elif index % 3 == 2:
            board_ += str(item) + ' | '
        else:
            board_ += str(item) + ' '

    print(board_)