#!usr/bin/python

import pygame
#导入pygame库
from pygame.locals import *
#导入一些常用的函数和常量
from sys import *
#向sys模块借一个exit函数用来退出程序

class hero:
    def __init__(self, study, sleep, social):
        self.image = pygame.image.load("fugu.png").convert()
        self.studyPoint = study
        self.sleepPoint = sleep
        self.socialPoint = social
        self.place = 0
        self.win = 0
        self.cheat = 0

    def dothings(self):
        print(123)
