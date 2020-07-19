import pygame
import sys

from pygame.locals import *

pygame.mixer.init()
pygame.init()

background = pygame.mixer.Sound('background.wav')  # sound by Setunima
victory = pygame.mixer.Sound('victory.wav')  # sound by grunz
defeat = pygame.mixer.Sound('defeat.wav')  # sound by spazzo_1493
jump = pygame.mixer.Sound('jump.wav')  # sound by CG
fall = pygame.mixer.Sound('fall.wav')  # sound by CG


def PlayMusic(font, black, my_screen):
    white = (255, 255, 255)
    string1 = 'Sounds from Freesound.org'
    string2 = 'By: Seunima,CG,spazzo_1493,CGEffex,grunz'
    string3 = 'I have no rights on the songs'
    string4 = 'Press Space to star the game'
    text1 = font.render(string1, True, black, white)
    text2 = font.render(string2, True, black, white)
    text3 = font.render(string3, True, black, white)
    text4 = font.render(string4, True, black, white)
    my_screen.blit(text1, (100, 20))
    my_screen.blit(text2, (100, 52))
    my_screen.blit(text3, (100, 84))
    my_screen.blit(text4, (100, 116))
    pygame.display.update()
    background.play(-1)  # play song
    background.set_volume(1)
    ready = True
    while ready:  # give to composer a gredit
        for ev in pygame.event.get():
            if ev.type == QUIT:
                pygame.quit()
                sys.exit()

            elif ev.type == KEYDOWN:
                if ev.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                elif ev.key == K_SPACE:
                    ready = False


def Jump():
    jump.play()
    jump.set_volume(1)


def Fall():
    fall.play()
    fall.set_volume(1)


def VictoryMusic():
    victory.play()
    victory.set_volume(1)


def DefeatMusic():
    defeat.play()
    defeat.set_volume(1)
