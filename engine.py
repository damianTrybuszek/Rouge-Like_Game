import main
import random
import ui
import math
import dictionaries


def create_board_level_1(width, height):
    board = []
    for i in range(30):
        temp_table = []
        for j in range(60):
            temp_table.append(" ")
        board.append(temp_table)

    for i in range(height):
        for j in range(width):
            if i == 3 and j == width-1:
                board[i][j]=main.GATE_ICON
            elif j == 0 or j == width -1:
                board[i][j]=main.WALL_ICON
            elif i == 0 or i == height -1:
                board[i][j]=main.WALL_ICON

    for i in range(height+2):
        for j in range(width-4):
            if i == 5 and j == width- 4 -1:
                board[i][j+30]=main.GATE_ICON
            elif i == 4 and j == 0:
                board[i][j+30]=main.GATE_ICON
            elif j == 0 or j == width - 4 -1:
                board[i][j+30]=main.WALL_ICON
            elif i == 0 or i == height +2 - 1:
                board[i][j+30]=main.WALL_ICON

    for i in range(height-2):
        for j in range(width+2):
            if i == 2 and j == width+2 -1:
                board[i+17][j+34]=main.GATE_ICON
            elif i == 3 and j == 0:
                board[i+17][j+34]=main.GATE_ICON
            elif j == 0 or j == width +2 -1:
                board[i+17][j+34]=main.WALL_ICON
            elif i == 0 or i == height - 2 - 1:
                board[i+17][j+34]=main.WALL_ICON
            elif (i == 5 and j == 4) or (i == 4 and j == 5):
                board[i+17][j+34] = dictionaries.enemy["monster"]["icon"]

    for i in range(height):
        for j in range(width-4):
            if i == 4 and j == width- 4 -1:
                board[i+20][j+10]=main.GATE_ICON
            elif i == height/2 and j == (width- 4)/2:
                board[i+20][j+10]=main.GATE_TO_UPPER_LEVEL
            elif j == 0 or j == width - 4 -1:
                board[i+20][j+10]=main.WALL_ICON
            elif i == 0 or i == height - 1:
                board[i+20][j+10]=main.WALL_ICON

    gate_coords = []

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == main.GATE_ICON:
                gate_coords.append((i,j))

    distance_1 = gate_coords[1][1] - gate_coords[0][1]
    distance_2 = gate_coords[3][1] - gate_coords[2][1]
    distance_3 = gate_coords[3][0] - gate_coords[2][0]
    distance_4 = distance_2 + 3 -  (gate_coords[3][1] - gate_coords[2][1])
    distance_5 = gate_coords[4][1] - gate_coords[5][1]
    distance_6 = gate_coords[5][0] - gate_coords[4][0]

    for i in range(distance_1-1):
        if i <= distance_1//2:
            height = gate_coords[0][0] 
            width = gate_coords[0][1] +1 
            board[height][width+i] = main.PATH_ICON
        if i >= distance_1 // 2:
            height = gate_coords[0][0] + 1
            width = gate_coords[0][1] + 1 
            board[height][width+i] = main.PATH_ICON
        
    for i in range(distance_2+3):
        if i <= distance_2 + 3:
            height = gate_coords[2][0] 
            width = gate_coords[2][1] +1 
            board[height][width+i] = main.PATH_ICON
        if i == distance_2 + 2:
            for j in range(distance_3+1):
                board[height+j][width + i] = main.PATH_ICON

    for i in range(distance_4-1):
        height = gate_coords[3][0] 
        width = gate_coords[3][1] +1 
        board[height][width+i] = main.PATH_ICON

    for i in range(distance_5):
        if i <= distance_5//2:
            height = gate_coords[5][0] 
            width = gate_coords[5][1] +1 
            board[height][width+i] = main.PATH_ICON
        if i == distance_5 // 2:
            for j in range(distance_6):
                board[height-j][width + i] = main.PATH_ICON
    
    for i in range(distance_5-1):
        if i >= distance_5//2:
            height = gate_coords[5][0] - distance_6 
            width = gate_coords[5][1] +1
            board[height][width+i] = main.PATH_ICON

    return board

