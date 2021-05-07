import main
import random
import ui
import math
import dictionaries

item_list = [dictionaries.items["shield"]["icon"], dictionaries.items["sword"]["icon"], dictionaries.items["armor"]["icon"]]
enemy_list = [dictionaries.enemy["monster"]["icon"], dictionaries.enemy["ghost"]["icon"], dictionaries.enemy["boss"]["icon"]]
enemy_list_without_boss = [dictionaries.enemy["monster"]["icon"], dictionaries.enemy["ghost"]["icon"]]


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
            elif i == height - 4 and j == width -6:
                board[i][j] = random.choice(item_list)
            elif i == 0 or i == height -1:
                board[i][j]=main.WALL_ICON

    for i in range(height+2):
        for j in range(width-4):
            if i == 5 and j == width- 4 -1:
                board[i][j+30]=main.GATE_ICON
            elif i == 4 and j == 0:
                board[i][j+30]=main.GATE_ICON
            elif i == height - 2 and j == width - 9:
                board[i][j+30]=random.choice(enemy_list_without_boss)
            elif i == height - 4 and j == width - 12:
                board[i][j+30]=item_list[0]  
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
            elif (i == height - 6 and j == 3) or (i == height - 7 and j == width-3):
                board[i+17][j+34] = random.choice(enemy_list_without_boss)

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
            elif i == height//3 and j == (width- 4)/4:
                board[i+20][j+10]=random.choice(enemy_list_without_boss)
            elif i == height - 3 and j == width - 8:
                board[i+20][j+10]=random.choice(item_list)  

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
            if board[i][j] == player["icon"]:
                height = i
                width = j
                break
    
    gate_coords = []

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == main.GATE_ICON:
                gate_coords.append((i,j))

    if move.lower() == "w" and board[height-1][width] in item_list:
        board[height][width] = " "
        height -=1
        item = board[height][width]
        board[height][width] = player["icon"]
        return item
    elif move.lower() == "a" and board[height][width-1] in item_list:
        board[height][width] = " "
        width -= 1
        item = board[height][width]
        board[height][width] = player["icon"]
        return item
    elif move.lower() == "s" and board[height+1][width] in item_list:
        board[height][width] = " "
        height += 1
        item = board[height][width]
        board[height][width] = player["icon"]
        return item
    elif move.lower() == "d" and board[height][width+1] in item_list:
        board[height][width] = " "
        width += 1
        item = board[height][width]
        board[height][width] = player["icon"]
        return item


    if move.lower() == "w" and board[height-1][width] == " ":
        board[height][width] = " "
        height -=1
        board[height][width] = player["icon"]
    elif move.lower() == "a" and board[height][width-1] == " ":
        board[height][width] = " "
        width -= 1
        board[height][width] = player["icon"]
    elif move.lower() == "s" and board[height+1][width] == " ":
        board[height][width] = " "
        height += 1
        board[height][width] = player["icon"]
    elif move.lower() == "d" and board[height][width+1] == " ":
        board[height][width] = " "
        width += 1
        board[height][width] = player["icon"]

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
        
        board[height][width] = player["icon"]


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
        
        board[height][width] = player["icon"]

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
        
        board[height][width] = player["icon"]
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
        
        board[height][width] = player["icon"]
        
    return False

def put_enemy_on_board(board, player):

    enemy_coords = []

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] in enemy_list:
                enemy_coords.append((i,j))
    gate_coords = []

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == main.GATE_ICON:
                gate_coords.append((i,j))

    collision_list = [main.WALL_ICON, main.GATE_ICON, main.GATE_TO_UPPER_LEVEL, main.GATE_TO_LOWER_LEVEL, player["icon"], dictionaries.items["shield"]["icon"], dictionaries.items["sword"]["icon"], dictionaries.items["armor"]["icon"]]

    for element in enemy_coords:
        height = element[0]
        width = element[1]

        if board[height][width] == dictionaries.enemy["monster"]["icon"]:
            enemy = dictionaries.enemy["monster"]["icon"]
        elif board[height][width] == dictionaries.enemy["ghost"]["icon"]:
            enemy = dictionaries.enemy["ghost"]["icon"]
        else:
            enemy = dictionaries.enemy["boss"]["icon"]
        
        while True:
        
            move = random.choice(["w","a","s","d"])

            if move.lower() == "w" and board[height-1][width] not in collision_list and board[height-1][width] not in enemy_list:
                board[height][width] = " "
                height -=1
                board[height][width] = enemy
                break
            elif move.lower() == "a" and board[height][width-1] not in collision_list and board[height][width-1] not in enemy_list:
                board[height][width] = " "
                width -= 1
                board[height][width] = enemy
                break
            elif move.lower() == "s" and board[height+1][width] not in collision_list and board[height+1][width] not in enemy_list:
                board[height][width] = " "
                height += 1
                board[height][width] = enemy
                break
            elif move.lower() == "d" and board[height][width+1] not in collision_list and  board[height][width+1] not in enemy_list:
                board[height][width] = " "
                width += 1
                board[height][width] = enemy
                break


# def put_item_on_board(board, items):
    
#     for item_key in items:
#         if items[item_key]:
#             board[items[item_key]['position_y']][items[item_key]['position_x']] = items[item_key]['icon']
#         else:
#             pass

#     return board

def add_to_inventory(inventory, item, properties):
    """Add to the inventory dictionary a list of items"""
    inventory[item] = properties

# def item_vs_player(inventory, items, player):    
#     for item, properties in items.items():
#         if properties['position_x'] == player['position_x'] and properties['position_y'] == player['position_y']:
#             add_to_inventory(inventory, item, properties)
#             add_stats_to_player(player, properties)

def item_vs_player(inventory, items, player, parameter):    
    for item, properties in items.items():
        if parameter == properties["icon"]:
            add_to_inventory(inventory, item, properties)
            add_stats_to_player(player, properties)

def add_stats_to_player(player, properties):
    player["hp"] += properties.get("hp",0)
    player["attack"] += properties.get("attack", 0)
    player["defense"] += properties.get("defense", 0)