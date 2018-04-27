#coding:utf-8
import os
from time import time,sleep
import pygame
from sys import exit
from pygame.locals import *
from random import randint
white=255, 255, 255
blue = 1, 1, 200

def print_text( font, x, y, text, color=white, shadow=True ):
    if shadow:
        imgText = font.render(text,  True,  (0,  0,  0))
        screen.blit(imgText,  (x-2,  y-2))
    imgText=font.render(text,  True,  color)
    screen.blit(imgText,  (x,  y))

def Judge(gameTrivia):
    if (gameTrivia.current/6 + 1) > 20:
        if gameTrivia.score1 > gameTrivia.score2 :
            print_text(font1,  width/8, height/15,  "恭喜 1 队获得胜利！！", red)
            return 1
        if gameTrivia.score1 < gameTrivia.score2:
            print_text(font1,  width/8, height/15,  "恭喜 2 队获得胜利！！", red)
            return 2
        if gameTrivia.score1 == gameTrivia.score2:
            return 0
    return 0

def run(width,height):
    pygame.init()
    screen = pygame.display.set_mode((width,height) , FULLSCREEN)
    stars = []
    clock = pygame.time.Clock()
    # 在第一帧，画上一些星星
    for n in range(200):
        x = float(randint(0, width - 1))
        y = float(randint(0, height - 1))
        speed = float(randint(10, 300))
        stars.append( Star(x, y, speed) )
    time_ready = time()
    white = (255, 255, 255)
    time_now = time()
    while time_now - time_ready <= 5:
        time_now = time()
        for event in pygame.event.get():
            if event.type == QUIT:
                return
        # 增加一颗新的星星
        x = float(randint(0, width - 1))
        y = float(randint(0, height - 1 ))
        speed = float(randint(10, 300))
        star = Star(x, y, speed)
        stars.append(star)

        time_passed = clock.tick()
        time_passed_seconds = time_passed / 1000.

        screen.fill((0, 0, 0))

        # 绘制所有的星
        for star in stars:
            new_x = star.x - time_passed_seconds * star.speed
            pygame.draw.aaline(screen, white, (new_x, star.y), (star.x+1., star.y))
            star.x = new_x
            # 星星跑出了画面，就删了它
            if not on_screen(star):
                stars.remove(star)
        pygame.display.flip()


class Star(object):
    def __init__(self, x, y, speed):

        self.x = x
        self.y = y
        self.speed = speed
def on_screen(star):
    return star.x > 0

