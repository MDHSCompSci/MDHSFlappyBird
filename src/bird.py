import pygame, os

class Bird():
    # Getting the target path for all the assets
    assets_path = os.path.join(os.path.split(os.getcwd())[0], "FlappyBird_Assets")
    
    # Setting the various animation frames
    frames = {0: pygame.image.load(os.path.join(assets_path, "yellowbird-downflap.png")),
              1: pygame.image.load(os.path.join(assets_path, "yellowbird-midflap.png")),
              2: pygame.image.load(os.path.join(assets_path, "yellowbird-downflap.png"))}
    
    def __init__(self, screen):
        
        # Setting the frame counter
        self.frame = 0
        # Ignore this, determines if the bird is flapping up or down, aka
        # which way to cycle through the frames
        self._animation_cycle = 1

        # Creating the Bird Rect object: (pos, size)
        self.rect = pygame.rect.Rect((0, 0), (34, 24))
        

    def getX(self):
        return self.rect.centerx
    
    def getY(self):
        return self.centery_pos

    def switch_frame(self):
        if self.frame <= 0:
            self._animation_cycle = abs(self._animation_cycle)
        elif self.frame >= (len(self.frames)):
            self._animation_cycle = -abs(self._animation_cycle)
            
        self.frame += self._animation_cycle

