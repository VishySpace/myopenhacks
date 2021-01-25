from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip,QPushButton, QLabel, QWidget, QVBoxLayout
from PyQt5.QtGui import QPainter, QBrush, QPen, QPixmap
from PyQt5.QtCore import Qt, QPointF
import threading
import math
from math import *
from random import seed, randint
import sys
from datetime import datetime
ents = []
allStop = 0
curIter = 0
numIter = 1000
trace = 0

terminate = 0
gridsize = 700
width = 500
height = gridsize / 2
xoffset = (gridsize - width)  / 2
yoffset = (gridsize - height) / 2
fixedShapes = []

# seed random number generator
dt = datetime.now()
sd = dt.microsecond
seed(sd)
# generate some integers


class Window(QMainWindow):
    def __init__(self):
        global painter
        super().__init__()
        self.title = "Curves Curves"
        self.top= 0
        self.left= 0
        self.width = gridsize
        self.height = gridsize
        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

        qbtn = QPushButton('Stop', self)
        qbtn.clicked.connect(stopLoop)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(gridsize/2, 10)

        sbtn = QPushButton('Start', self)
        sbtn.clicked.connect(startTimer)
        sbtn.resize(qbtn.sizeHint())
        sbtn.move(xoffset+10, 10)
        self.show()

    def drawBorders(ll, ur):
        # ct = Rectangle()
        #ect.draw(win)
        return

    def paintEvent(self, event):
        global ents, fixedShapes
        painter = QPainter(self)
        for i in range(len(fixedShapes)):
            p = fixedShapes[i]
            p.draw(painter)
        for i in range(len(ents)):
            p = ents[i]
            p.draw(painter)

class shapeCircle(object):
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def draw(self, x, y, painter):
        if (self.radius == 0):
            return
        # painter.setPen(QPen(self.color, 1, Qt.SolidLine))
        painter.setBrush(QBrush(self.color, Qt.SolidPattern))
        painter.drawEllipse(x - self.radius, y - self.radius, 2*self.radius, 2*self.radius)
        return

class shapePoly(object):
    def __init__(self, pts, color):
        self.pts = pts
        self.color = color

    def draw(self, x, y, painter):
        # painter.setPen(QPen(self.color, 1, Qt.SolidLine))
        polygon = QtGui.QPolygonF()
        for i in range(len(self.pts)):
            polygon.append(self.pts[i])
        painter.setBrush(QBrush(self.color, Qt.SolidPattern))
        painter.drawPolygon(polygon)

class shapeSquare(object):
    def __init__(self, side, color):
        self.side = side
        self.color = color

    def draw(self, x, y, painter):
        painter.setBrush(QBrush(self.color, Qt.SolidPattern))
        painter.drawRect(x - self.side/2, y - self.side/2, self.side, self.side)

class Entity(object):
    def __init__(self, shape, speed, x, y):
        self.shape = shape
        self.speed = speed
        self.x = x
        self.y = y
        self.pastx = []
        self.pasty = []

    def draw(self, painter):
        if (trace):
            self.pastx.append(self.x)
            self.pasty.append(self.y)
            for i in range(len(self.pastx)):
                self.shape.draw(self.pastx[i], self.pasty[i], painter)
        else:
            self.shape.draw(self.x, self.y, painter)
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

    def move(self):
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

    def move(self):
        nx = self.x
        nx += self.speed
        if (nx >= gridsize):
            nx = self.ix
        ny = self.iy + self.amp * (math.sin(4 * nx * math.pi / 360)) #
        x = nx
        ny = self.iy + eval(self.expr)
        self.x = nx
        self.y = ny

class FollowerEntity(Entity):
    def __init__(self, shape, speed, x, y, fid, towards):
        Entity.__init__(self, shape, speed, x, y)
        self.following = fid
        self.dist = 0
        self.towards = towards

    def move(self):
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

        #lin = Line(Point(x, y), Point(xf, yf))
        #lin.setWidth(1)
        #lin.setFill('green')
        #lin.draw(win)


def drawPoly(cx, cy, size, speed, n):
    global fixedShapes
    entities = []
    redSquare = shapeSquare(10, Qt.red)
    pts = []
    for i in range(n):
        x = cx + size * math.cos(2 * math.pi * i / n)
        y = cy + size * math.sin(2 * math.pi * i / n)
        pts.append(QPointF(x, y))
        if (i > 0):
            entities.append(FollowerEntity(redSquare, speed, x, y, entities[i-1], 1))
        else:
            entities.append(FollowerEntity(redSquare, speed, x, y, None, 1))
    entities[0].following = entities[n-1]
    fixedShapes.append(FixedEntity(shapePoly(pts, Qt.white), 0, 0))
    return entities

class bugs():
    def __init__(self):
        global gridsize
        cx = gridsize/2
        cy = gridsize/2
        n = 6
        size = gridsize/4
        speed = 6
        self.entities = drawPoly(cx, cy, size, speed, n)

    def iterate(self, num):
        for e in range(len(self.entities)):
            self.entities[e].move()
        return self.entities

