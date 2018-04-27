import pygame,sys
import time
import math
from pygame.locals import *
white=255,255,255
blue = 1,1,200

# ------------1
# pygame.init()
# width = 20
# screen = pygame.display.set_mode((600,600))
# pygame.display.set_caption("bubble sorting")
# a = [400,150,200,490,390,180,301,511,540,90]
# def swap(t1, t2):
#     return t2, t1
# for x in range(0,10):
#     for s in range(0,9-x):
#         if a[s]>a[s+1]:
#             a[s],a[s+1]=swap(a[s],a[s+1])
#         time.sleep(0.05)
#         screen.fill((0,200,0))
#         for i in range(0,10):
#                 pygame.draw.line(screen,white,(50*(i+1),10),(50*(i+1),a[i]),width)  
#                 pygame.display.update()
# while True:
#     for event in pygame.event.get():
#         if event.type in (QUIT,KEYDOWN):
#             sys.exit()
#     screen.fill((0,200,0))
#     for i in range(0,10):
#         pygame.draw.line(screen,(255,0,0),(50*(i+1),10),(50*(i+1),a[i]),width)
#     pygame.display.update()
# -------------


# --------------2
# pygame.display.set_caption("Draw Rectangle")
# pos_x=200
# pos_y=0
# v_x=10
# v_y=10
# screen = pygame.display.set_mode((600,600))
# while(True):
#     for event in pygame.event.get():
#         if event.type in (QUIT,KEYDOWN):
#             sys.exit()
#     screen.fill((100,20,0))
#     pos_x+=v_x
#     pos_y+=v_y
#     if pos_x>500 or pos_x<0:
#         v_x=-v_x
#     if pos_y>500 or pos_y<0:
#         v_y=-v_y
#     color = 10,255,0
#     color1= 0,55,100
#     width = 0
#     start_radians=math.radians(0)
#     end_radians=math.radians(180)
#     pos=pos_x,pos_y,100,100
#     pygame.draw.rect(screen,color,pos,width)
#     pygame.draw.line(screen,color,(100,100),(500,500),20)
#     pygame.draw.arc(screen,color1,pos,start_radians,end_radians,20)
#     pygame.draw.circle(screen,color,(pos_x,pos_y),100,30)
#     pygame.display.update()
# --------------


# ------------3
# pygame.display.set_caption("Draw Train")
# pos_x=200
# pos_y=0
# v_x=10
# v_y=10
# width=0
# screen = pygame.display.set_mode((600,600))
# myfont=pygame.font.Font(None,30)
# image = myfont.render("hello py?",True,(255,25,0))
# while(True):
#     screen.fill((0,0,0))
#     if pos_x>=550 or pos_x<=0:
#         v_x=0
#     if pos_y>=550 or pos_y<=0:
#         v_y=0
#     for event in pygame.event.get():
#         if event.type == KEYDOWN:
#             if event.key == pygame.K_ESCAPE:
#                 sys.exit()
#             elif event.key == pygame.K_LEFT:
#                 v_x=-10
#                 v_y=0
#             elif event.key == pygame.K_RIGHT:
#                 v_x=10
#                 v_y=0
#             elif event.key == pygame.K_UP:
#                 v_x=0
#                 v_y=-10
#             elif event.key == pygame.K_DOWN:
#                 v_x=0
#                 v_y=10 
#     pos=pos_x,pos_y,50,50   
#     color = 255,255,255
#     pos_x+=v_x
#     pos_y+=v_y
#     screen.blit(image,(100,100))
#     pygame.draw.rect(screen,color,pos,width)
#     pygame.display.update()
# -------------


# ------------ game for chapter 3
# def print_text(font,x,y,text,color=white,shadow=True):
#     if shadow:
#         imgText = font.render(text,True,(0,0,0))
#         screen.blit(imgText,(x-2,y-2))
#     imgText=font.render(text,True,color)
#     screen.blit(imgText,(x,y))


# class Trivia(object):
#     def __init__(self,filename):
#         self.data = []
#         self.current = 0 
#         self.total = 0 
#         self.correct = 0
#         self.score = 0 
#         self.scored = False
#         self.failed = False
#         self.wronganswer = 0
#         self.colors = [white,white,white,white]

#         f=open(filename,"r")
#         trivia_data = f.readlines()
#         f.close()

#         for text_line in trivia_data:
#             self.data.append(text_line.strip())
#             self.total+=1

#     def show_question(self):
#         print_text(font1,210,5,"TRIVIA GAME")
#         print_text(font2,190,500-20,"Press Keys (1-4) To Answer",purple)
#         print_text(font2,530,5,"SCORE",purple)
#         self.correct = int(self.data[self.current+5])
#         question=self.current
#         print_text(font1,5,80,"Question"+str(question))
#         print_text(font2,20,120,self.data[self.current],yellow)

#         if self.scored:
#             self.colors = [white,white,white,white]
#             self.colors[self.current-1] = green
#             print_text(font1,230,380,"CORRECT!",green)
#             print_text(font2,170,420,"Press Enter for Next One",green)
#         elif self.failed:
#             self.colors = [white,white,white,white]
#             self.colors[self.current-1] = red
#             print_text(font1,230,380,"INCORRECT!",red)
#             print_text(font2,170,420,"Press Enter for Next One",red)
#         print_text(font1,5,170,"Answer")
#         print_text(font2,20,210,"1- "+self.data[self.current+1],self.colors[0])
#         print_text(font2,20,240,"2- "+self.data[self.current+2],self.colors[1])
#         print_text(font2,20,270,"3- "+self.data[self.current+3],self.colors[2])
#         print_text(font2,20,300,"4- "+self.data[self.current+4],self.colors[3])

#     def handle_input(self,number):
#         if (not self.scored) and (not self.failed):
#             if number == self.correct:
#                 self.scored=True
#                 self.score+=1
#             else:
#                 self.failed = True
#                 self.wronganswer = number
#     def next_question(self):
#         if self.scored or self.failed:
#             self.failed = False
#             self.scored = False
#             self.correct = 0
#             self.colors = [white,white,white,white]
#             self.current += 6
#             if self.current >= self.total:
#                 self.current = 0 

# pygame.init()
# screen = pygame.display.set_mode((600,600))
# pygame.display.set_caption("The Trivia Game")
# font1=pygame.font.Font(None,40)
# font2=pygame.font.Font(None,24)
# cyan=0,255,255
# yellow=255,255,0
# purple=255,0,255
# green=0,255,0
# red=255,0,0

# trivia=Trivia("/Users/zhangzhaobo/test.txt")

# while(True):
#     screen.fill((0,0,200))
#     trivia.show_question()
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             sys.exit()
#         elif event.type == KEYUP:
#             if event.type == pygame.K_ESCAPE:
#                 sys.exit()
#             elif event.type == pygame.K_LEFT:
#                 trivia.handle_input(1)
#             elif event.type == pygame.K_RIGHT:
#                 trivia.handle_input(2)
#             elif event.type == pygame.K_UP:
#                 trivia.handle_input(3)
#             elif event.type == pygame.K_DOWN:
#                 trivia.handle_input(4)
#             elif event.type == pygame.K_j:
#                 trivia.next_question()
#     pygame.display.update()

# --------

# ------------ game for chapter 4


