#coding:utf-8
import os
from time import time
from time import sleep
import pygame
from sys import exit
from pygame.locals import *
from random import randint

white=255, 255, 255
blue = 1, 1, 200
cyan = 0, 255, 255
yellow = 255, 255, 0
purple = 255, 0, 255
green = 0, 255, 0
red = 255, 0, 0
gray = 63, 63, 63
black = 8, 8, 8
orange = 255, 165, 0
Magenta = 255, 0, 255
width,  height = 1200, 677

def print_text(screen, font, x, y, text, color=white, shadow=True ):
    if shadow:
        imgText = font.render(text,  True,  (0,  0,  0))
        screen.blit(imgText,  (x-2,  y-2))
    imgText=font.render(text,  True,  color)
    screen.blit(imgText,  (x,  y))

def Judge(gameTrivia,screen):
    if (gameTrivia.current/6 + 1) > 2:
        if gameTrivia.score1 > gameTrivia.score2 :
            return 1
        if gameTrivia.score1 < gameTrivia.score2:
            return 2
        if gameTrivia.score1 == gameTrivia.score2:
            return 0
    return 0


def choosePart(screen):
    xd = 50
    yd = 20
    heartPosition = [ (width//10, height//3),(width//10*3, height//3),(width//2, height//3), (width//10*7, height//3), (width//10*9 , height//3), (width//5, height//3*2), (width//5*2, height//3*2), (width//5*3, height//3*2), (width//5*4, height//3*2) ] 
    Radius = width//15
    chooseSubject = 0
    chooseOk = False
    font4 = pygame.font.Font('ye.ttf', 50)
    while not chooseOk:
        screen.blit(background,  (0, 0))
        print_text(screen, font1,  width/8, height/15,  "机械学院14级\"头脑风暴\"知识竞赛！", blue)
        print_text(screen, font3,  width/3, height/20*19,  "***最终解释权归机械学院14级年级学生会所有***", white)
        pygame.draw.circle(screen, purple, heartPosition[0], Radius)
        print_text(screen, font4, heartPosition[0][0] - xd, heartPosition[0][1] - yd, "机械", cyan)
        pygame.draw.circle(screen, purple, heartPosition[1], Radius)
        print_text(screen, font4, heartPosition[1][0] - xd, heartPosition[1][1] - yd, "产设", cyan)
        pygame.draw.circle(screen, purple, heartPosition[2], Radius)
        print_text(screen, font4, heartPosition[2][0] - xd, heartPosition[2][1] - yd, "测控", cyan)
        pygame.draw.circle(screen, purple,  heartPosition[3], Radius)
        print_text(screen, font4, heartPosition[3][0] - xd, heartPosition[3][1] - yd, "工程", cyan)
        pygame.draw.circle(screen, purple, heartPosition[4], Radius)
        print_text(screen, font4, heartPosition[4][0] - xd, heartPosition[4][1] - yd, "人文", cyan)
        pygame.draw.circle(screen, purple, heartPosition[5], Radius)
        print_text(screen, font4, heartPosition[5][0] - xd, heartPosition[5][1] - yd, "诗歌", cyan)
        pygame.draw.circle(screen, purple, heartPosition[6], Radius)
        print_text(screen, font4, heartPosition[6][0] - xd, heartPosition[6][1] - yd, "网文", cyan)
        pygame.draw.circle(screen, purple, heartPosition[7], Radius)
        print_text(screen, font4, heartPosition[7][0] - xd, heartPosition[7][1] - yd, "艺术", cyan)
        pygame.draw.circle(screen, purple, heartPosition[8], Radius)
        print_text(screen, font4, heartPosition[8][0] - xd, heartPosition[8][1] - yd, "二次元", cyan)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    exit()
                elif event.key == pygame.K_1:
                    if chooseSubject == 0:
                        chooseSubject += 1
                    else:
                        chooseSubject += 10
                        chooseOk = True
                elif event.key == pygame.K_2:
                    if chooseSubject == 0:
                        chooseSubject += 2
                    else:
                        chooseSubject += 20
                        chooseOk = True
                elif event.key == pygame.K_3:
                    if chooseSubject == 0:
                        chooseSubject += 3
                    else:
                        chooseSubject += 30
                        chooseOk = True
                elif event.key == pygame.K_4:
                    if chooseSubject == 0:
                        chooseSubject += 4
                    else:
                        chooseSubject += 40
                        chooseOk = True
                elif event.key == pygame.K_5:
                    if chooseSubject == 0:
                        chooseSubject += 5
                    else:
                        chooseSubject += 50
                        chooseOk = True
                elif event.key == pygame.K_6:
                    if chooseSubject == 0:
                        chooseSubject += 6
                    else:
                        chooseSubject += 60
                        chooseOk = True
                elif event.key == pygame.K_7:
                    if chooseSubject == 0:
                        chooseSubject += 7
                    else:
                        chooseSubject += 70
                        chooseOk = True
                elif event.key == pygame.K_8:
                    if chooseSubject == 0:
                        chooseSubject += 8
                    else:
                        chooseSubject += 80
                        chooseOk = True
                elif event.key == pygame.K_9:
                    if chooseSubject == 0:
                        chooseSubject += 9
                    else:
                        chooseSubject += 90
                        chooseOk = True
    if chooseSubject > 10:
        print(chooseSubject)
        return chooseSubject,chooseOk


def run(width,height,screen,delay):
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
    while time_now - time_ready <= delay:
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


class MySprite(pygame.sprite.Sprite):
    def __init__(self, target):
        pygame.sprite.Sprite.__init__(self)
        self.target_surface = target
        self.image = None
        self.master_image = None
        self.rect = None
        self.topleft = 0,0
        self.frame = 0
        self.old_frame = -1
        self.frame_width = 1
        self.frame_height = 1
        self.first_frame = 0
        self.last_frame = 0
        self.columns = 1
        self.last_time = 0

    def load(self, filename, width, height, columns, posx, posy):
        self.master_image = pygame.image.load(filename).convert_alpha()
        self.frame_width = width
        self.frame_height = height
        self.rect = posx,posy,width,height
        self.columns = columns
        rect = self.master_image.get_rect()
        self.last_frame = (rect.width // width) * (rect.height // height) - 1

    def update(self, current_time, rate=60):
        if current_time > self.last_time + rate:
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = self.first_frame
            self.last_time = current_time

        if self.frame != self.old_frame:
            frame_x = (self.frame % self.columns) * self.frame_width
            frame_y = (self.frame // self.columns) * self.frame_height
            rect = ( frame_x, frame_y, self.frame_width, self.frame_height )
            self.image = self.master_image.subsurface(rect)
            self.old_frame = self.frame


class Trivia(object):
    def __init__(self):
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

    def loadSubject(self,filename):
        f=open(filename,  'r', encoding="utf-8")
        tdata = f.readlines()
        for x in tdata:
            self.data.append(x.strip())
            self.total += 1

    def timeCount(self, screen):
        if self.readyTimeCount > 0:
            print_text(screen, fontno,  width/4*3, height/3, str(self.readyTimeCount//5), red)
            self.readyTimeCount -= 1
            sleep(0.2)
        elif self.readyTimeCount == 0 and not self.go:
            self.go = True
            print_text(screen, fontno,  width/3, height/4, "Go!", yellow)
            sleep(0.2)
        elif self.answerTimeCount > 0:
            print_text(screen, font1,  width/6*5, height/2, str(self.answerTimeCount//5), orange)
            self.answerTimeCount -= 1
            sleep(0.2)

    def timeReset(self):
        self.readyTimeCount = 10
        self.answerTimeCount = 128
        self.go = False

    def show_question(self, screen):
        print_text(screen, font1,  width/8, height/15,  "机械学院14级\"头脑风暴\"知识竞赛！", blue)
        print_text(screen, font3,  width/3, height/20*19,  "***最终解释权归机械学院14级年级学生会所有***", white)
        print_text(screen, font2,  width/20, height/25*4, "SCORE->1", cyan)
        print_text(screen, font2,  width/10*8, height/25*4, "SCORE->2", cyan)
        self.correct = int(self.data[self.current+5])
        question = self.current//6 + 1
        print_text(screen, font1, width/10*4, height/20*4, "Question "+str(question), orange)
        fontsize =  1000//len(self.data[self.current])
        if fontsize > 50:
            fontsize = 50
        if fontsize < 30:
            fontsize = 30
        if len(self.data[self.current])>35:
            str1 = self.data[self.current][0:35]
            if len(self.data[self.current])<=70:
                str2 = self.data[self.current][35:]
                print_text(screen, pygame.font.Font('zui.ttf',  fontsize),  width/10,  height/20*6,  str1, yellow)
                print_text(screen, pygame.font.Font('zui.ttf',  fontsize),  width/10,  height/20*7,  str2, yellow)
            else:
                str2 = self.data[self.current][35:70]
                str3 = self.data[self.current][70:]
                print_text(screen, pygame.font.Font('zui.ttf', 20),  width/10,  height/60*17,  str1, yellow)
                print_text(screen, pygame.font.Font('zui.ttf',  20),  width/10,  height/60*19,  str2, yellow)
                print_text(screen, pygame.font.Font('zui.ttf',  20),  width/10,  height/60*21,  str2, yellow)
        else:
            print_text(screen, pygame.font.Font('zui.ttf',  fontsize),  width/6,  height/20*6,  self.data[self.current],  yellow)

        if self.scored:
            self.colors[self.correct-1] = green
        elif self.failed:
            self.colors[self.wronganswer-1] = red
        print_text(screen, font1, width/10*4, height/20*8, "Answer:",  orange)
        maxlen = 0
        for i in range(4):
            if len(self.data[self.current+i+1])>maxlen:
                maxlen = len(self.data[self.current+i+1])
        print_text(screen, font2,  width/20*9-maxlen*20,  height/20*10,  "1->  "+self.data[self.current+1],  self.colors[0])
        print_text(screen, font2,  width/20*9-maxlen*20,  height/20*12,  "2->  "+self.data[self.current+2],  self.colors[1])
        print_text(screen, font2,  width/20*9-maxlen*20,  height/20*14,  "3->  "+self.data[self.current+3],  self.colors[2])
        print_text(screen, font2,  width/20*9-maxlen*20,  height/20*16,  "4->  "+self.data[self.current+4],  self.colors[3])
        print_text(screen, font2,  width/8,  height/5+10,  str(self.score1),  red)
        print_text(screen, font2,  width/20*17,  height/5+10, str(self.score2),  red)

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


def generateTrivia(num):
    trivia = Trivia()
    subject = "subject/test"
    if num//10 != num % 10:
        trivia.loadSubject(subject + str(num // 10) + ".txt")
    trivia.loadSubject(subject + str(num % 10) + ".txt")
    trivia.loadSubject("subject/normal.txt")
    return trivia


pygame.init()   
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100, 30)
font1 = pygame.font.Font('zui.ttf',  60)
font2 = pygame.font.Font('zui.ttf',  40)
font3 = pygame.font.Font('zui.ttf',  20)
fontno = pygame.font.Font('ye.ttf', 300)
screen = pygame.display.set_mode((width, height),RESIZABLE,32) # ,HWSURFACE | FULLSCREEN,
background = pygame.image.load("back.jpg").convert()


def main():

    pygame.display.set_caption("机械学院14级\"头脑风暴\"知识竞赛！")
    # run(background.get_width(),background.get_height(),screen,2)

    chooseSubject = 0
    chooseOk = False
    while not chooseOk :
        chooseSubject = 0
        screen.blit(background,  (0, 0))
        print_text(screen, font1,  width/8, height/15,  "机械学院14级\"头脑风暴\"知识竞赛！", blue)
        print_text(screen, font3,  width/3, height/20*19,  "***最终解释权归机械学院14级年级学生会所有***", white)
        chooseSubject,chooseOk = choosePart(screen)
        pygame.display.flip()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        exit()
                    

    trivia = generateTrivia(chooseSubject)

    framerate = pygame.time.Clock()
    cat = MySprite(screen)
    cat.load("sprite.png", 100, 100, 4, 20, height/5*4)
    cat2 = MySprite(screen)
    cat2.load("sprite.png", 100, 100, 4, width - 120, height/5*4)

    group = pygame.sprite.Group()
    group.add(cat)
    group.add(cat2)

    while True :
        Flag = True
        done = Judge(trivia,screen)
        if done != 0:
            TIME1 = time()
            while time() - TIME1 < 5:
                screen.blit(background,  (0, 0))
                if done == 1:
                    print_text(screen, font1,  width/8, height//5*2,  "恭喜 1 队获得胜利！！进入下一轮！", red)
                else :
                    print_text(screen, font1,  width/8, height//5*2,  "恭喜 2 队获得胜利！！进入下一轮！", red)
            
                framerate.tick(30)
                ticks = pygame.time.get_ticks()
                group.update(ticks)
                group.draw(screen)
                # trivia.timeCount(screen)
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return
                    elif event.type == pygame.KEYUP and trivia.readyTimeCount >= 0:
                        if event.key == pygame.K_ESCAPE:
                            return
            break


        while Flag:
            screen.blit(background,  (0, 0))
            trivia.show_question(screen)
            framerate.tick(30)
            ticks = pygame.time.get_ticks()
            group.update(ticks)
            group.draw(screen)
            # trivia.timeCount(screen)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.KEYUP and trivia.readyTimeCount >= 0:
                    if event.key == pygame.K_ESCAPE:
                        return
                    elif event.key == pygame.K_u and (trivia.scored or trivia.failed):
                        trivia.score1 += 2
                        Flag = False
                    elif event.key == pygame.K_j and (trivia.scored or trivia.failed):
                        trivia.score2 += 2
                        Flag = False
                    elif event.key == pygame.K_i and (trivia.scored or trivia.failed):
                        if trivia.score1 > 0:
                            trivia.score1 -= 1
                        Flag = False
                    elif event.key == pygame.K_k and (trivia.scored or trivia.failed):
                        if trivia.score2 > 0:
                            trivia.score2 -= 1
                        Flag = False
                    elif event.key == pygame.K_a:
                        trivia.handle_input(1)
                    elif event.key == pygame.K_s:
                        trivia.handle_input(2)
                    elif event.key == pygame.K_d:
                        trivia.handle_input(3)
                    elif event.key == pygame.K_f:
                        trivia.handle_input(4)
                    elif event.key == pygame.K_n:
                        trivia.next_question()
                        Flag = False

if __name__ == '__main__':
    for i in range(8):
        main()