def create_board_level_2(width, height):
    board = []
    for i in range(30):
        temp_table = []
        for j in range(60):
            temp_table.append(" ")
        board.append(temp_table)

    for i in range(height):
        for j in range(width):
            if i == 3 and j == width-1:
                board[i][j]=main.GATE_ICON
            elif i == height//2 and j == (width)//2:
                board[i][j]=main.GATE_TO_LOWER_LEVEL
            elif j == 0 or j == width -1:
                board[i][j]=main.WALL_ICON
            elif i == 0 or i == height -1:
                board[i][j]=main.WALL_ICON

    for i in range(height+2):
        for j in range(width+4):
            if i == 5 and j == width+ 4 -1:
                board[i][j+26]=main.GATE_ICON
            elif i == 4 and j == 0:
                board[i][j+26]=main.GATE_ICON
            elif j == 0 or j == width + 4 -1:
                board[i][j+26]=main.WALL_ICON
            elif i == 0 or i == height +2 - 1:
                board[i][j+26]=main.WALL_ICON

    for i in range(height+5):
        for j in range(width+2):
            if i == 2 and j == width+2 -1:
                board[i+12][j+6]=main.GATE_ICON
            elif i == 6 and j == 0:
                board[i+12][j+6]=main.GATE_ICON
            elif j == 0 or j == width +2 -1:
                board[i+12][j+6]=main.WALL_ICON
            elif i == 0 or i == height +5 - 1:
                board[i+12][j+6]=main.WALL_ICON

    for i in range(height):
        for j in range(width-4):
            if i == 4 and j == width- 4 -1:
                board[i+18][j+30]=main.GATE_ICON
            elif i == height/2 and j == (width- 4)/2:
                board[i+18][j+30]=main.GATE_TO_UPPER_LEVEL
            elif j == 0 or j == width - 4 -1:
                board[i+18][j+30]=main.WALL_ICON
            elif i == 0 or i == height - 1:
                board[i+18][j+30]=main.WALL_ICON

    gate_coords = []

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == main.GATE_ICON:
                gate_coords.append((i,j))

    distance_1 = gate_coords[1][1] - gate_coords[0][1]
    distance_2 = 3 
    distance_3 = gate_coords[3][0] - gate_coords[2][0]
    distance_4 = distance_2 + distance_2 -  (gate_coords[3][1] - gate_coords[2][1])
    distance_5 = 3
    distance_6 = len(board) - gate_coords[4][0]-1
    distance_7 = len(board) - gate_coords[5][0]-1
    distance_8 = gate_coords[5][1] - gate_coords[4][1] +1
    

    for i in range(distance_1-1):
        if i <= distance_1//2:
            height = gate_coords[0][0] 
            width = gate_coords[0][1] +1 
            board[height][width+i] = main.PATH_ICON
        if i >= distance_1 // 2:
            height = gate_coords[0][0] + 1
            width = gate_coords[0][1] + 1 
            board[height][width+i] = main.PATH_ICON
        
    for i in range(distance_2+3):
        if i <= distance_2 + 3:
            height = gate_coords[2][0] 
            width = gate_coords[2][1] +1 
            board[height][width+i] = main.PATH_ICON
        if i == distance_2 + 2:
            for j in range(distance_3+1):
                board[height+j][width + i] = main.PATH_ICON

    for i in range(distance_4-1):
        height = gate_coords[3][0] 
        width = gate_coords[3][1] +1 
        board[height][width+i] = main.PATH_ICON

    for i in range(distance_5):
        if i <= distance_5-1:
            height = gate_coords[4][0] 
            width = gate_coords[4][1] -1
            board[height][width-i] = main.PATH_ICON
        if i == distance_5 -1:
            for j in range(distance_6):
                board[height+j][width - i] = main.PATH_ICON
    
    for i in range(distance_8 + 2*distance_5):
        height = gate_coords[4][0] + distance_6 
        width = gate_coords[4][1] - distance_5
        board[height][width+i] = main.PATH_ICON
        if i == distance_8 + 2*distance_5-1:
            for j in range(distance_7):
                board[height-j][width + i] = main.PATH_ICON

    for i in range(distance_5):
        height = gate_coords[5][0] 
        width = gate_coords[5][1] +1 
        board[height][width+i] = main.PATH_ICON
    

    return board

