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

############### Code Overview
# All Puzzle logic is handled within puzzle classes: island, bugs, orbits
# Graphics is handled by Window class which simply draws from ents and fixedShapes lists
# All drawn objects are derived from Entity, which has a shape class and coordinates
# Each entity can either be static, going on an ellipse around another entity,
# tracking towards or away from an entity, or tracking any arbitrary y=f(x) sine etc function
# Shapeclass can be whatever you want: ellipse, square, person, etc.
# Simulation: A timer fires regularly and calls the Puzzle Iterate() to move its entities however it wishes (captured in the list of entities),
# and calls Window to paint from the two lists
############### IDEAS To Do
# Tilted functionEntities
# Split entities on collision
# Entity Contained on another?
# Learning
# Real-time external inputs

ents = []  # moving entities
fixedShapes = [] # fixed entities like background
allStop = 0 # stop rounds
curIter = 0
numIter = 1000
gridsize = 700


## GRAPHICS CLASS. I understand this part the least. It just works.
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

        qbtn = QPushButton('END SIMULATION', self)
        qbtn.clicked.connect(stopLoop)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(gridsize/2, 10)

        sbtn = QPushButton('START', self)
        sbtn.clicked.connect(startTimer)
        sbtn.resize(qbtn.sizeHint())
        sbtn.move(120, 10)

        self.show()

    def drawBorders(ll, ur):
        # ct = Rectangle()
        #ect.draw(win)
        return

    def paintEvent(self, event):
        global ents, fixedShapes, numIter
        self.setWindowTitle("Round: " + str(curIter))
        painter = QPainter(self)

        for i in range(len(fixedShapes)):
            p = fixedShapes[i]
            p.draw(painter)
        for i in range(len(ents)):
            p = ents[i]
            p.draw(painter)

## SHAPES ##############################
class shapeCircle(object):
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def draw(self, x, y, painter, highlight):
        if (self.radius == 0):
            return
        # painter.setPen(QPen(self.color, 1, Qt.SolidLine))
        painter.setBrush(QBrush(self.color, Qt.SolidPattern))
        painter.drawEllipse(x - self.radius, y - self.radius, 2*self.radius, 2*self.radius)
        if (highlight):
            painter.setBrush(QBrush(Qt.green, Qt.SolidPattern))
            painter.drawEllipse(x - self.radius, y - 3*self.radius, 2*self.radius, 2*self.radius)

class shapePoly(object):
    def __init__(self, pts, color):
        self.pts = pts
        self.color = color

    def draw(self, x, y, painter, highlight):
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

    def draw(self, x, y, painter, highlight):
        painter.setBrush(QBrush(self.color, Qt.SolidPattern))
        painter.drawRect(x - self.side/2, y - self.side/2, self.side, self.side)
        if (highlight):
            painter.setBrush(QBrush(Qt.green, Qt.SolidPattern))
            painter.drawEllipse(x - self.side/2, y - 1.5*self.side, self.side, self.side)

class shapePerson(object):
    def __init__(self, width, color):
        self.width = width
        self.color = color
        self.head = width/3
        self.leg = width/2.5

    def draw(self, x, y, painter, highlight):
        # painter.setPen(QPen(self.color, 1, Qt.SolidLine))
        painter.setBrush(QBrush(self.color, Qt.SolidPattern))
        painter.drawEllipse(x - self.head, y - self.width - self.head, 2*self.head, 2*self.head)
        painter.drawRect(x - self.width/2, y - self.width/2, self.width, self.width)
        painter.drawLine(x-self.head, y+self.width/2, x-self.head, y+self.width+self.leg)
        painter.drawLine(x+self.head, y+self.width/2, x+self.head, y+self.width+self.leg)

        if (highlight):
            painter.setBrush(QBrush(Qt.green, Qt.SolidPattern))
            painter.drawEllipse(x - self.head, y - self.width - 3*self.head, 2*self.head, 2*self.head)


