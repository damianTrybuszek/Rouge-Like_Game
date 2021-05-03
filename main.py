import util
import engine
import ui

PLAYER_ICON = '@'
PLAYER_START_X = 5
PLAYER_START_Y = 3

BOARD_WIDTH = 20
BOARD_HEIGHT = 10

GATE_ICON = chr(9647)
GATE_TO_UPPER_LEVEL = "U"
GATE_TO_LOWER_LEVEL = "L"
PATH_ICON = chr(9641)
WALL_ICON = chr(9609)

def create_player():
    return PLAYER_ICON

def get_active_board(active_board, param, level_1, level_2 ,level_3):
    if active_board == level_1:
        if param == "upper":
            return level_2
    elif active_board == level_2:
        if param == "upper":
            return level_3
        elif param == "lower":
            return level_1
    elif active_board == level_3:
        if param == "lower":
            return level_1
    else: 
        return active_board

def main():
    board_level_1 = engine.create_board_level_1(BOARD_WIDTH, BOARD_HEIGHT)
    board_level_2 = engine.create_board_level_2(BOARD_WIDTH, BOARD_HEIGHT)
    board_level_3 = engine.create_board_level_3(BOARD_WIDTH, BOARD_HEIGHT)
    board = board_level_1
    player = create_player()
    gameplay(board, player, board_level_1, board_level_2, board_level_3)

def gameplay(board, player, board_level_1, board_level_2, board_level_3):
    height = PLAYER_START_Y
    width = PLAYER_START_X
    board[height][width] = player
    is_running = True
    
    while is_running:
        util.clear_screen()
        ui.display_board(board)
        key = util.key_pressed()
        if key == 'q':
            is_running = False
        if key == "i":
            pass
        else:
            pass
        parameter = engine.put_player_on_board(board, player, key)
        if parameter:
            board = get_active_board(board, parameter, board_level_1, board_level_2, board_level_3)
            height = PLAYER_START_Y
            width = PLAYER_START_X
            board[height][width] = player

if __name__ == '__main__':
    main()