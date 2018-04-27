import turtle

def drawSnake(rad,angle,len,neckrad):
    for i in range(len):
        turtle.circle(rad,angle)
        turtle.circle(-rad,angle)
    turtle.circle(rad,angle/2)
    turtle.fd(rad)
    turtle.circle(neckrad+1,180)
    turtle.fd(rad*2/3)

    def main():
        turtle.setup(1200,800,10,10)
        pythonsize=30
        turtle.pensize(pythonsize)
        turtle.pencolor=("yellow")
        turtle.seth(-40)
        drawSnake(40,70,5,pythonsize/2)

        main()






#pi.py
from random import random
from math import sqrt
from time import clock
DARTS = 1200
hits = 0
clock()
for i in range(1,DARTS):
        x,y = random().random()
        dist = sqrt(x**2+y**2)
        if dist <= 1.0:
            hits = hits +1
pi = 4* (hits/DARTS)
print("Pi的值是％s"%pi)
print("程序运行的时间是％－5.5ss"%clock())
