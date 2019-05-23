
import pygame
#导入pygame库
from pygame.locals import *
#导入一些常用的函数和常量
from sys import *

pygame.init()

class study:
    def __init__(self, screen):
        self.background = pygame.image.load("scene.jpg")
        self.image = pygame.image.load("fugu.png")

        self.screen = screen
        self.count = 0
        self.locationX = 780

    def run(self):
        i = 780
        self.screen.blit(self.background,(0,0))
        self.screen.blit(self.image, (300,200))
        event = pygame.event.poll()

        if(event.type == pygame.KEYDOWN):
            if( event.key == K_a or event.key == K_s):
                self.count += 1
        if(self.count == 20):
            return 1
