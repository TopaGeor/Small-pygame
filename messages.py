import pygame
import sys
import time

from pygame.locals import *
pygame.init()

HOR = 600
VER = 400
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 225)
red = (255, 0, 0)


def message1(surf, font):
    string1 = 'Use D to move Right'
    string2 = 'Use W or Space to jump'
    string3 = 'Use A to move Left '
    text1 = font.render(string1, True, black, white)
    text2 = font.render(string2, True, black, white)
    text3 = font.render(string3, True, black, white)
    surf.blit(text1, (100, 20))
    surf.blit(text2, (100, 52))
    surf.blit(text3, (100, 84))
    pygame.display.update()


def message2(surf, font):
    string1 = 'You have only range attacks'
    string2 = 'Use M1 for normal attack'
    string3 = 'Use M3 for special attack'
    text1 = font.render(string1, True, black, white)
    text2 = font.render(string2, True, black, white)
    text3 = font.render(string3, True, black, white)
    surf.blit(text1, (100, 20))
    surf.blit(text2, (100, 52))
    surf.blit(text3, (100, 84))
    pygame.display.update()


def message3(surf, font):
    string1 = 'Wait  this is an enemy            '
    string2 = 'You have to destroy him      '
    string3 = 'Press space to continue      '
    text1 = font.render(string1, True, black, white)
    text2 = font.render(string2, True, black, white)
    text3 = font.render(string3, True, black, white)
    surf.blit(text1, (100, 20))
    surf.blit(text2, (100, 52))
    surf.blit(text3, (100, 84))
    pygame.display.update()
    ready = True
    while ready:
        for ev in pygame.event.get():
            if ev.type == QUIT:
                pygame.quit()
                sys.exit()

            elif (ev.type == KEYDOWN):
                if ev.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if (ev.key == K_SPACE):
                    ready = False


def message4(surf, font):
    string1 = 'Your life is on top left corner'
    string2 = 'The enemy life is on top right corner'
    string3 = 'Press space to continue     '
    text1 = font.render(string1, True, black, white)
    text2 = font.render(string2, True, black, white)
    text3 = font.render(string3, True, black, white)
    surf.blit(text1, (100, 20))
    surf.blit(text2, (100, 52))
    surf.blit(text3, (100, 84))
    pygame.display.update()
    ready = True
    while ready:
        for ev in pygame.event.get():
            if ev.type == QUIT:
                pygame.quit()
                sys.exit()

            elif (ev.type == KEYDOWN):
                if ev.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if (ev.key == K_SPACE):
                    ready = False


def message5(surf, font):
    string1 = 'Win by bring the enemy life to zero'
    string2 = 'If your life reach to zero you will lose'
    string3 = 'Press space to continue'
    text1 = font.render(string1, True, black, white)
    text2 = font.render(string2, True, black, white)
    text3 = font.render(string3, True, black, white)
    surf.blit(text1, (100, 20))
    surf.blit(text2, (100, 52))
    surf.blit(text3, (100, 84))
    pygame.display.update()
    ready = True
    while ready:
        for ev in pygame.event.get():
            if ev.type == QUIT:
                pygame.quit()
                sys.exit()

            elif (ev.type == KEYDOWN):
                if ev.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if (ev.key == K_SPACE):
                    ready = False


def message6(surf, font):
    string1 = 'Your normal attack has no benefits'
    string2 = 'Your special attack is a CO_2 ball        '
    string3 = 'You fight a product of CH_4'
    string4 = 'Press space to start the fight'
    text1 = font.render(string1, True, black, white)
    text2 = font.render(string2, True, black, white)
    text3 = font.render(string3, True, black, white)
    text4 = font.render(string4, True, black, white)
    surf.blit(text1, (100, 20))
    surf.blit(text2, (100, 52))
    surf.blit(text3, (100, 84))
    surf.blit(text4, (100, 116))
    pygame.display.update()
    ready = True
    while ready:
        for ev in pygame.event.get():
            if ev.type == QUIT:
                pygame.quit()
                sys.exit()

            elif (ev.type == KEYDOWN):
                if ev.type == K_ESCAPE:
                    pygame.quit()
                    sys.exit
                elif (ev.key == K_SPACE):
                    ready = False
                    string4 = 52 * ' '
                    text4 = font.render(string4, True, black, white)
                    surf.blit(text4, (100, 116))


def heal(surf, font, heal1, heal2):
    text1 = font.render(str(heal1).zfill(3), True, black, blue)
    text2 = font.render(str(heal2).zfill(3), True, black, red)
    surf.blit(text1, (0, 0))
    surf.blit(text2, (560, 0))


def victory(surf, font):
    string = 'YOU WIN'
    text = font.render(string, True, black, white)
    surf.blit(text, (200, 120))
    pygame.display.update()
    ready = True
    while ready:
        for ev in pygame.event.get():
            if ev.type == QUIT:
                pygame.quit()
                sys.exit()

            elif (ev.type == KEYDOWN):
                if ev.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if (ev.key == K_SPACE):
                    ready = False


def defeat(surf, font):
    string = 'YOU LOOSE'
    text = font.render(string, True, black, white)
    surf.blit(text, (200, 120))
    pygame.display.update()
    ready = True
    while ready:
        for ev in pygame.event.get():
            if ev.type == QUIT:
                pygame.quit()
                sys.exit()

            elif (ev.type == KEYDOWN):
                if ev.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if (ev.key == K_SPACE):
                    ready = False
