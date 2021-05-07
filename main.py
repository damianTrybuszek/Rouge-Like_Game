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

enemy_list = [dictionaries.enemy["monster"]["icon"], dictionaries.enemy["boss"]["icon"], dictionaries.enemy["ghost"]["icon"]]
item_list = [dictionaries.items["shield"]["icon"], dictionaries.items["sword"]["icon"], dictionaries.items["armor"]["icon"]]

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
    player = dictionaries.player
    gameplay(board, player, board_level_1, board_level_2, board_level_3)

def gameplay(board, player, board_level_1, board_level_2, board_level_3, ):
    height = PLAYER_START_Y
    width = PLAYER_START_X
    board[height][width] = player["icon"]
    inventory = dictionaries.inventory
    current_level = "Level 1"
    is_running = True
    util.clear_screen()
    ui.print_story()
    
    while is_running:
        util.clear_screen()
        ui.display_board(board, current_level, player)
        key = util.key_pressed()
        if key == 'q':
            is_running = False
        if key == "i":
            ui.print_message('This is your inventory content: \n')
            ui.print_table(inventory)
            input("Press enter to continue:\n")
        else: 
            parameter = engine.put_player_on_board(board, player, key)
            engine.put_enemy_on_board(board, player)
            if parameter:
                if parameter in item_list:
                    engine.item_vs_player(inventory, dictionaries.items, player, parameter)
                else:
                    board, current_level = get_active_board(current_level, parameter, board_level_1, board_level_2, board_level_3)
                    height = PLAYER_START_Y
                    width = PLAYER_START_X
                    board[height][width] = player["icon"]

if __name__ == '__main__':
    main()