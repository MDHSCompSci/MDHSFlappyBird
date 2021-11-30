class PipeSet():
    def __init__(self,topY_pos, bottomY_pos, x_pos, screen):
        self.screen = screen
        self.topY_pos = topY_pos
        self.bottomY_pos = bottomY_pos
        self.x_pos = x_pos

class Pipes():
    def __init__(self,screen):
        self.screen = screen
        list_pipes = []
