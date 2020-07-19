# Python Libraries
import pygame
import sys
import time
import random

# My Libraries
import music
import characters as ch
import attacks
import messages

from pygame.locals import *
from pygame.sprite import *
from random import randint

pygame.init()
Done1 = Done2 = Done3 = Done4 = Done6 = False  # For tutorial


def eventHandeler(ev, player):  # EH
    global Done1, Done2, Done3, Done4, Done6

    if ev.type == QUIT:
        pygame.quit()
        sys.exit()

    if ev.type == KEYDOWN:
        if (ev.key == K_a):
            player.moveLeft = True
            Done1 = True
        elif (ev.key == K_d):
            player.moveRight = True
            Done2 = True
        elif (ev.key == K_w or ev.key == K_SPACE):
            player.moveUp = True
            Done3 = True
        elif ev.key == K_ESCAPE:
            pygame.quit()
            sys.exit()

    elif ev.type == KEYUP:
        if (ev.key == K_a):
            player.moveLeft = False
        elif (ev.key == K_d):
            player.moveRight = False

    elif ev.type == MOUSEBUTTONDOWN:
        if pygame.mouse.get_pressed()[0]:
            player.attack0 = True
            Done4 = True
        if pygame.mouse.get_pressed()[2]:
            player.attack2 = True
            Done6 = True


# Display
HOR = 600
VER = 400
my_screen = pygame.display.set_mode((HOR, VER), 0, 32)
pygame.display.set_caption('GAME-NAME')
my_clock = pygame.time.Clock()
white = (255, 255, 255)
black = (0, 0, 0)
my_screen.fill(white)

font = pygame.font.SysFont(None, 32)
pygame.display.update()


def main():

    music.PlayMusic(font, black, my_screen)

    my_screen.fill(white)
    global Done1, Done2, Done3, Done4, Done6
    # Set the text for the first tutorial

    messages.message1(my_screen, font)  # First set of messages

    # posX=50 posY=VER-65 dimesionX=70 dimesionY=50 speedX=5 speedY=5
    player = ch.Player(50, VER-65, 70, 50, 5, 5, 'player.png')
    player.draw(my_screen)  # Draw plaeyer
    pygame.display.update()

    while ((Done1 and Done2 and Done3) is not True):
        # First section
        # Tutorial 1
        for ev in pygame.event.get():
            eventHandeler(ev, player)
        player.move()
        player.draw(my_screen)
        player.mouse(my_screen)
        pygame.display.update()
        my_clock.tick(120)

    # Set the text for the second tutorial
    Done1 = Done2 = Done3 = Done4 = Done6 = False

    messages.message2(my_screen, font)  # Second set of messages

    while (Done4 and Done6) is not True:
        # Second section
        # Tutorial 2
        for ev in pygame.event.get():
            eventHandeler(ev, player)
        player.move()
        player.draw(my_screen)
        player.mouse(my_screen)
        pygame.display.update()
        my_clock.tick(120)

    # Set the text for the last tutorial
    Done1 = Done2 = Done3 = Done4 = Done6 = False
    pygame.display.update()

    while len(player.AttackList):  # Clear all the attacks
        player.move()
        player.draw(my_screen)
        player.mouse(my_screen)
        pygame.display.update()
        my_clock.tick(120)

    possition = HOR - 60 - player.returnPosX()  # Find the place for the NPC
    ch_4 = ch.NPC(possition, VER-65, 70, 50, 5, 0, 'CH_4.png')  # place the NPC
    ch_4.draw(my_screen)  # Draw the NPC

    messages.message3(my_screen, font)  # Thrird set of messages
    messages.heal(my_screen, font, player.life, ch_4.life)  # Show heal
    messages.message4(my_screen, font)  # Four set of messages
    messages.message5(my_screen, font)  # Fith set of messages
    messages.message6(my_screen, font)  # Six set of messages

    while (player.life > 0) and (ch_4.life > 0):
        # Τhird section
        # Βattle tutorial
        for ev in pygame.event.get():
            eventHandeler(ev, player)

        player.move()  # Start of the player time
        player.draw(my_screen)
        player.mouse(my_screen)

        ch.checkcollide(player, ch_4, my_screen)
        ch_4.draw(my_screen)  # Εnd of the player turn

        ch_4.move(randint(0, 5), player.posX)  # Start the AI turn
        ch_4.draw(my_screen)
        ch_4.attacks(my_screen, randint(0, 50))
        ch.checkcollide(ch_4, player, my_screen)
        player.draw(my_screen)  # Εnd AI turn

        messages.heal(my_screen, font, player.life, ch_4.life)  # Dsplay heal
        pygame.display.update()

        # NPC auto generate health
        if (randint(0, 29) == 0) and (ch_4.life < 100):
            ch_4.changeHeal(-1)

        if player.rect.colliderect(ch_4):
            player.changeHeal(1)  # The fire will burn you

        messages.heal(my_screen, font, player.life, ch_4.life)  # Display heal
        pygame.display.update()
        my_clock.tick(120)

    my_screen.fill(white)
    pygame.display.update()
    if player.life > 0:  # Victory message
        music.VictoryMusic()
        messages.victory(my_screen, font)
    else:  # Defeat message
        music.DefeatMusic()
        messages.defeat(my_screen, font)


if __name__ == "__main__":
    main()
