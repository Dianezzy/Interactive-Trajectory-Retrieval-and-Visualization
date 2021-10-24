class Ball():
    def __init__(self, ball):
        self.x = float(ball[0])
        self.y = float(50 - ball[1])
        self.radius = float(ball[2])
        self.color = '#ff8c00'  
    
    
    def update_position(self, position):
        self.x = float(position[0])
        self.y = float(50 - position[1])
        self.radius = float(position[2])