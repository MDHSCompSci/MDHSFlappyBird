import pygame

class PipeSet():
    def __init__(self, topY_pos, bottomY_pos, x_pos):
        self.x_pos = x_pos

        #Defining the image :)

        self.rectBottom = self.imageBottom.get_rect()
        self.rectBottom.rect.midtop = (x_pos, topY_pos)
        self.rectTop = self.imageTop.get_rect()
        self.rectTop.rect.midbottom = (x_pos, bottomY_pos)
        
    def moveLeft(self, dis):
        self.rectBottom.x -= dis
        self.rectTop.x -= dis

class Pipes():
    def __init__():
        list_pipes = []
