from graphics import *
import math
from math import *
from random import seed, randint
import sys
from datetime import datetime

# seed random number generator
dt = datetime.now()
sd = dt.microsecond
seed(sd)
# generate some integers
terminate = 0
gridsize = 600
entities = []
win = GraphWin('Face', gridsize, gridsize)

class shapeCircle(object):
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
        self.sobj = Circle(Point(0, 0), self.radius)
        self.sobj.setOutline(self.color)
        self.sobj.setFill(self.color)
        self.sobj.draw(win)
    def draw(self, x, y):
        if (self.radius == 0):
            return

        self.sobj.move(x - self.sobj.getCenter().getX(), y - self.sobj.getCenter().getY())
        return
        self.sobj = Circle(Point(x, y), self.radius)
        self.sobj.setOutline(self.color)
        self.sobj.setFill(self.color)
        self.sobj.draw(win)
        self.sobj.undraw()

        self.sobj = Circle(Point(x, y), self.radius)
        self.sobj.setOutline(self.color)
        self.sobj.setFill(self.color)
        self.sobj.draw(win)

class shapeSquare(object):
    def __init__(self, side, color):
        self.side = side
        self.color = color

    def draw(self, x, y):
        c1 = Rectangle(Point(x - self.side/2, y - self.side/2), Point(x+self.side/2, y+self.side/2))
        c1.setOutline(self.color)
        c1.setFill(self.color)
        c1.draw(win)

class Entity(object):
    def __init__(self, shape, speed, x, y):
        self.shape = shape
        self.speed = speed
        self.x = x
        self.y = y
        shape.draw(x, y)

    def draw(self):
        self.shape.draw(self.x, self.y)

    def move(self, x, y):
        self.x = x
        self.y = y

class FixedEntity(Entity):
    def __init__(self, shape, x, y):
        Entity.__init__(self, shape, 0, x, y)
        self.x = x
        self.y = y

    def move(self):
        return

class EllipseEntity(Entity):
    def __init__(self, shape, speed, angle, cobj, rx, ry):
        Entity.__init__(self, shape, speed, 0, 0)
        self.rx = rx
        self.ry = ry
        self.center = cobj
        self.setAngle(angle)
        self.perimeter = 2 * math.pi * sqrt((rx**2 + ry**2)/2)
        self.dist = self.angle * self.perimeter / 360

    def setAngle(self, angle):
        self.angle = angle
        theta = 2 * math.pi * self.angle/360
        r = (self.rx * self.ry) / sqrt((self.rx**2 * (sin(theta))**2) + (self.ry**2 * (cos(theta))**2))
        self.x = self.center.x + r*math.cos(theta)
        self.y = self.center.y + r*math.sin(theta)
        self.draw()

    def move(self, iter):
        self.dist += self.speed
        self.angle = (self.dist * 360 / self.perimeter)
        if (self.angle >= 360):
            self.angle -= 360
            self.dist = 0
        self.setAngle(self.angle)


class FunctionEntity(Entity):
    def __init__(self, shape, speed, ix, iy, expr, amp):
        Entity.__init__(self, shape, speed, ix, iy)
        self.expr = expr
        self.dist = 0
        self.iy = iy
        self.ix = ix
        self.amp = amp

    def move(self, iter):
        nx = self.x
        nx += self.speed
        if (nx >= gridsize):
            nx = self.ix
        ny = self.iy + self.amp * (math.sin(4 * nx * math.pi / 360)) #
        x = nx
        ny = self.iy + eval(self.expr)
        self.x = nx
        self.y = ny
        self.draw()

class FollowerEntity(Entity):
    def __init__(self, shape, speed, x, y, fid, towards):
        Entity.__init__(self, shape, speed, x, y)
        self.following = fid
        self.dist = 0
        self.towards = towards

    def move(self, iter):
        global entities, win
        if (self.following == None):
            return
        x = self.x
        y = self.y
        xf = self.following.x
        yf = self.following.y

        dist = ((y - yf)**2 + (x - xf)**2)**0.5
        if (dist == 0):
            dist = 1
        if (self.towards):
            ny = y + (yf - y) * self.speed / dist
            nx = x + (xf - x) * self.speed / dist
        else:
            ny = y - (yf - y) * self.speed / dist
            nx = x - (xf - x) * self.speed / dist
        self.x = nx
        self.y = ny
        self.draw()

        #lin = Line(Point(x, y), Point(xf, yf))
        #lin.setWidth(1)
        #lin.setFill('green')
        #lin.draw(win)


def drawPoly(cx, cy, size, speed, n):
    global entities, win
    redSquare = shapeSquare(10, 'red')
    for i in range(n):
        x = cx + size * math.cos(2 * math.pi * i / n)
        y = cy + size * math.sin(2 * math.pi * i / n)

        if (i > 0):
            entities.append(FollowerEntity(redSquare, speed, x, y, entities[i-1], 1))
            lin = Line(Point(entities[i].x, entities[i].y), Point(entities[i-1].x, entities[i-1].y))
            lin.setWidth(3)
            lin.draw(win)
        else:
            entities.append(FollowerEntity(redSquare, speed, x, y, None, 1))

    lin = Line(Point(entities[n-1].x, entities[n-1].y), Point(entities[0].x, entities[0].y))
    lin.setWidth(3)
    lin.draw(win)
    entities[0].following = entities[n-1]
    return