class orbits():
    def __init__(self):
        global gridsize
        incr0 = 3
        incr1 = 2
        speed = incr1
        n = 7
        radius = 100
        cx = gridsize/2
        cy = gridsize/2
        size = gridsize/4

        blueCircle = shapeCircle(2, Qt.blue)
        redCircle = shapeCircle(2, Qt.red)
        greenCircle = shapeCircle(2, Qt.green)
        yCircle = shapeCircle(6, Qt.yellow)

        sun = FixedEntity(yCircle, cx, cy)

        earthSpeed = 2 # 30KMPS
        moonSpeed = 7 #1.1 KMPS
        marsSpeed = 6
        rocketSpeed = 4
        earthRadius = radius # 1.5 * 10^8 KM
        moonRadius = radius / 4 # 3.48 * 10^5KM

        startAngle = 45
        self.entities = []
        self.entities.append(EllipseEntity(blueCircle, earthSpeed, startAngle, sun, earthRadius*1.5, earthRadius))
        self.entities.append(EllipseEntity(yCircle, marsSpeed, startAngle, sun, earthRadius*2.5, earthRadius*2.5))
        self.entities.append(EllipseEntity(greenCircle, moonSpeed, startAngle, self.entities[0], moonRadius, moonRadius))
        self.entities.append(FunctionEntity(redCircle, incr0, 100, 200, '50*sin(4*x*2*math.pi/360)**2', 50))
        self.entities.append(FollowerEntity(blueCircle, rocketSpeed, self.entities[0].x, self.entities[0].y, self.entities[1], 1))
        self.entities.append(sun)

    def iterate(self, num):
        for e in range(len(self.entities)):
            self.entities[e].move()
        return self.entities

class island():
    # On a primitive island there live equal numbers of yellow bellied cowards and red bellied brave warriors.
    # They don't know their own type but can tell others types.
    # How do they pair up (with one yellow and one red) and head out to explore? Being primitive they can't count or communicate.
    def __init__(self):
        global gridsize, painter, fixedShapes
        self.islandRadius = (int) (gridsize / 3)
        self.cx = gridsize/2
        self.cy = gridsize/2
        self.numP = 40
        self.pspeed = 10

        # Generate people
        self.persons = []
        redCircle = shapeCircle(2, Qt.red)
        yellowCircle = shapeCircle(2, Qt.yellow)
        self.emptyCircle = shapeCircle(0, Qt.white)
        blueCircle = shapeCircle(2, Qt.blue)
        self.border = FixedEntity(shapeCircle(self.islandRadius, Qt.white), self.cx, self.cy)
        self.sun = FixedEntity(self.emptyCircle, self.cx, self.cy)
        fixedShapes.append(self.border)
        for p in range(self.numP):
            r = randint(0,100)
            if (r < 50):
                c = shapeCircle(3, Qt.red)
            else:
                c = shapeCircle(3, Qt.blue)

            pa = randint(0, 360)
            pr = randint(0, self.islandRadius)
            px = self.cx + pr*math.cos(pa)
            py = self.cy + pr*math.sin(pa)
            self.persons.append(FollowerEntity(c, self.pspeed, px, py, None, 1))



    def iterate(self, iter):
        for n0 in range(self.numP):
            # each person looks at their closest 2 neighbors.
            # If there are similar, they move towards them (say using midpoint).
            # If dissimilar, he moves away from them. Eventually converge into two groups
            p0 = self.persons[n0]
            minDist = 4 * (self.islandRadius**2)
            minP1 = n0
            for n1 in range(self.numP):
                if (n0 == n1):
                    continue
                p1 = self.persons[n1]
                d1 = (p1.x-p0.x)**2 + (p1.y-p0.y)**2
                if (d1 < minDist):
                    minP1 = n1
                    minDist = d1

            minDist = 4 * self.islandRadius ** 2
            minP2 = n0
            for n1 in range(self.numP):
                if ((n1 == n0) or (n1 == minP1)):
                    continue
                p1 = self.persons[n1]
                d1 = (p1.x-p0.x)**2 + (p1.y-p0.y)**2
                if (d1 < minDist):
                    minP2 = n1
                    minDist = d1
            if ((self.cx-self.persons[n0].x)**2 + (self.cy-self.persons[n0].y)**2 >= self.islandRadius**2):
                self.persons[n0].following = self.sun
                self.persons[n0].towards = 1
            else:
                mid = FixedEntity(self.emptyCircle, (self.persons[minP1].x + self.persons[minP2].x)/2, \
                                (self.persons[minP1].y + self.persons[minP2].y)/2)
                self.persons[n0].following = mid
                self.persons[n0].towards = (self.persons[minP1].shape.color == self.persons[minP2].shape.color)
            self.persons[n0].move()

        return self.persons

def stopLoop():
    global allStop
    allStop = 1

def startTimer():
    global numIter, curIter, window, prob, ents
    # print("in timer: ", curIter, numIter)
    if (allStop or (curIter >= numIter)):
        endProgram()
        return
    curIter += 1
    ents = prob.iterate(curIter)
    window.update()
    threading.Timer(0.3, startTimer).start()

def endProgram():
    sys.exit(0)

def main():
    global window, painter, prob,trace

    App = QApplication(sys.argv)
    window = Window()
    trace = 0
    #prob = orbits()
    prob = island()
    #prob = bugs()
    window.InitWindow()
    startTimer()
    sys.exit(App.exec_())
main()
