import pygame
import sys
import time

from pygame.locals import *
from pygame.sprite import *

pygame.init()
HOR = 600
VER = 400


class Attacks(Sprite):
    def __init__(self, posX, posY, dX, dY, pic, faceRight, surf, damage, scl):
        if faceRight:
            posX = posX-10
        else:
            posX = posX+50
        Sprite.__init__(self)
        self.rect = pygame.Rect(posX, posY, dX, dY)
        self.image = pygame.image.load(pic)
        scl = 80 // scl
        self.image = pygame.transform.scale(self.image, (scl, scl))
        self.damage = damage
        self.posX = posX
        self.posY = posY
        self.speed = 6
        self.faceRight = faceRight
        self.hit = True
        surf.blit(self.image, self.rect)

    def move(self, surf):
        if (self.faceRight) and (self.posX <= 600):  # move right
            self.posX = self.posX + self.speed
            self.rect.move_ip(self.speed, 0)
        elif (not self.faceRight) and (self.posX > -80):  # move left
            self.posX = self.posX - self.speed
            self.rect.move_ip(-self.speed, 0)
        surf.blit(self.image, self.rect)
