import pygame
import sys
import time

import music

from pygame.locals import *
from pygame.sprite import *
from attacks import *

pygame.init()

HOR = 600
VER = 400
pics = ['n_attack.png', 'CO_2.png', 'fire.png']


class Characters(Sprite):
    def __init__(self,  posX, posY,  speedX, speedY):
        Sprite.__init__(self)
        self.posY = posY
        self.posX = posX
        self.life = 100
        self.speedX = speedX
        self.speedY = speedY
        self.AttackList = []  # All active attacks

    def returnPosX(self):
        return(self.posX)

    def move(self):
        pass

    def changeHeal(self, number):
        self.life = self.life - number

    def draw(self, surf):
        surf.blit(self.image, self.rect)

    def controlAttacks(self, surf):
        for i in self.AttackList:
            i.move(surf)
            # delete objects outside of window
            if (i.faceRight) and (i.posX >= 600):
                self.AttackList.remove(i)
            elif (not i.faceRight) and (i.posX <= -80):
                self.AttackList.remove(i)


class Player(Characters):
    def __init__(self, posX, posY, dX, dY, speedX, speedY, pic):
        Characters.__init__(self,  posX, posY, speedX, speedY)
        self.rect = pygame.Rect(posX, posY, dX, dY)
        self.image = pygame.image.load(pic)
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.moveLeft = False
        self.moveRight = False
        self.moveUp = False  # You can move Up
        self.moveDown = False  # You can move Down
        self.attack0 = False
        self.attack2 = False
        self.faceRight = True  # character face

    def move(self):
        if self.moveLeft and self.rect.left >= -10:  # Move left
            self.faceRight = False
            self.posX = self.posX - self.speedX
            self.rect.move_ip(-self.speedX, 0)

        elif self.moveRight and self.rect.right <= HOR-1:  # Move right
            self.faceRight = True
            self.posX = self.posX + self.speedX
            self.rect.move_ip(self.speedX, 0)

        elif self.moveUp and self.posY == VER-65:  # Star the Jump
            music.Jump()
            self.posY = self.posY - self.speedY
            self.rect.move_ip(0, - self.speedY)

        elif self.moveUp and self.posY >= VER-200:  # Jump not in Top
            self.posY = self.posY - self.speedY
            self.rect.move_ip(0, -self.speedY)

        elif self.moveUp and self.posY == VER-200-5:  # Jump in Top
            self.posY = self.posY + self.speedY
            self.rect.move_ip(0, self.speedY)
            self.moveUp = False
            self.moveDown = True

        elif self.moveDown and self.posY <= VER-55:  # Falling from the Top
            self.posY = self.posY + self.speedY
            self.rect.move_ip(0, self.speedY)

            if self.posY == VER-65:  # Reach the bottom
                self.moveDown = False
                music.Fall()

    def mouse(self, surf):
        if self.attack0:
            if self.faceRight:  # Character face right side
                attack = Attacks(self.posX+80, self.posY, 70, 50,
                                 pics[0], True, surf, 1, 1)
                self.AttackList.append(attack)  # Insert the new attack
                self.attack0 = False

            else:  # Character face left side
                attack = Attacks(self.posX-100, self.posY, 70, 50,
                                 pics[0], False, surf, 1, 1)
                self.AttackList.append(attack)  # Insert the new attack
                self.attack0 = False

        elif self.attack2:
            if self.faceRight:  # Character face right side
                attack = Attacks(self.posX+80, self.posY, 70, 50,
                                 pics[1], True, surf, 10, 2)
                self.AttackList.append(attack)  # insert new attack
                self.attack2 = False

            else:  # Character face left side
                attack = Attacks(self.posX-100, self.posY, 70, 50,
                                 pics[1], False, surf, 10, 2)
                self.AttackList.append(attack)  # insert new attack
                self.attack2 = False

        self.controlAttacks(surf)


class NPC(Characters):
    def __init__(self, posX, posY, dX, dY, speedX, speedY, pic):
        Characters.__init__(self,  posX, posY, speedX, speedY)
        self.rect = pygame.Rect(posX, posY, dX, dY)
        self.image = pygame.image.load(pic)
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.faceRight = False  # Face towards the left

    def move(self, rand, enemy):
        if rand == 1:
            if enemy < self.posX:
                self.posX = self.posX - self.speedX
                self.rect.move_ip(-self.speedX, 0)
                self.faceRight = False
            else:
                self.posX = self.posX + self.speedX
                self.rect.move_ip(self.speedX, 0)
                self.faceRight = True

    def attacks(self, surf, rand):
        if rand == 2:
            if self.faceRight:
                attack = Attacks(self.posX + 80, self.posY, 70, 50,
                                 pics[2], True, surf, 10, 1)
                self.AttackList.append(attack)
            else:
                attack = Attacks(self.posX - 100, self.posY, 70, 50,
                                 pics[2], False, surf, 10, 1)
                self.AttackList.append(attack)
        self.controlAttacks(surf)


def checkcollide(ch1, ch2, surf):
    for i in ch1.AttackList:
        if i.rect.colliderect(ch2.rect):
            ch2.draw(surf)
            if i.hit:
                ch2.changeHeal(i.damage)
                i.hit = False
