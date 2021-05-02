import util
import engine
import ui

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 20
BOARD_HEIGHT = 10

GATE_ICON = "+"
GATE_TO_UPPER_LEVEL = "U"
GATE_TO_LOWER_LEVEL = "L"


def create_player():
    return PLAYER_ICON


def main():
    player = create_player()
    height = PLAYER_START_Y
    width = PLAYER_START_X
    board = engine.create_board_level_1(BOARD_WIDTH, BOARD_HEIGHT)
    board[height][width] = player
    is_running = True
    
    while is_running:
        util.clear_screen()
        ui.display_board(board)
        key = util.key_pressed()
        if key == 'q':
            is_running = False
        else:
            pass
        engine.put_player_on_board(board, player, key)


if __name__ == '__main__':
    main()