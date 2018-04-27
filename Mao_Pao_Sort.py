import pygame,sys
import time
import math
from pygame.locals import *
white=255,255,255
blue = 1,1,200
pygame.init()
width = 20
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("bubble sorting")
a = [400,150,200,490,390,180,301,511,540,90]
def swap(t1, t2):
    return t2, t1


while True:
    for x in range(0,10):
        for s in range(0,9-x):
            if a[s]>a[s+1]:
                a[s],a[s+1]=swap(a[s],a[s+1])
            time.sleep(0.05)
            screen.fill((0,200,0))
            for i in range(0,10):
                    pygame.draw.line(screen,white,(50*(i+1),10),(50*(i+1),a[i]),width)  
                    pygame.display.update()
            for event in pygame.event.get():
                if event.type in (QUIT,KEYDOWN):
                    sys.exit()
            screen.fill((0,200,0))
            for i in range(0,10):
                pygame.draw.line(screen,(255,0,0),(50*(i+1),10),(50*(i+1),a[i]),width)
            pygame.display.update()

    break;