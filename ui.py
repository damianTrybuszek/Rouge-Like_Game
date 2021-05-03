def display_board(board, current_level):
    print("The Best Rouge Game in the World!\n")
    print(f"Current level: {current_level}.\n")
    for row in board:
        for cell in row:
            print(cell, end=' ')
        print()
    print()
    
