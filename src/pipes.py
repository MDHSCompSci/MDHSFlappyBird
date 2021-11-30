import pygame

class PipeSet():
    def __init__(self, topY_pos, bottomY_pos, x_pos):
        self.x_pos = x_pos

        # Defining the assets path
        assets_path = os.path.join(os.path.split(os.getcwd())[0], "FlappyBird_Assets")

        # Importing pipe image
        pipe_image = pygame.image.load(os.path.join(assets_path, "pipe-green.png"))

        # Defining the pipes' images, flipping top image
        self.imageBottom = (pipe_image)
        self.imageTop = pygame.transform.flip(pipe_image, True, False)

        # Creating the Rect objects to represent the images, defining their top & bottom middle
        # positions
        self.rectBottom = self.imageBottom.get_rect()
        self.rectBottom.rect.midtop = (x_pos, topY_pos)
        self.rectTop = self.imageTop.get_rect()
        self.rectTop.rect.midbottom = (x_pos, bottomY_pos)
        
    def moveLeft(self, dis):
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