def create_board_level_3(width, height):
    board = []
    for i in range(30):
        temp_table = []
        for j in range(60):
            temp_table.append(" ")
        board.append(temp_table)

    for i in range(height+2):
        for j in range(width+2):
            if i == 3 and j == width +2 -1:
                board[i][j]=main.GATE_ICON
            elif i == (height+2)//2 and j == (width+2)//2:
                board[i][j]=main.GATE_TO_LOWER_LEVEL
            elif j == 0 or j == width + 2 - 1:
                board[i][j]=main.WALL_ICON
            elif i == 0 or i == height + 2 - 1:
                board[i][j]=main.WALL_ICON

    for i in range(height+4):
        for j in range(width-4):
            if i == 5 and j == width- 4 -1:
                board[i+2][j+30]=main.GATE_ICON
            elif i == 2 and j == 0:
                board[i+2][j+30]=main.GATE_ICON
            elif j == 0 or j == width - 4 -1:
                board[i+2][j+30]=main.WALL_ICON
            elif i == 0 or i == height +4 - 1:
                board[i+2][j+30]=main.WALL_ICON

    for i in range(height):
        for j in range(width+2):
            if i == 2 and j == width+2 -1:
                board[i+17][j+32]=main.GATE_ICON
            elif i == 3 and j == 0:
                board[i+17][j+32]=main.GATE_ICON
            elif j == 0 or j == width +2 -1:
                board[i+17][j+32]=main.WALL_ICON
            elif i == 0 or i == height - 1:
                board[i+17][j+32]=main.WALL_ICON

    for i in range(height+2):
        for j in range(width+6):
            if i == 4 and j == width + 6 -1:
                board[i+18][j+2]=main.GATE_ICON
            elif j == 0 or j == width + 6 -1:
                board[i+18][j+2]=main.WALL_ICON
            elif i == 0 or i == height + 2 - 1:
                board[i+18][j+2]=main.WALL_ICON

    gate_coords = []

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == main.GATE_ICON:
                gate_coords.append((i,j))

    distance_1 = gate_coords[1][1] - gate_coords[0][1]
    distance_2 = gate_coords[3][1] - gate_coords[2][1]
    distance_3 = gate_coords[3][0] - gate_coords[2][0]
    distance_4 = distance_2 + 3 -  (gate_coords[3][1] - gate_coords[2][1])
    distance_5 = gate_coords[4][1] - gate_coords[5][1]
    distance_6 = gate_coords[5][0] - gate_coords[4][0]

    for i in range(distance_1-1):
        if i <= distance_1//2:
            height = gate_coords[0][0] 
            width = gate_coords[0][1] +1 
            board[height][width+i] = main.PATH_ICON
        if i >= distance_1 // 2:
            height = gate_coords[0][0] + 1
            width = gate_coords[0][1] + 1 
            board[height][width+i] = main.PATH_ICON
        
    for i in range(distance_2+3):
        if i <= distance_2 + 3:
            height = gate_coords[2][0] 
            width = gate_coords[2][1] +1 
            board[height][width+i] = main.PATH_ICON
        if i == distance_2 + 2:
            for j in range(distance_3+1):
                board[height+j][width + i] = main.PATH_ICON

    for i in range(distance_4-1):
        height = gate_coords[3][0] 
        width = gate_coords[3][1] +1 
        board[height][width+i] = main.PATH_ICON

    for i in range(distance_5):
        if i <= distance_5//2:
            height = gate_coords[5][0] 
            width = gate_coords[5][1] +1 
            board[height][width+i] = main.PATH_ICON
        if i == distance_5 // 2:
            for j in range(distance_6):
                board[height-j][width + i] = main.PATH_ICON
    
    for i in range(distance_5-1):
        if i >= distance_5//2:
            height = gate_coords[5][0] - distance_6 
            width = gate_coords[5][1] +1
            board[height][width+i] = main.PATH_ICON

    return board


