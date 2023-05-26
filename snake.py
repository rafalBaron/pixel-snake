import pygame
from CONST import *

class Snake(pygame.Rect):

    def __init__(self):
        self.x = int(SCREEN_SIZE[0]/2)
        self.y = int(SCREEN_SIZE[1]/2)
        self.h = 35
        self.w = 35
