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



            if(check == 6):
                screen.blit(quiz1.image, (100, 0))
                screen.blit(rpg, (0,0))
                rpgstudy = RPGsize.render(str(hero1.studyPoint), True, (0,0,0))
                rpgsleep = RPGsize.render(str(hero1.sleepPoint), True, (0,0,0))
                rpgsocial = RPGsize.render(str(hero1.socialPoint), True, (0,0,0))
                question = RPGsize.render(str(quiz1.health), True, (0,0,0))

                screen.blit(rpgstudy, (110, 310))
                screen.blit(rpgsocial, (380, 310))
                screen.blit(rpgsleep, (650, 310))
                screen.blit(question, (380, 100))
                pygame.display.flip()
                event = pygame.event.wait()
                if(event.type == pygame.MOUSEBUTTONDOWN):
                    if (event.type == pygame.MOUSEBUTTONDOWN and 195 <=event.pos[0] <= 302 and 365 <= event.pos[1] <=390 and hero1.studyPoint > 0):
                        quiz1.health -= 1
                        hero1.studyPoint -= 1
                        continue
                    elif( event.type == pygame.MOUSEBUTTONDOWN and 486 <=event.pos[0] <= 575 and 365 <= event.pos[1] <=390 and hero1.socialPoint >= 7):
                        quiz1.health -= 5
                        hero1.studyPoint -= 2
                        hero1.socialPoint -= 7
                        count += 1
                        continue
                    elif ( event.type == pygame.MOUSEBUTTONDOWN and 188 <=event.pos[0] <= 283 and 410 <= event.pos[1] <=435 and hero1.sleepPoint > 0 and hero1.studyPoint > 0):
                        randomInt = random.randint(0,3)
                        quiz1.health -= randomInt
                        hero1.studyPoint -= 1
                        hero1.sleepPoint -= 1
                        continue
                    elif (event.type == pygame.MOUSEBUTTONDOWN and 491 <=event.pos[0] <= 566 and 410 <= event.pos[1] <=435):
                        check = 2
                        count = 2
                        hero1.place += 1
                        continue
                if(hero1.studyPoint < 0):
                    check = 2
                    count = 0
                    hero1.place += 1
                    continue
                elif( quiz1.health < 0):
                    check = 2
                    if(count > 1):
                        hero1.cheat = 1
                        count = 0
                        hero1.place += 1
                    hero1.win += 1
                    continue
                elif(count == 2):
                    check = 2
                    count = 0
                    hero1.place += 1
                    continue
                else:
                    continue