## ENTITIES ##############################
class Entity(object):
    def __init__(self, shape, speed, x, y):
        self.shape = shape
        self.speed = speed
        self.x = x
        self.y = y
        self.pastx = []
        self.pasty = []
        self.highlight = 0
        self.tilt = 0

    def doHighlight(self):
        self.highlight = 1

    def draw(self, painter):
        if (trace):
            self.pastx.append(self.x)
            self.pasty.append(self.y)
            for i in range(len(self.pastx)):
                self.shape.draw(self.pastx[i], self.pasty[i], painter, self.highlight)
        else:
            self.shape.draw(self.x, self.y, painter, self.highlight)

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
    def __init__(self, shape, speed, angle, cobj, rx, ry, tiltAngle):
        Entity.__init__(self, shape, speed, 0, 0)
        self.rx = rx
        self.ry = ry
        self.center = cobj
        self.setAngle(angle)
        self.perimeter = 2 * math.pi * sqrt((rx**2 + ry**2)/2)
        self.dist = self.angle * self.perimeter / 360
        self.tilt = tiltAngle

    def setAngle(self, angle):
        self.angle = angle
        theta = 2 * math.pi * self.angle/360
        r = (self.rx * self.ry) / sqrt((self.rx**2 * (sin(theta))**2) + (self.ry**2 * (cos(theta))**2))
        self.x = self.center.x + r*math.cos(theta + 2 * math.pi * self.tilt/360)
        self.y = self.center.y + r*math.sin(theta+ 2 * math.pi * self.tilt/360)

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

## PUZZLES ##############################
class Puzzle():
    def __init__(self, tr):
        global trace, gridsize
        self.entities = []
        trace = tr
        self.cx = gridsize/2
        self.cy = gridsize/2

    def Entities(self):
        return self.entities

    def iterate(self, num):
        for e in range(len(self.entities)):
            self.entities[e].move()

# bugs crawling towards each other on a polygon
class bugs(Puzzle):
    def __init__(self, n):
        global gridsize
        Puzzle.__init__(self, 1)
        self.sides = n
        size = gridsize/4
        speed = 6
        self.createPoly(self.cx, self.cy, size, speed, self.sides)

    def createPoly(self, cx, cy, size, speed, n):
        global fixedShapes
        redSquare = shapeSquare(10, Qt.red)
        pts = []
        for i in range(n):
            x = cx + size * math.cos(2 * math.pi * i / n)
            y = cy + size * math.sin(2 * math.pi * i / n)
            pts.append(QPointF(x, y))
            if (i > 0):
                self.entities.append(FollowerEntity(redSquare, speed, x, y, self.entities[i-1], 1))
            else:
                self.entities.append(FollowerEntity(redSquare, speed, x, y, None, 1))
        self.entities[0].following = self.entities[n-1]
        fixedShapes.append(FixedEntity(shapePoly(pts, Qt.white), 0, 0))

class orbits(Puzzle):
    def __init__(self):
        global gridsize
        Puzzle.__init__(self, 1)
        speed = 2
        n = 7
        radius = 100
        size = gridsize/4

        blueCircle = shapeCircle(2, Qt.blue)
        redCircle = shapeCircle(2, Qt.red)
        greenCircle = shapeCircle(2, Qt.green)
        yCircle = shapeCircle(6, Qt.yellow)
        sun = FixedEntity(yCircle, self.cx, self.cy)

        earthSpeed = 20 # 30KMPS
        moonSpeed = 40 #1.1 KMPS
        marsSpeed = 20
        rocketSpeed = 4
        earthRadius = radius # 1.5 * 10^8 KM
        moonRadius = radius / 4 # 3.48 * 10^5KM

        startAngle = 0
        self.entities = []
        self.entities.append(EllipseEntity(blueCircle, earthSpeed, startAngle, sun, earthRadius*3.5, earthRadius, 30))
        self.entities.append(EllipseEntity(redCircle, marsSpeed, startAngle, sun, earthRadius*2.5, earthRadius, -45))
        self.entities.append(EllipseEntity(greenCircle, moonSpeed, startAngle, self.entities[0], moonRadius, moonRadius, 0))
        self.entities.append(FunctionEntity(redCircle, speed, 100, 200, '50*sin(4*x*2*math.pi/360)**2', 50))
        # self.entities.append(FollowerEntity(blueCircle, rocketSpeed, self.entities[0].x, self.entities[0].y, self.entities[1], 1))
        self.entities.append(sun)
        self.entities[3].doHighlight()

    def iterate(self, num):
        for e in range(len(self.entities)):
            self.entities[e].move()

