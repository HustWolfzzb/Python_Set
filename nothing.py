import pygame,sys
import time
from pygame.locals import *
white=255,255,255
blue = 1,1,200
pygame.init()
screen = pygame.display.set_mode((600,600))
width=0
pygame.display.set_caption("冒泡排序")
a=[550,500,450,400,350,300,250,200,100,50]
def swap(t1, t2):
    return t2, t1
for x in range(0,10):
	width+=3
	for s in range(0,9-x):
		if a[s]>a[s+1]:
			a[s],a[s+1]=swap(a[s],a[s+1])
		time.sleep(0.1)
		for i in range(1,10):
			pygame.draw.line(screen,white,(50*(i+1),10),(50*(i+1),a[i]/2),width)
		for event in pygame.event.get():
			if event.type in (QUIT,KEYDOWN):
				sys.exit()
		pygame.display.flip()
