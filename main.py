#!usr/bin/python
import pygame
import time
import sys
import hero
import random
from scene1 import *
from hero import *
from pygame.locals import *
from sys import *
#from random import *
from maP import *
from study import *
from quiz import *

pygame.init();

pygame.mixer.init();
pygame.mixer.music.load("background.mp3")
pygame.mixer.music.set_volume(0.2)

bg_size = width, height = 800, 480

screen = pygame.display.set_mode(bg_size)
study1 = study(screen)


hero1 = hero(0,0,0)
quiz1 = quiz(1)
scene1 = scene1(screen,hero1)




pygame.display.set_caption("collegeMaker")
background = pygame.image.load("first.png").convert()
move = pygame.image.load("1111.png").convert_alpha()
hand = pygame.image.load("222.png").convert_alpha()
sleep = pygame.image.load("sleep.png").convert_alpha()
rpg = pygame.image.load("RPG.png").convert_alpha()

fontObj = pygame.font.Font('04b_08.ttf', 32)
choose = pygame.font.Font('04b_08.ttf', 25)
RPGsize = pygame.font.Font('04b_08.ttf', 20)
healthsize = pygame.font.Font('04b_08.ttf', 70)
newGame = fontObj.render("New game", True, (0,0,0))
exiT = fontObj.render("exit", True, (0,0,0))

clock = pygame.time.Clock();


check = 0;
count = 0;


