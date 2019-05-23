#!usr/bin/python

import pygame
#导入pygame库
from pygame.locals import *
#导入一些常用的函数和常量
from sys import *

#向sys模块借一个exit函数用来退出程序

pygame.init()
value = [48,49,50,51,52,53,54,55,56,57,58,59]
fontObj = pygame.font.Font('COPRGTL.ttf', 32)
fontObj1 = pygame.font.Font('COPRGTL.ttf', 16)
study = fontObj.render("How much do you like study?", True, (0,0,0))
party = fontObj.render("How much do you like party?", True, (0,0,0))
sleep = fontObj.render("How much do you like sleep?", True, (0,0,0))
rate = fontObj1.render("rate from 0~9", True, (0,0,0))
class scene1:
    def __init__(self, screen, hero):
        self.background = pygame.image.load("scene.jpg").convert()
        self.screen = screen
        self.hero = hero
        self.study = study.convert_alpha()

    def firstQuestion(self):
        self.screen.blit(study, (130, 150))
        #self.screen.blit(self.study, (130,150))
        self.screen.blit(rate, (320, 300))
        pass


    def secondQuestion(self):
        self.screen.blit(party, (130, 150))
        self.screen.blit(rate, (320, 300))

    def thirdQuestion(self):
        self.screen.blit(sleep, (130, 150))
        self.screen.blit(rate, (320, 300))


    def setStudy(self,thing):
        print(thing)
        for item in value:
            if thing == item:
                self.hero.studyPoint = 1+value.index(thing)
                print("study")
                print(self.hero.studyPoint)

    def setSocial(self,thing):
        print(thing)
        for item in value:
            if thing == item:
                self.hero.socialPoint = 1+value.index(thing)
                print("social")
                print(self.hero.socialPoint)

    def setSleep(self,thing):
        print(thing)
        for item in value:
            if thing == item:
                self.hero.sleepPoint = 1+value.index(thing)
                print("sleep")
                print(self.hero.sleepPoint)
