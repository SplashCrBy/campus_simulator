
import pygame
#导入pygame库
from pygame.locals import *
#导入一些常用的函数和常量
from sys import *

class quiz:
    def __init__(self, count):
        if(count == 1):
            self.image = pygame.image.load("010_7015.png").convert_alpha()
            self.health = 5
        elif( count == 2):
            self.image = pygame.image.load("015_25944.png").convert_alpha()
            self.health = 10
        elif( count == 3):
            self.image = pygame.image.load("019_20676.png").convert_alpha()
            self.health = 15
