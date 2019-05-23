#!usr/bin/python
import pygame
import sys
import hero
#import random
from hero import *
from pygame.locals import *
from sys import *
#from random import *

pygame.init()

fontObj = pygame.font.Font('04b_08.ttf', 15)




count = 1
count1 = 1
count2 = 1
count3 = 1
count4 = 1

class maP:
    def __init__(self, screen,hero):
        self.background = pygame.image.load("first.png").convert()
        self.screen = screen
        self.hero = hero
        self.study = fontObj.render("studyPoint: " + str(hero.studyPoint), True, (0,0,0))
        self.sleep = fontObj.render("sleepPoint: "+str(hero.sleepPoint), True, (0,0,0))
        self.social = fontObj.render("socialPoint: "+str(hero.socialPoint), True, (0,0,0))
        self.change = pygame.transform.scale(self.hero.image, (20,20))
        self.place = 1

    def draw(self,x):
        global count
        global count1
        global count2
        global count3
        global count4
        self.screen.blit(self.background, (0,0))
        if(x==0):
            position= self.change.get_rect().move(56,340)
        elif(x == 3):
            position = self.change.get_rect().move(56+170,340)
        elif(x == 7):
            position = self.change.get_rect().move(466,340)
        elif(x ==4):
            position = self.change.get_rect().move(56+count1*240, 340)
        elif( x == 8):
            position = self.change.get_rect().move(536, 340)
        elif(x == 5 ):
            position = self.change.get_rect().move(56+1*290,340)
            #count2 += 1
        elif(x == 9):
            position = self.change.get_rect().move(586,340)
            #count2 += 1
        elif(x == 6):
            position = self.change.get_rect().move(396,340)
            count3 += 1
        elif( x == 10):
            position = self.change.get_rect().move(636,340)
            count3 += 1
        elif( x == 11):
            position = self.change.get_rect().move(706,340)
            count3 += 1
        else:
            position = self.change.get_rect().move(56+x*50,340)

        self.screen.blit(self.study, (100, 100))
        self.screen.blit(self.sleep, (100, 150))
        self.screen.blit(self.social, (100, 200))
        rec1 = pygame.draw.circle(self.screen, (0,0,0), [66, 350], 20, 1)
        line1 = pygame.draw.line(self.screen,(0,0,0),[86, 350], [96, 350])
        rec2 = pygame.draw.circle(self.screen, (0,0,0), [116, 350], 20, 1)
        line2 = pygame.draw.line(self.screen,(0,0,0),[136, 350], [146, 350])
        rec3 = pygame.draw.circle(self.screen, (0,0,0), [166, 350], 20, 1)
        line3 = pygame.draw.line(self.screen,(0,0,0),[186, 350], [196, 350])
        rec4 = pygame.draw.circle(self.screen, (0,0,0), [236, 350], 40, 0)
        line4 = pygame.draw.line(self.screen,(0,0,0),[276, 350], [286, 350])
        rec5 = pygame.draw.circle(self.screen, (0,0,0), [306, 350], 20, 1)
        line5 = pygame.draw.line(self.screen,(0,0,0),[326, 350], [336, 350])
        rec6 = pygame.draw.circle(self.screen, (0,0,0), [356, 350], 20, 1)
        line6 = pygame.draw.line(self.screen,(0,0,0),[376, 350], [386, 350])
        rec7 = pygame.draw.circle(self.screen, (0,0,0), [406, 350], 20, 1)
        line7 = pygame.draw.line(self.screen,(0,0,0),[426, 350], [436, 350])
        rec8 = pygame.draw.circle(self.screen, (0,0,0), [476, 350], 40, 0)
        line8 = pygame.draw.line(self.screen,(0,0,0),[516, 350], [526, 350])
        rec9 = pygame.draw.circle(self.screen, (0,0,0), [546, 350], 20, 1)
        line9 = pygame.draw.line(self.screen,(0,0,0),[566, 350], [576, 350])
        rec10 = pygame.draw.circle(self.screen, (0,0,0), [596, 350], 20, 1)
        line10 = pygame.draw.line(self.screen,(0,0,0),[616, 350], [626, 350])
        rec11 = pygame.draw.circle(self.screen, (0,0,0), [646, 350], 20, 1)
        line11 = pygame.draw.line(self.screen,(0,0,0),[666, 350], [676, 350])
        rec12 = pygame.draw.circle(self.screen, (0,0,0), [716, 350], 40, 0)
        self.screen.blit(self.change, position)
        pygame.display.flip()

    def updateHero(self,x):

        self.screen.blit(self.background, (0,0))
        if(x == 3):
            position = self.change.get_rect().move(56+170,340)
        elif(x == 7):
            position = self.change.get_rect().move(456,340)
        elif(x == 11):
            position = self.change.get_rect().move(686, 340)
        elif(x ==4):
            position = self.change.get_rect().move(56+count1*240, 340)
        elif( x == 8):
            position = self.change.get_rect().move(546, 340)
        elif(x == 5 or x== 9):
            position = self.change.get_rect().move(56+count2*290,340)
            count2 += 1
        elif(x == 6 or x == 10):
            position = self.change.get_rect().move(56+count3*336,340)
            count3 += 1
        else:
            position = self.change.get_rect().move(56+x*50,340)
        self.screen.blit(self.study, (100, 100))
        self.screen.blit(self.sleep, (100, 150))
        self.screen.blit(self.social, (100, 200))
        rec1 = pygame.draw.circle(self.screen, (0,0,0), [66, 350], 20, 1)
        line1 = pygame.draw.line(self.screen,(0,0,0),[86, 350], [96, 350])
        rec2 = pygame.draw.circle(self.screen, (0,0,0), [116, 350], 20, 1)
        line2 = pygame.draw.line(self.screen,(0,0,0),[136, 350], [146, 350])
        rec3 = pygame.draw.circle(self.screen, (0,0,0), [166, 350], 20, 1)
        line3 = pygame.draw.line(self.screen,(0,0,0),[186, 350], [196, 350])
        rec4 = pygame.draw.circle(self.screen, (0,0,0), [236, 350], 40, 0)
        line4 = pygame.draw.line(self.screen,(0,0,0),[276, 350], [286, 350])
        rec5 = pygame.draw.circle(self.screen, (0,0,0), [306, 350], 20, 1)
        line5 = pygame.draw.line(self.screen,(0,0,0),[326, 350], [336, 350])
        rec6 = pygame.draw.circle(self.screen, (0,0,0), [356, 350], 20, 1)
        line6 = pygame.draw.line(self.screen,(0,0,0),[376, 350], [386, 350])
        rec7 = pygame.draw.circle(self.screen, (0,0,0), [406, 350], 20, 1)
        line7 = pygame.draw.line(self.screen,(0,0,0),[426, 350], [436, 350])
        rec8 = pygame.draw.circle(self.screen, (0,0,0), [476, 350], 40, 0)
        line8 = pygame.draw.line(self.screen,(0,0,0),[516, 350], [526, 350])
        rec9 = pygame.draw.circle(self.screen, (0,0,0), [546, 350], 20, 1)
        line9 = pygame.draw.line(self.screen,(0,0,0),[566, 350], [576, 350])
        rec10 = pygame.draw.circle(self.screen, (0,0,0), [596, 350], 20, 1)
        line10 = pygame.draw.line(self.screen,(0,0,0),[616, 350], [626, 350])
        rec11 = pygame.draw.circle(self.screen, (0,0,0), [646, 350], 20, 1)
        line11 = pygame.draw.line(self.screen,(0,0,0),[666, 350], [676, 350])
        rec12 = pygame.draw.circle(self.screen, (0,0,0), [716, 350], 40, 0)
        self.screen.blit(self.change, position)
        pygame.display.flip()
