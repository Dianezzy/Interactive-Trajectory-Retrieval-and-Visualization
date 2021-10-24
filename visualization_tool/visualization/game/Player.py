class Player():
    def __init__(self, player, jersey, color):
        self.id = int(player[0])
        self.x = float(player[1])
        self.y = float(50 - player[2])
        self.jersey = int(jersey)
        self.color = color

    
    def update_position(self, position):
        self.x = float(position[0])
        self.y = float(50 - position[1])
    

    def get_id(self):
        return self.id
    

