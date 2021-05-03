def display_board(board):
    print("The Best Rouge Game in the World!\n\n")
    for row in board:
        for cell in row:
            print(cell, end=' ')
        print()
    print()
    