def put_player_on_board(board, player, move):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == player:
                height = i
                width = j
                break
    
    gate_coords = []

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == main.GATE_ICON:
                gate_coords.append((i,j))


    if move.lower() == "w" and board[height-1][width] not in [main.WALL_ICON, main.GATE_ICON, main.GATE_TO_UPPER_LEVEL, main.GATE_TO_LOWER_LEVEL]:
        board[height][width] = " "
        height -=1
        board[height][width] = player
    elif move.lower() == "a" and board[height][width-1] not in [main.WALL_ICON, main.GATE_ICON, main.GATE_TO_UPPER_LEVEL, main.GATE_TO_LOWER_LEVEL]:
        board[height][width] = " "
        width -= 1
        board[height][width] = player
    elif move.lower() == "s" and board[height+1][width] not in [main.WALL_ICON, main.GATE_ICON, main.GATE_TO_UPPER_LEVEL, main.GATE_TO_LOWER_LEVEL]:
        board[height][width] = " "
        height += 1
        board[height][width] = player
    elif move.lower() == "d" and board[height][width+1] not in [main.WALL_ICON, main.GATE_ICON, main.GATE_TO_UPPER_LEVEL, main.GATE_TO_LOWER_LEVEL]:
        board[height][width] = " "
        width += 1
        board[height][width] = player

    if move.lower() == "w" and board[height-1][width] in [main.GATE_TO_UPPER_LEVEL]:
        board[height][width] = " "
        return "upper"
    elif move.lower() == "a" and board[height][width-1] in [main.GATE_TO_UPPER_LEVEL]:
        board[height][width] = " "
        return  "upper"
    elif move.lower() == "s" and board[height+1][width] in [main.GATE_TO_UPPER_LEVEL]:
        board[height][width] = " "
        return  "upper"
    elif move.lower() == "d" and board[height][width+1] in [main.GATE_TO_UPPER_LEVEL]:
        board[height][width] = " "
        return  "upper"
    
    if move.lower() == "w" and board[height-1][width] in [main.GATE_TO_LOWER_LEVEL]:
        board[height][width] = " "
        return "lower"
    elif move.lower() == "a" and board[height][width-1] in [main.GATE_TO_LOWER_LEVEL]:
        board[height][width] = " "
        return "lower"
    elif move.lower() == "s" and board[height+1][width] in [main.GATE_TO_LOWER_LEVEL]:
        board[height][width] = " "
        return "lower"
    elif move.lower() == "d" and board[height][width+1] in [main.GATE_TO_LOWER_LEVEL]:
        board[height][width] = " "
        return "lower"
    

    if move.lower() == "w" and board[height-1][width] == main.GATE_ICON:
        board[height][width] = " " 
        height -=1
        if (height, width) == gate_coords[0]:
            height = gate_coords[1][0] - 1
            width = gate_coords[1][1]
        elif (height, width) == gate_coords[1]:
            height = gate_coords[0][0] + 1
            width = gate_coords[0][1]
        elif (height, width) == gate_coords[2]:
            height = gate_coords[3][0] - 1
            width = gate_coords[3][1]
        elif (height, width) == gate_coords[3]:
            height = gate_coords[2][0] + 1
            width = gate_coords[2][1]
        elif (height, width) == gate_coords[4]:
            height = gate_coords[5][0] + 1
            width = gate_coords[5][1]
        elif (height, width) == gate_coords[5]:
            height = gate_coords[4][0] + 1
            width = gate_coords[4][1]
        
        board[height][width] = player


    elif move.lower() == "a" and board[height][width-1] == main.GATE_ICON:
        board[height][width] = " "
        width -= 1
        if (height, width) == gate_coords[0]:
            height = gate_coords[1][0] 
            width = gate_coords[1][1] - 1
        elif (height, width) == gate_coords[1]:
            height = gate_coords[0][0] 
            width = gate_coords[0][1] - 1
        elif (height, width) == gate_coords[2]:
            height = gate_coords[3][0] 
            width = gate_coords[3][1] - 1
        elif (height, width) == gate_coords[3]:
            height = gate_coords[2][0] 
            width = gate_coords[2][1] - 1
        elif (height, width) == gate_coords[4]:
            height = gate_coords[5][0] 
            width = gate_coords[5][1] -1 
        elif (height, width) == gate_coords[5]:
            height = gate_coords[4][0] 
            width = gate_coords[4][1] - 1
        
        board[height][width] = player

    elif move.lower() == "s" and board[height+1][width] == main.GATE_ICON:
        board[height][width] = " "
        height += 1
        if (height, width) == gate_coords[0]:
            height = gate_coords[1][0] + 1
            width = gate_coords[1][1]
        elif (height, width) == gate_coords[1]:
            height = gate_coords[0][0] - 1
            width = gate_coords[0][1]
        elif (height, width) == gate_coords[2]:
            height = gate_coords[3][0] + 1
            width = gate_coords[3][1]
        elif (height, width) == gate_coords[3]:
            height = gate_coords[2][0] - 1
            width = gate_coords[2][1]
        elif (height, width) == gate_coords[4]:
            height = gate_coords[5][0] + 1
            width = gate_coords[5][1]
        elif (height, width) == gate_coords[5]:
            height = gate_coords[4][0] - 1
            width = gate_coords[4][1]
        
        board[height][width] = player
    elif move.lower() == "d" and board[height][width +1] == main.GATE_ICON:
        board[height][width] = " "
        width += 1
        if (height, width) == gate_coords[0]:
            height = gate_coords[1][0] 
            width = gate_coords[1][1] + 1
        elif (height, width) == gate_coords[1]:
            height = gate_coords[0][0] 
            width = gate_coords[0][1] - 1
        elif (height, width) == gate_coords[2]:
            height = gate_coords[3][0] 
            width = gate_coords[3][1] - 1
        elif (height, width) == gate_coords[3]:
            height = gate_coords[2][0] 
            width = gate_coords[2][1] - 1
        elif (height, width) == gate_coords[4]:
            height = gate_coords[5][0] 
            width = gate_coords[5][1] - 1 
        elif (height, width) == gate_coords[5]:
            height = gate_coords[4][0] 
            width = gate_coords[4][1] +1
        
        board[height][width] = player
    return False