def eventLoop():
    global terminate, entities
    i = 0
    while (not terminate):
        i += 1
        for e in range(len(entities)):
            entities[e].move(i)
            if (e > 0):
                lin = Line(Point(entities[e].x, entities[e].y), Point(entities[e-1].x, entities[e-1].y))
            else:
                lin = Line(Point(entities[e].x, entities[e].y), Point(entities[len(entities)-1].x, entities[len(entities)-1].y))
            lin.setWidth(1)
            lin.setFill('green')
            #lin.draw(win)
        if (i > 1000):
            terminate = 1

def bugs():
    global terminate, entities, win, gridsize
    cx = gridsize/2
    cy = gridsize/2
    n = 6
    size = gridsize/4
    speed = 6
    drawPoly(cx, cy, size, speed, n)
    eventLoop()

def orbits():
    global terminate, entities, win, gridsize
    i = 0
    incr0 = 3
    incr1 = 2
    speed = incr1
    n = 7
    radius = 100
    cx = gridsize/2
    cy = gridsize/2
    size = gridsize/4

    blueCircle = shapeCircle(2, 'blue')
    redCircle = shapeCircle(2, 'red')
    greenCircle = shapeCircle(2, 'green')
    yCircle = shapeCircle(6, 'yellow')

    sun = FixedEntity(yCircle, cx, cy)

    earthSpeed = 2 # 30KMPS
    moonSpeed = 7 #1.1 KMPS
    marsSpeed = 6
    rocketSpeed = 4
    earthRadius = radius # 1.5 * 10^8 KM
    moonRadius = radius / 4 # 3.48 * 10^5KM

    startAngle = 45

    entities.append(EllipseEntity(greenCircle, earthSpeed, startAngle, sun, earthRadius*1.5, earthRadius))
    entities.append(EllipseEntity(yCircle, marsSpeed, startAngle, sun, earthRadius*2.5, earthRadius*2.5))
    entities.append(EllipseEntity(greenCircle, moonSpeed, startAngle, entities[0], moonRadius, moonRadius))
    entities.append(FunctionEntity(redCircle, incr0, 100, 200, '50*sin(4*x*2*math.pi/360)**2', 50))
    entities.append(FollowerEntity(blueCircle, rocketSpeed, entities[0].x, entities[0].y, entities[1], 1))

    eventLoop()

def island():
    # On a primitive island there live equal numbers of yellow bellied cowards and red bellied brave warriors.
    # They don't know their own type but can tell others types.
    # How do they pair up (with one yellow and one red) and head out to explore? Being primitive they can't count or communicate.

    global terminate, entities, win, gridsize
    islandRadius = gridsize / 3
    cx = gridsize/2
    cy = gridsize/2
    c1 = Circle(Point(cx, cy), islandRadius)
    c1.setOutline('black')
    c1.setFill('grey')
    c1.draw(win)
    numP = 40
    pspeed = 10

    # Generate people
    persons = []
    redCircle = shapeCircle(2, 'red')
    yellowCircle = shapeCircle(2, 'yellow')
    emptyCircle = shapeCircle(0, 'grey')
    blueCircle = shapeCircle(2, 'blue')

    sun = FixedEntity(emptyCircle, cx, cy)
    terminate = 0
    for p in range(numP):
        r = randint(0,100)
        if (r < 50):
            c = shapeCircle(3, 'yellow')
        else:
            c = shapeCircle(3, 'blue')

        pa = randint(0, 360)
        pr = randint(0, islandRadius)
        px = cx + pr*math.cos(pa)
        py = cy + pr*math.sin(pa)
        persons.append(FollowerEntity(c, pspeed, px, py, None, 1))

    # Move them
    i = 0
    while (not terminate):
        i += 1
        for n0 in range(numP):
            # each person looks at their closest 2 neighbors.
            # If there are similar, they move towards them (say using midpoint).
            # If dissimilar, he moves away from them. Eventually converge into two groups
            p0 = persons[n0]
            minDist = 4 * (islandRadius**2)
            minP1 = n0
            for n1 in range(numP):
                if (n0 == n1):
                    continue
                p1 = persons[n1]
                d1 = (p1.x-p0.x)**2 + (p1.y-p0.y)**2
                if (d1 < minDist):
                    minP1 = n1
                    minDist = d1

            minDist = 4 * islandRadius ** 2
            minP2 = n0
            for n1 in range(numP):
                if ((n1 == n0) or (n1 == minP1)):
                    continue
                p1 = persons[n1]
                d1 = (p1.x-p0.x)**2 + (p1.y-p0.y)**2
                if (d1 < minDist):
                    minP2 = n1
                    minDist = d1

            if ((cx-persons[n0].x)**2 + (cy-persons[n0].y)**2 >= islandRadius**2):
                persons[n0].following = sun
                persons[n0].towards = 1
            else:
                mid = FixedEntity(emptyCircle, (persons[minP1].x + persons[minP2].x)/2, (persons[minP1].y + persons[minP2].y)/2)
                persons[n0].following = mid
                persons[n0].towards = (persons[minP1].shape.color == persons[minP2].shape.color)
            persons[n0].move(i)
        if (i > 1000):
            terminate = 1

def main():
    global terminate, entities, win

    win.setCoords(0, 0, gridsize-1, gridsize-1)
    # orbits()
    island()
    #bugs()
    win.getMouse()
    win.close()

main()
