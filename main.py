import util
import engine
import ui
import dictionaries

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

MONSTER_ICON = ' M'
MONSTER_START_X = 7
MONSTER_START_Y = 7
MONSTER_HP = 3

def create_player():
    return PLAYER_ICON

def get_active_board(current_level, param, level_1, level_2 ,level_3):
    if current_level == "Level 1":
        if param == "upper":
            return level_2, "Level 2"
    elif current_level == "Level 2":
        if param == "upper":
            return level_3, "Level 3"
        elif param == "lower":
            return level_1, "Level 1"
    elif current_level == "Level 3":
        if param == "lower":
            return level_2, "Level 2"

def main():
    board_level_1 = engine.create_board_level_1(BOARD_WIDTH, BOARD_HEIGHT)
    board_level_2 = engine.create_board_level_2(BOARD_WIDTH, BOARD_HEIGHT)
    board_level_3 = engine.create_board_level_3(BOARD_WIDTH, BOARD_HEIGHT)
    board = board_level_1
    player = dictionaries.player["icon"]
    gameplay(board, player, board_level_1, board_level_2, board_level_3)
    # enemy = dictionaries.enemy["monster"]

def gameplay(board, player, board_level_1, board_level_2, board_level_3, ):
    height = PLAYER_START_Y
    width = PLAYER_START_X
    board[height][width] = player
    item = engine.put_item_on_board(board, dictionaries.items)
    board = item
    
    current_level = "Level 1"
    is_running = True
    
    while is_running:
        util.clear_screen()
        ui.display_board(board, current_level)
        key = util.key_pressed()
        if key == 'q':
            is_running = False
        if key == "i":
            ui.print_message('This is your inventory content: ')
            ui.print_table(eq)
        else:
            pass
        parameter = engine.put_player_on_board(board, player, key)
        engine.put_enemy_on_board(board)
        eq = engine.item_vs_player( dictionaries.items, dictionaries.player, dictionaries.items)
        if engine.player_meets_other(dictionaries.enemy, dictionaries.player, board) != False:
            other = engine.player_meets_other(dictionaries.enemy, dictionaries.player, board)
            if dictionaries.enemy[other]['monster_type'] == 'enemy':
                engine.fight(dictionaries.player, dictionaries.enemy, other)
           
        
        if parameter:
            board, current_level = get_active_board(current_level, parameter, board_level_1, board_level_2, board_level_3)
            height = PLAYER_START_Y
            width = PLAYER_START_X
            board[height][width] = player

if __name__ == '__main__':
    main()