def put_enemy_on_board(board):

    enemy_coords = []

    enemy_list = [dictionaries.enemy["monster"]["icon"], dictionaries.enemy["Boss"]["icon"]]

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] in enemy_list:
                enemy_coords.append((i,j))
    gate_coords = []

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == main.GATE_ICON:
                gate_coords.append((i,j))

    

    for element in enemy_coords:
        height = element[0]
        width = element[1]

        if board[height][width] == dictionaries.enemy["monster"]["icon"]:
            enemy = dictionaries.enemy["monster"]["icon"]
        else:
            enemy = dictionaries.enemy["Boss"]["icon"]
        
        move = random.choice(["w","a","s","d"])

        if move.lower() == "w" and board[height-1][width] not in [enemy_list[0], enemy_list[1], main.WALL_ICON, main.GATE_ICON, main.GATE_TO_UPPER_LEVEL, main.GATE_TO_LOWER_LEVEL]:
            board[height][width] = " "
            height -=1
            board[height][width] = enemy
        elif move.lower() == "a" and board[height][width-1] not in [enemy_list[0], enemy_list[1], main.WALL_ICON, main.GATE_ICON, main.GATE_TO_UPPER_LEVEL, main.GATE_TO_LOWER_LEVEL]:
            board[height][width] = " "
            width -= 1
            board[height][width] = enemy
        elif move.lower() == "s" and board[height+1][width] not in [enemy_list[0], enemy_list[1], main.WALL_ICON, main.GATE_ICON, main.GATE_TO_UPPER_LEVEL, main.GATE_TO_LOWER_LEVEL]:
            board[height][width] = " "
            height += 1
            board[height][width] = enemy
        elif move.lower() == "d" and board[height][width+1] not in [enemy_list[0], enemy_list[1], main.WALL_ICON, main.GATE_ICON, main.GATE_TO_UPPER_LEVEL, main.GATE_TO_LOWER_LEVEL]:
            board[height][width] = " "
            width += 1
            board[height][width] = enemy


def put_item_on_board(board, items):
    
    for item_key in items:
        if items[item_key]:
            board[items[item_key]['position_y']][items[item_key]['position_x']] = items[item_key]['icon']
        else:
            pass

    return board

# def add_to_inventory(inventory, item_key):
#     """Add to the inventory dictionary a list of items"""


#     if item_key == 'sowrd':
        

#     elif item_key in inventory:
#         inventory[item_key] += 1
#     else:
#         inventory[item_key] = 1

def item_vs_player(item, player, items):
    inventory = []
    for item_key in item:
        if item[item_key]['position_x'] == player['position_x'] and item[item_key]['position_y'] == player['position_y']:
            inventory.append[item_key] 

            if item_key == 'sword':
                ui.print_message('\n' + ' +2 Life point! ')
                player['atack'] += 2 
            else:
                ui.print_message('\n' + item_key + ' has been added to your inventory!')

    return inventory       

def player_meets_other(others, player, board = ''):
   
    if_meet = False

    for other in others:     
            if others[other]['name'] != 'Boss':
                if others[other]["hp"] > 0:
                    if others[other]["position_y"] == player["position_y"] and (others[other]["position_x"] == player["position_x"] + 1 or others[other]["position_x"] == player["position_x"] - 1):
                        return other
                    elif others[other]["position_x"] == player["position_x"] and (others[other]["position_y"] == player["position_y"] + 1 or others[other]["position_y"] == player["position_y"] - 1):
                        return other
                    elif others[other]["position_y"] == player["position_y"] and others[other]["position_x"] == player["position_x"]:
                        return other
            

    return if_meet

def fight(player, others, other):
    
    player_x = player['position_x']
    player_y = player['position_y']
    other_x = others[other]['position_x']
    other_y = others[other]['position_y']

    if player_x == other_x and player_y == other_y:
        player_hit = (player['atack'])
        other_hit = (others[other]['atack'])

    if player_hit > other_hit:
        ui.print_message('You just won the fight with %s! +1 to power for you!' %(others[other]['name']))
        player['atack'] += 1

    elif player_hit == other_hit:
        ui.print_message('You just fought with %s! It was a draw' %(others[other]['name']))
    
    else:
        ui.print_message('You just lost fight with %s! You loose one life point' %(others[other]['name']))
        player['hp'] -= 1
       
    