class island(Puzzle):
    # On a primitive island there live equal numbers of yellow bellied cowards and red bellied brave warriors.
    # They don't know their own type but can tell others types.
    # How do they pair up (with one yellow and one red) and head out to explore? Being primitive they can't count or communicate.
    def __init__(self):
        global gridsize, painter, fixedShapes
        Puzzle.__init__(self, 0)
        self.islandRadius = (int) (gridsize / 3)
        self.numP = 40
        self.pspeed = 10

        # Generate people
        self.entities = []
        self.redCircle = shapePerson(6, Qt.red)
        self.yellowCircle = shapePerson(6, Qt.yellow)
        self.blueCircle = shapePerson(6, Qt.blue)
        self.emptyCircle = shapeCircle(0, Qt.white)
        self.border = FixedEntity(shapeCircle(self.islandRadius, Qt.white), self.cx, self.cy)
        self.sun = FixedEntity(self.emptyCircle, self.cx, self.cy)
        fixedShapes.append(self.border)
        self.random = []

        # a fraction of them are shapeshifters: they shift color on each move!
        prando = 10

        for p in range(self.numP):
            r = randint(0,100)
            if (r < 50):
                c = self.redCircle
            else:
                c = self.blueCircle
            pa = randint(0, 360)
            pr = randint(0, self.islandRadius)
            px = self.cx + pr*math.cos(pa)
            py = self.cy + pr*math.sin(pa)
            self.entities.append(FollowerEntity(c, self.pspeed, px, py, None, 1))
            self.random.append(randint(0,100) < prando)
            if (self.random[p]):
                self.entities[p].doHighlight()

    def iterate(self, iter):
        for n0 in range(self.numP):
            # each person looks at their closest 2 neighbors.
            # If there are similar, they move towards them (say using midpoint).
            # If dissimilar, he moves away from them. Eventually converge into two groups
            p0 = self.entities[n0]
            if (self.random[n0]):
                if (p0.shape.color == Qt.blue):
                    p0.shape = self.redCircle
                else:
                    p0.shape = self.blueCircle
            minDist = 4 * (self.islandRadius**2)
            minP1 = n0
            for n1 in range(self.numP):
                if (n0 == n1):
                    continue
                p1 = self.entities[n1]
                d1 = (p1.x-p0.x)**2 + (p1.y-p0.y)**2
                if (d1 < minDist):
                    minP1 = n1
                    minDist = d1
            minDist = 4 * self.islandRadius ** 2
            minP2 = n0
            for n1 in range(self.numP):
                if ((n1 == n0) or (n1 == minP1)):
                    continue
                p1 = self.entities[n1]
                d1 = (p1.x-p0.x)**2 + (p1.y-p0.y)**2
                if (d1 < minDist):
                    minP2 = n1
                    minDist = d1
            # dont let it go outside the island
            if ((self.cx-self.entities[n0].x)**2 + (self.cy-self.entities[n0].y)**2 >= self.islandRadius**2):
                self.entities[n0].following = self.sun
                self.entities[n0].towards = 1
            else:
                mid = FixedEntity(self.emptyCircle, (self.entities[minP1].x + self.entities[minP2].x)/2, \
                                (self.entities[minP1].y + self.entities[minP2].y)/2)
                self.entities[n0].following = mid
                self.entities[n0].towards = (self.entities[minP1].shape.color == self.entities[minP2].shape.color)
            self.entities[n0].move()

## SIMULATION ITERATOR ##############################
def startTimer():
    global numIter, curIter, window, prob, ents
    # print("in timer: ", curIter, numIter)
    if (allStop or (curIter >= numIter)):
        endProgram()
        return
    curIter += 1
    prob.iterate(curIter)
    ents = prob.Entities()
    window.update()
    threading.Timer(0.3, startTimer).start()

def stopLoop():
    global allStop
    allStop = 1

def endProgram():
    sys.exit(0)

def main():
    global window, painter, prob, ents

    seed(datetime.now().microsecond)
    App = QApplication(sys.argv)
    window = Window()

    ## SELECT the problem you want to simulate, comment the rest
    # prob = orbits()
    # prob = bugs(5) # takes number of bugs
    prob = island()

    ents = prob.Entities()
    window.InitWindow()
    window.update()
    ## startTimer() <-- uncomment to auto start the program
    sys.exit(App.exec_())
main()
