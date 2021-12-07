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
        
    def move(self, dis):
        # Subtracting fromt the x value to move the pipes left
        self.rectBottom.x -= dis
        self.rectTop.x -= dis
        
    def displayPipe(self, surface):
        # Blitting the two images at the rects' coordinates
        surface.blit(self.imageBottom, self.rectBottom.topleft)
        surface.blit(self.imageTop, self.rectTop.topleft)

class Pipes():
    def __init__():
        list_pipes = []
