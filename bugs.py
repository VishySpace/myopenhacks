from graphics import *
import math
from random import seed
from random import randint
import sys

# seed random number generator
seed(1)
# generate some integers

def main():
    nump = int(sys.argv[1])
    ox = 10.0
    oy = 10.0
    gridsize = 600
    size = 300.0
    radius = 5.0
    cx = gridsize / 2
    cy = gridsize / 2
    win = GraphWin('Face', gridsize, gridsize)
    win.setCoords(0, 0, gridsize-1, gridsize-1)
    antpos = []
    colors = ["blue", "red", "green", "black"]
    ants = []
    for i in range(nump):
        antpos.append(Point(cx + size * math.cos(2 * math.pi * i / nump), cy + size * math.sin(2 * math.pi * i / nump)))
        if (i > 0):
            lin = Line(antpos[i-1], antpos[i])
            lin.setWidth(3)
            lin.draw(win)
        ants.append(Circle(antpos[i], radius))
        ants[i].setFill(colors[i%4])
        ants[i].draw(win)
    lin = Line(antpos[nump-1], antpos[0])
    lin.setWidth(3)
    lin.draw(win)
    incr = 10
    touching = 0
    i = 0
    delt = 1
    while (not touching):
        i += 1
        for a in range(nump):
#            delt = randint(1, nump)
            next = (a+delt) % nump
            if (a == next):
                next = (a+1) % nump
            ax = ants[a].getCenter().getX()
            ay = ants[a].getCenter().getY()
            pt = Point(ax, ay)
            pt.setFill(colors[a%4])
            pt.draw(win)
            nx = ants[next].getCenter().getX()
            ny = ants[next].getCenter().getY()
            dist = ((ny - ay)**2 + (nx - ax)**2)**0.5
#            print(dist)
            dy = (ny - ay) / (dist - incr)
            dx = (nx - ax) / (dist - incr)

            ants[a].move(-dx, -dy)
            if (i%5 == 0):
                lin = Line(Point(ax, ay), Point(nx, ny))
                lin.setWidth(1)
                lin.setFill(colors[a%4])
                lin.draw(win)
            if ((dist < radius) or (dist < incr)):
                touching = 1
            if (touching):
                break

    if (0):
        head = Circle(Point(40,100), 25) # set center and radius
        head.setFill("yellow")
        head.draw(win)

        eye1 = Circle(Point(30, 105), 5)
        eye1.setFill('blue')
        eye1.draw(win)

        eye2 = Line(Point(45, 105), Point(55, 105)) # set endpoints
        eye2.setWidth(3)
        eye2.draw(win)

        mouth = Oval(Point(30, 90), Point(50, 85)) # set corners of bounding box
        mouth.setFill("red")
        mouth.draw(win)

    #label = Text(Point(100, 120), 'A face')
    #label.draw(win)

    #message = Text(Point(win.getWidth()/2, 20), 'Click anywhere to quit.')
    #message.draw(win)
    for i in range(nump):
        ants[i].undraw()
    win.getMouse()
    win.close()

main()
