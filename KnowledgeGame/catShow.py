import pygame
from sys import exit
from pygame.locals import *
from time import time
class catShow():
    def __init__(self,screen):
        self.screen = screen
        self.cat = []
        self.now = 1
        self.size = 0
        self.lastTime = 0

    def loadCat(self):
        for i in range(14):
            self.cat.append(pygame.image.load('cat/cat'+str(i+1)+'.png').convert())
        self.size = 14

    def update(self, width, height):
        if(time() - self.lastTime > 0.3):
            self.lastTime = time()
            if self.now <= self.size - 1 :
                self.screen.blit(pygame.transform.rotozoom(self.cat[self.now]  , 0, 0.5), (width/7*5,height/3*2))
                self.now += 1
            else:
                self.screen.blit(pygame.transform.rotozoom(self.cat[0]  , 0, 0.5), (width/7*5,height/3*2))
                self.now = 1
