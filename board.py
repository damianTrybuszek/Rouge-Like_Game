class Board():
    WALL_ICON = '#'
    FLOOR_ICON = '.'
    def __init__(self, width, height, gate):
        self.width = width
        self.height = height
        self.gate = gate

    def place_player(self, player):
        self.player = player
        
    def move_player(self, move_input):
        if move_input == "a":
            self.player.move_left()
        elif move_input == "d":
            self.player.move_rigth()
        elif move_input == "w":
            self.player.move_up()
        elif move_input == "s":
            self.player.move_down()
        else:
            print("WRONG KEY YOU FAGGOT")
        
    
#w klasie board trzymac next board