def main():
    pygame.mixer.music.load("background.mp3")

    global check
    global count
    global clock
    global quiz1



    pygame.mixer.music.play(-1)

    while True:

        pygame.display.flip()

        if(check == 0):
            screen.blit(background, (0,0))
        #screen.blit(hero1.image, (0,0))
            screen.blit(newGame, (310,330))
            screen.blit(exiT, (310, 380))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif check == 0 and event.type == pygame.MOUSEBUTTONDOWN and 310 <=event.pos[0] <= 8*32+230 and 330 <= event.pos[1] <=362:
                check = 1;
                for i in range (225):
                    background.fill((255,255,255))
                    background.set_alpha(i)
                    screen.blit(background, (0,0))
                    pygame.display.flip()
                    pygame.time.delay(10)
                continue
            elif check == 0 and event.type == pygame.MOUSEBUTTONDOWN and 310 <=event.pos[0] <= 8*32+230 and 380 <= event.pos[1] <=412:
                pygame.quit()
                sys.exit()
            else:
                pass




        if(check == 1):
            screen.blit(scene1.background, (0,0))
            if(count == 0):

                scene1.firstQuestion()
                #pygame.time.delay(20)
            elif(count == 1):
                scene1.secondQuestion()
                #pygame.time.delay(20)
            elif(count == 2):
                scene1.thirdQuestion()
                #pygame.time.delay(20)
            event = pygame.event.wait()
            if(event.type == pygame.KEYDOWN):
                if count == 0:
                    scene1.setStudy(event.key)
                    count = count + 1
                    continue
                if count == 1:
                    scene1.setSocial(event.key)
                    count = count + 1
                    continue
                if count == 2:
                    scene1.setSleep(event.key)
                    check = 2
                    count = 0
                    continue
            #print(hero1.studyPoint)


        if(check == 2):
            print(hero1.place)
            if(hero1.place > 11):
                check = 7
                count = 0
                continue
            pygame.display.flip()
            Map = maP(screen, hero1)
            #print(hero1.place)
            Map.draw(hero1.place)
            event = pygame.event.wait()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            while( count == 1):
                background.fill((255,255,255))
                background.set_alpha(150)
                screen.blit(background, (0,0))
                wordStudy = choose.render("1. study", True, (0,0,0))
                wordSocial = choose.render("2. social", True, (0,0,0))
                wordSleep = choose.render("3. sleep", True, (0,0,0))
                screen.blit(wordStudy, (310, 190))
                screen.blit(wordSocial, (310, 235))
                screen.blit(wordSleep, (310, 280))
                pygame.display.flip()
                event = pygame.event.wait()
                if(event.type == pygame.KEYDOWN):
                    if(event.key == K_1):
                        check = 3
                        count = 0
                        #print(check)
                        screen.fill((255,255,255))
                        start_tick = pygame.time.get_ticks()
                        continue
                    if(event.key == K_2):
                        check = 4
                        count = 0
                        screen.fill((255,255,255))
                        start_tick = pygame.time.get_ticks()
                        continue
                    if(event.key == K_3):
                        check = 5
                        count = 0
                        screen.fill((255,255,255))
                        #start_tick = pygame.time.get_ticks()
                        continue
                else:
                    pass
            #event = pygame.event.wait()
            if(event.type == pygame.KEYDOWN):
                if( event.key == K_SPACE):
                    if(hero1.place == 3):
                        check = 6
                        count = 0
                        quiz1 = quiz(1)
                        pygame.mixer.music.load("boss.mp3")
                        pygame.mixer.music.play(-1)
                        continue
                    if(hero1.place == 7):
                        check = 6
                        count = 0
                        quiz1 = quiz(2)
                        pygame.mixer.music.load("boss.mp3")
                        pygame.mixer.music.play(-1)
                        continue
                    if(hero1.place == 11):
                        check = 6
                        count = 0
                        quiz1 = quiz(3)
                        pygame.mixer.music.load("boss.mp3")
                        pygame.mixer.music.play(-1)
                        continue
                count = 1
                continue
            else:
                pass


        if( check == 3):

            second = (pygame.time.get_ticks()-start_tick)/1000
            #print(second)
            if(second >= 15):
                check = 2
                count = 0
                hero1.place += 1
                if(hero1.studyPoint < 10):
                    hero1.studyPoint += 1
                if(hero1.socialPoint > 0 and hero1.sleepPoint > 0):
                    hero1.socialPoint -= 1
                    hero1.sleepPoint -= 1
                continue
            pygame.display.flip()
            screen.fill((255,255,255))
            position = move.get_rect().move(290,150)
            screen.blit(move, position)
            screen.blit(hand, (650-(count*2.5),180))
            if(650-(count*2.5) < 400):
                print(count)
                check = 2
                count = 0
                hero1.place += 1
                if(hero1.studyPoint < 10):
                    hero1.studyPoint += 3
                if(hero1.socialPoint > 0 and hero1.sleepPoint > 0):
                    hero1.socialPoint -= 1
                    hero1.sleepPoint -= 1
                screen.fill((255,255,255))
                continue
            pygame.time.delay(100)
            event = pygame.event.poll()
            if(event.type == pygame.KEYDOWN):
                if(event.key == K_SPACE):
                    screen.fill((255,255,255))
                    screen.blit(move, position)
                    screen.blit(hand, (650-(count*2)+count*0.2,180))
                    count -= 0.8
                    continue
                else:
                    pass
            else:
                count += 1
            continue

        if( check == 4):

            second = (pygame.time.get_ticks()-start_tick)/1000
            #print(second)
            if(second >= 15):
                check = 2
                count = 0
                hero1.place += 1
                if(hero1.socialPoint < 10):
                    hero1.socialPoint += 1
                if(hero1.studyPoint > 0 and hero1.sleepPoint > 0):
                    hero1.studyPoint -= 1
                    hero1.sleepPoint -= 1
                continue
            pygame.display.flip()
            screen.fill((255,255,255))
            position = move.get_rect().move(290,150)
            screen.blit(move, position)
            screen.blit(hand, (380+(count*2.5),180))
            if(380+(count*2.5) > 800):
                print(count)
                check = 2
                count = 0
                hero1.place += 1
                if(hero1.socialPoint < 10):
                    hero1.socialPoint += 3
                if(hero1.studyPoint > 0 and hero1.sleepPoint > 0):
                    hero1.studyPoint -= 1
                    hero1.sleepPoint -= 1
                screen.fill((255,255,255))
                continue
            pygame.time.delay(100)
            event = pygame.event.poll()
            if(event.type == pygame.KEYDOWN):
                if(event.key == K_SPACE):
                    screen.fill((255,255,255))
                    screen.blit(move, position)
                    screen.blit(hand, (380+(count*2.5)-count*0.2,180))
                    count += 2
                    continue
                else:
                    pass
            else:
                if(count > 1):
                    count -= 0.5
                else:
                    count = 0
            continue

        if(check == 5):
            YN = fontObj.render("Y / N", True, (0,0,0))
            screen.fill((255,255,255))
            #screen.blit(background, (0,0))
            screen.blit(sleep, (30, 290))
            screen.blit(YN, (380, 200))
            pygame.display.flip()
            event = pygame.event.wait()
            if(event.type == pygame.KEYDOWN):
                if(event.key == K_n):
                    screen.fill((255,255,255))
                    #screen.blit(background, (0,0))
                    time = pygame.image.load("china.png").convert_alpha()
                    screen.blit(time, (30,290))
                    pygame.display.flip()
                    pygame.time.delay(4000)
                else:
                    pass
                for i in range (225):
                    background.fill((0,0,0))
                    background.set_alpha(i)
                    screen.blit(background, (0,0))
                    pygame.display.flip()
                    pygame.time.delay(10)
                check = 2
                count = 0
                hero1.place += 1
                if(hero1.sleepPoint < 10):
                    hero1.sleepPoint += 2
                if(hero1.studyPoint > 0 and hero1.socialPoint > 0):
                    hero1.studyPoint -= 1
                    hero1.socialPoint -= 1
            continue

        if(check == 6):

            screen.fill((255,255,255))
            screen.blit(quiz1.image, (100, 0))
            screen.blit(rpg, (0,0))
            rpgstudy = RPGsize.render(str(hero1.studyPoint), True, (0,0,0))
            rpgsleep = RPGsize.render(str(hero1.sleepPoint), True, (0,0,0))
            rpgsocial = RPGsize.render(str(hero1.socialPoint), True, (0,0,0))
            question = healthsize.render(str(quiz1.health), True, (255,100,110))

            screen.blit(rpgstudy, (110, 310))
            screen.blit(rpgsocial, (380, 310))
            screen.blit(rpgsleep, (650, 310))
            screen.blit(question, (380, 70))
            pygame.display.flip()
            event = pygame.event.wait()
            if (event.type == QUIT):
                pygame.quit()
                sys.exit()
            elif (event.type == pygame.MOUSEBUTTONDOWN and 195 <=event.pos[0] <= 302 and 365 <= event.pos[1] <=390 and hero1.studyPoint > 0):
                quiz1.health -= 1
                hero1.studyPoint -= 1
                continue
            elif (event.type == pygame.MOUSEBUTTONDOWN and 486 <=event.pos[0] <= 575 and 365 <= event.pos[1] <=390 and hero1.socialPoint >= 7):
                quiz1.health -= 5
                hero1.studyPoint -= 2
                hero1.socialPoint -= 7
                count += 1
                continue
            elif (event.type == pygame.MOUSEBUTTONDOWN and 188 <=event.pos[0] <= 283 and 410 <= event.pos[1] <=435 and hero1.sleepPoint > 0 and hero1.studyPoint > 0):
                randomInt = random.randint(0,3)
                quiz1.health -= randomInt
                hero1.studyPoint -= 1
                hero1.sleepPoint -= 1
                continue
            elif (event.type == pygame.MOUSEBUTTONDOWN and 491 <=event.pos[0] <= 566 and 410 <= event.pos[1] <=435):
                check = 2
                count = 0
                hero1.place += 1
                pygame.mixer.music.load("background.mp3")
                pygame.mixer.music.play(-1)
                continue
            if(hero1.studyPoint <= 0):
                check = 2
                count = 0
                hero1.place += 1
                pygame.mixer.music.load("background.mp3")
                pygame.mixer.music.play(-1)
                continue
            elif( quiz1.health <= 0):
                check = 2
                if(count > 1):
                    hero1.cheat = 1
                pygame.mixer.music.load("background.mp3")
                pygame.mixer.music.play(-1)
                count = 0
                hero1.place += 1
                hero1.win += 1
                continue
            #elif(count == 2):
            #    check = 2
                #count = 0
                #hero1.place += 1
                #pygame.mixer.music.load("background.mp3")
                #pygame.mixer.music.play(-1)
                #continue
            else:
                pass

        if(check == 7):
            screen.fill((0,0,0))
            if(hero1.win == 3):
                winP = pygame.image.load("win.jpg").convert()
                screen.blit(winP, (0,0))
            elif( hero1.cheat == 1):
                cheatP = pygame.image.load("CHEAT.jpg").convert()
                screen.blit(cheatP, (0,0))
            else:
                loseP = pygame.image.load("LOSE.jpg").convert()
                screen.blit(loseP, (0,0))
                pygame.display.flip()
                event = pygame.event.wait()
            if( event.type == QUIT):
                pygame.quit()
                sys.exit()
            break




            #print("done")







        pygame.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()
