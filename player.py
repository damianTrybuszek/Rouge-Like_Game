class Player():
    ICON = '@'

    def __init__(self, start_x=3, start_y =3):
        self.x = start_x
        self.y = start_y

    def move_left(self):
        self.x = self.x-1
        
    def move_rigth(self):
        self.x = self.x+1
    
    def move_up(self):
        self.y = self.y-1

    def move_down(self):
        self.y = self.y+1

        
