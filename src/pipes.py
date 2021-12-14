import pygame, os

# Defining the assets path, the file path where all the images are stored
assets_path = os.path.join(os.path.split(os.getcwd())[0], "FlappyBird_Assets")


class PipeSet():
    def __init__(self, topY_pos, bottomY_pos, x_pos, pipe_type="green"):
        self.x_pos = x_pos

        # Importing pipe image, based on the pipe type
        if pipe_type == "green":
            pipe_image = pygame.image.load(os.path.join(assets_path, "pipe-green.png"))
        elif pipe_type == "red":
            pipe_image = pygame.image.load(os.path.join(assets_path, "pipe-red.png"))
            self._og_pos = (self.bottomY_pos + self.topY_pos)/2
            self._motion_type = 0
        self.pipe_type = pipe_type

        # Defining the pipes' images, flipping top image
        self.imageBottom = (pipe_image)
        self.imageTop = pygame.transform.flip(pipe_image, True, False)

        # Creating the Rect objects to represent the images, defining their top & bottom middle
        # positions
        self.rectBottom = self.imageBottom.get_rect()
        self.rectBottom.rect.midtop = (x_pos, topY_pos)
        self.rectTop = self.imageTop.get_rect()
        self.rectTop.rect.midbottom = (x_pos, bottomY_pos)
        
    def move_pipe(self, speedx):
        # Subtracting fromt the x value to move the pipes left
        self.rectBottom.x -= speedx
        self.rectTop.x -= speedx

        # Moving the pipes up and down
        if self.pipe_type=="red":
            speedy = 4
            if self._motion_type == 0:
                self.rectBottom.y -= speedy
                self.rectTop.y -= speedy
            elif self._motion_type == 1:
                self.rectBottom.y += speedy
                self.rectTop.y += speedy
                
            if (self.rectTop.y<self._og_pos-192):
                self._motion_type = 1
            elif (self.rectBottom.bottom>self._og_pos+192):
                self._motion_type = 0
        
    def displayPipe(self, surface):
        # Blitting the two images at the rects' coordinates
        surface.blit(self.imageBottom, self.rectBottom.topleft)
        surface.blit(self.imageTop, self.rectTop.topleft)

class Pipes():
    def __init__():
        list_pipes = []