class Trivia(object):
    def __init__(self, filename):
        self.data = []
        self.current = 0
        self.total = 0
        self.correct = 0
        self.score1 = 0
        self.score2 = 0
        self.scored = False
        self.failed = False
        self.wronganswer = 0
        self.readyTimeCount = 10
        self.answerTimeCount = 128
        self.go = False
        self.colors = [white,  white,  white,  white]

        f=open(filename,  'r', encoding="utf-8")
        tdata = f.readlines()
        for x in tdata:
            self.data.append(x.strip())
            self.total += 1

    def timeCount(self):
        if self.readyTimeCount > 0:
            print_text(fontno,  width/4*3, height/3, str(int(self.readyTimeCount/5)), red)
            self.readyTimeCount -= 1
            sleep(0.2)
        elif self.readyTimeCount == 0 and not self.go:
            self.go = True
            print_text(fontno,  width/3, height/4, "Go!", yellow)
            sleep(0.2)
        elif self.answerTimeCount > 0:
            print_text(font1,  width/6*5, height/2, str(int(self.answerTimeCount/5)), orange)
            self.answerTimeCount -= 1
            sleep(0.2)

    def timeReset(self):
        self.readyTimeCount = 10
        self.answerTimeCount = 128
        self.go = False

    def show_question(self):
        print_text(font1,  width/8, height/15,  "机械学院14级\"头脑风暴\"知识竞赛！", blue)
        print_text(font3,  width/3, height/20*19,  "***最终解释权归机械学院14级年级学生会所有***", white)
        print_text(font2,  width/20, height/25*4, "SCORE->1", cyan)
        print_text(font2,  width/10*8 , height/25*4, "SCORE->2", cyan)
        self.correct = int(self.data[self.current+5])
        question=int(self.current/6)+1
        print_text(font1, width/10*4, height/20*4, "Question "+str(question), orange)
        fontsize = int(1000/len(self.data[self.current]))
        if fontsize > 50:
            fontsize = 50
        if fontsize < 30:
            fontsize = 30
        if len(self.data[self.current])>35:
            str1 = self.data[self.current][0:35]
            if len(self.data[self.current])<=70:
                str2 = self.data[self.current][35:]
                print_text(pygame.font.Font('zui.ttf',  fontsize),  width/10,  height/20*6,  str1, yellow)
                print_text(pygame.font.Font('zui.ttf',  fontsize),  width/10,  height/20*7,  str2, yellow)
            else:
                str2 = self.data[self.current][35:70]
                str3 = self.data[self.current][70:]
                print_text(pygame.font.Font('zui.ttf', 20),  width/10,  height/60*17,  str1, yellow)
                print_text(pygame.font.Font('zui.ttf',  20),  width/10,  height/60*19,  str2, yellow)
                print_text(pygame.font.Font('zui.ttf',  20),  width/10,  height/60*21,  str2, yellow)
        else:
            print_text(pygame.font.Font('zui.ttf',  fontsize),  width/6,  height/20*6,  self.data[self.current],  yellow)

        if self.scored:
            self.colors[self.correct-1] = green
        elif self.failed:
            self.colors[self.wronganswer-1] = red
        print_text(font1, width/10*4, height/20*8, "Answer:",  orange)
        maxlen = 0
        for i in range(4):
            if len(self.data[self.current+i+1])>maxlen:
                maxlen = len(self.data[self.current+i+1])
        print_text(font2,  width/20*9-maxlen*20,  height/20*10,  "1->  "+self.data[self.current+1],  self.colors[0])
        print_text(font2,  width/20*9-maxlen*20,  height/20*12,  "2->  "+self.data[self.current+2],  self.colors[1])
        print_text(font2,  width/20*9-maxlen*20,  height/20*14,  "3->  "+self.data[self.current+3],  self.colors[2])
        print_text(font2,  width/20*9-maxlen*20,  height/20*16,  "4->  "+self.data[self.current+4],  self.colors[3])
        print_text(font2,  width/8,  height/5+10,  str(self.score1),  red)
        print_text(font2,  width/20*17,  height/5+10, str(self.score2),  red)

    def handle_input(self,  number):
        if not self.scored:
            if number == self.correct :
                self.scored = True
            else:
                self.failed = True
                self.wronganswer = number

    def next_question(self):
        pygame.display.flip()
        if self.scored or self.failed:
            self.failed = False
            self.scored = False
            self.correct = 0
            self.colors = [white, white, white, white]
            self.current += 6
            self.timeReset()
            if self.current >= self.total:
                self.current = 0

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100,0)
pygame.init()
width,  height = 1240,  698
screen = pygame.display.set_mode((width, height), HWSURFACE | FULLSCREEN,32)
background = pygame.image.load("kate.png").convert()
frontground = pygame.image.load("dragon.png").convert_alpha()
# frontground = pygame.transform.smoothscale(frontground, (int(frontground.get_width()/2), int(frontground.get_height()/2)))
pygame.display.set_caption("机械学院14级\"头脑风暴\"知识竞赛！")
font1 = pygame.font.Font('zui.ttf',  60)
font2 = pygame.font.Font('zui.ttf',  40)
font3 = pygame.font.Font('zui.ttf',  20)
fontno = pygame.font.Font('ye.ttf', 300)

run(background.get_width(),background.get_height())
cyan = 0, 255, 255
yellow = 255, 255, 0
purple = 255, 0, 255
green = 0, 255, 0
red = 255, 0, 0
gray = 63, 63, 63
black = 8, 8, 8
orange = 255, 165, 0
Magenta = 255, 0, 255
trivia = Trivia("test.txt")
screen.blit(background,  (0, 0))
print_text(font1,  width/8, height/15,  "机械学院14级\"头脑风暴\"知识竞赛！", blue)
print_text(font3,  width/3, height/20*19,  "***最终解释权归机械学院14级年级学生会所有***", white)
pygame.display.flip()
sleep(3)
while True:
    screen.blit(background,  (0, 0))
    trivia.show_question()
    pygame.display.flip()
    Flag = True
    if Judge(trivia) != 0:
        continue
    while Flag:
        screen.blit(background,  (0, 0))
        trivia.show_question()
        trivia.timeCount()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYUP and trivia.readyTimeCount == 0:
                if event.key == pygame.K_ESCAPE:
                    exit()
                elif event.key == pygame.K_a:
                    trivia.handle_input(1)
                elif event.key == pygame.K_y and (trivia.scored or trivia.failed):
                    trivia.score1 += 2
                    Flag = False
                elif event.key == pygame.K_h and (trivia.scored or trivia.failed):
                    trivia.score2 += 2
                    Flag = False
                elif event.key == pygame.K_u and (trivia.scored or trivia.failed):
                    if trivia.score1 > 0:
                        trivia.score1 -= 1
                    Flag = False
                elif event.key == pygame.K_j and (trivia.scored or trivia.failed):
                    if trivia.score2 > 0:
                        trivia.score2 -= 1
                    Flag = False
                elif event.key == pygame.K_s:
                    trivia.handle_input(2)
                elif event.key == pygame.K_d:
                    trivia.handle_input(3)
                elif event.key == pygame.K_f:
                    trivia.handle_input(4)
                elif event.key == pygame.K_n:
                    trivia.next_question()
                    Flag = False