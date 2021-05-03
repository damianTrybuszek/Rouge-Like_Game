import util
import engine
import ui
from player import Player

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 30
BOARD_HEIGHT = 10
GATE_ICON = 'G'

def create_player():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''

    return Player()


def main():
    player = create_player()
    level = 1
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT, level)

    util.clear_screen()
    is_running = True
    engine.put_player_on_board(board, player)
    while is_running:
        ui.display_board(board)

        key = util.key_pressed()
        if key == 'q':
            is_running = False
        else:
            board.move_player(key)
            
        util.clear_screen()


if __name__ == '__main__':
    main()
