

class Bird():

    downflap = None
    upflap = None
    midflap = None
    bird_frames = []

    def __init__(self, screen):
        bird_img = None
        current_frame = None
        self.centerx_pos = None
        self.centery_pos = None
        pass
    
    def getX(self):
        return self.centerx_pos
    
    def getY(self):
        return self.centery_pos
