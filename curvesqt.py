from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip,QPushButton, QLabel, QWidget, QVBoxLayout
from PyQt5.QtGui import QPainter, QBrush, QPen, QPixmap
from PyQt5.QtCore import Qt, QPointF
import threading
import math
from math import *
from random import seed, randint, random
import sys
from datetime import datetime
import numpy as np

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


## GRAPHICS CLASS. I understand this part the least. It just works.
class Window(QMainWindow):
    def __init__(self, gridsize):
        global painter
        super().__init__()
        self.title = "Curves Curves"
        self.top= 0
        self.left= 0
        self.gridsize = gridsize
        self.width = gridsize
        self.height = gridsize
        self.ents = []  # moving entities
        self.fixedShapes = [] # fixed entities like background
        self.connectors = [] # lines to connect entities
        # self.InitWindow(puzl)

    def InitWindow(self, puzl):
        self.puzl = puzl
        self.ents = puzl.Entities()
        self.fixedShapes = puzl.FixedShapes()
        self.connectors = puzl.Connectors()
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

        qbtn = QPushButton('END SIMULATION', self)
        qbtn.clicked.connect(lambda: stopLoop(puzl))
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(self.gridsize/2, 10)

        sbtn = QPushButton('START', self)
        sbtn.clicked.connect(lambda: startTimer(puzl, self))
        sbtn.resize(qbtn.sizeHint())
        sbtn.move(120, 10)

        self.show()

    def drawBorders(ll, ur):
        # ct = Rectangle()
        #ect.draw(win)
        return

    def paintEvent(self, event):
        self.setWindowTitle(self.title)
        painter = QPainter(self)

        for i in range(len(self.fixedShapes)):
            p = self.fixedShapes[i]
            p.draw(painter)
        for i in range(len(self.ents)):
            p = self.ents[i]
            p.draw(painter)
        self.connectors = self.puzl.Connectors()
        for i in range(len(self.connectors)):
            e1 = self.connectors[i]["e1"]
            e2 = self.connectors[i]["e2"]
            painter.drawLine(e1["x"], e1["y"], e2["x"], e2["y"])

## SHAPES ##############################
class Shape(object):
    def __init__(self, color, size):
        self.color = color
        self.boundingRadius = size

class shapeCircle(Shape):
    def __init__(self, radius, color):
        Shape.__init__(self, color, radius)
        self.radius = radius

    def draw(self, x, y, painter, highlight):
        if (self.radius == 0):
            return
        # painter.setPen(QPen(self.color, 1, Qt.SolidLine))
        painter.setBrush(QBrush(self.color, Qt.SolidPattern))
        painter.drawEllipse(x - self.radius, y - self.radius, 2*self.radius, 2*self.radius)
        if (highlight):
            painter.setBrush(QBrush(Qt.green, Qt.SolidPattern))
            painter.drawEllipse(x - self.radius, y - 3*self.radius, 2*self.radius, 2*self.radius)

class shapePoly(Shape):
    def __init__(self, pts, color, boundingRadius):
        Shape.__init__(self,color, boundingRadius)
        self.pts = pts

    def draw(self, x, y, painter, highlight):
        # painter.setPen(QPen(self.color, 1, Qt.SolidLine))
        polygon = QtGui.QPolygonF()
        for i in range(len(self.pts)):
            polygon.append(self.pts[i])
        painter.setBrush(QBrush(self.color, Qt.SolidPattern))
        painter.drawPolygon(polygon)

class shapeSquare(Shape):
    def __init__(self, side, color):
        Shape.__init__(self,color, side/2)
        self.side = side
        self.firm = 1

    def draw(self, x, y, painter, highlight):
        painter.setBrush(QBrush(self.color, Qt.SolidPattern))
        painter.drawRect(x - self.side/2, y - self.side/2, self.side, self.side)
        if (highlight):
            painter.setBrush(QBrush(Qt.green, Qt.SolidPattern))
            painter.drawEllipse(x - self.side/2, y - 1.5*self.side, self.side, self.side)

class shapePerson(Shape):
    def __init__(self, width, color):
        Shape.__init__(self, color, width)
        self.width = width
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
    def __init__(self, shape, speed, x, y, tr):
        self.shape = shape
        self.speed = speed
        self.x = x
        self.y = y
        self.pastx = []
        self.pasty = []
        self.highlight = 0
        self.tilt = 0
        self.trace = tr

    def doHighlight(self):
        self.highlight = 1

    def bounce(self):
        return

    def draw(self, painter):
        if (self.trace):
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
    def __init__(self, shape, x, y, trace):
        Entity.__init__(self, shape, 0, x, y, trace)
        self.x = x
        self.y = y

    def move(self):
        return

class EllipseEntity(Entity):
    def __init__(self, shape, speed, angle, cobj, rx, ry, tiltAngle, trace):
        Entity.__init__(self, shape, speed, 0, 0, trace)
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

def degToRadian(angle):
    return (angle * math.pi / 180)

# follows a n-sided polygon trajectory
class PolygonEntity(Entity):
    def __init__(self, shape, speed, angle, cobj, nsides, sidelength, tiltAngle, trace):
        Entity.__init__(self, shape, speed, 0, 0, trace)
        self.nsides = nsides
        self.center = cobj
        self.sidelength = sidelength
        self.perimeter = self.nsides * self.sidelength
        self.tilt = tiltAngle
        self.corners = []
        self.sectorAngle = 360 / self.nsides
        self.angle = angle
        self.dist = self.angle * self.perimeter / 360
        self.apothem = self.sidelength / (2 * math.tan(degToRadian(180 / self.nsides)))
        self.setAngle(self.angle)

    def setAngle(self, angle):
        self.angle = angle
        sideAngle = self.sectorAngle * round(angle / self.sectorAngle)
        sideNormalX = math.cos(degToRadian(sideAngle + self.tilt))
        sideNormalY = math.sin(degToRadian(sideAngle + self.tilt))
        sideward = self.apothem * math.tan(degToRadian(angle - sideAngle))
        self.x = self.center.x + sideNormalX * self.apothem - sideNormalY * sideward
        self.y  = self.center.y + sideNormalY * self.apothem + sideNormalX * sideward

    def move(self):
        self.dist += self.speed
        self.angle = (self.dist * 360 / self.perimeter)
        if (self.angle >= 360):
            self.angle -= 360
            self.dist = 0
        self.setAngle(self.angle)

# added BoundedBox trajectory: entity moves along a random st. line,
# bouncing within a box (or can randomly change angle at each step)
class BoundedBoxEntity(Entity):
    def __init__(self, shape, speed, x, y, lx, ly, ux, uy, rando, trace):
        Entity.__init__(self, shape, speed, x, y, trace)
        self.y = y
        self.x = x
        self.lx = lx
        self.ly = ly
        self.ux = ux
        self.uy = uy
        self.random = rando
        self.angle = randint(0, 360)

    def bounce(self):
        self.angle = 180 - self.angle

    def move(self):
        dx = self.speed * math.cos(2 * math.pi * self.angle / 360)
        dy = self.speed * math.sin(2 * math.pi * self.angle / 360)
        nx = self.x + dx
        ny = self.y + dy
        na = self.angle
        if (self.random):
            na = randint(0, 360)
        if ((nx <= self.lx) or (nx >= self.ux)):
            nx -= dx
            na = 180 - self.angle
        elif ((ny <= self.ly) or (ny >= self.uy)):
            na = 360 - self.angle
            ny -= dy
        self.x = nx
        self.y = ny
        self.angle = na

# follows a random function. CAREFUL! USES EVAL()
class FunctionEntity(Entity):
    def __init__(self, shape, speed, ix, iy, expr, bound, trace):
        Entity.__init__(self, shape, speed, ix, iy, trace)
        self.expr = expr
        self.dist = 0
        self.iy = iy
        self.ix = ix
        self.bound = bound

    def move(self):
        nx = self.x
        nx += self.speed
        if (nx >= self.bound):
            nx = self.ix
        # ny = self.iy + self.amp * (math.sin(4 * nx * math.pi / 360)) #
        x = nx
        ny = self.iy + eval(self.expr)

        self.x = nx
        self.y = ny


# goes towards or away from another entity
class FollowerEntity(Entity):
    def __init__(self, shape, speed, x, y, fid, towards, trace):
        Entity.__init__(self, shape, speed, x, y, trace)
        self.following = fid
        self.dist = 0
        self.towards = towards

    def move(self):
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


def colliding(e1, e2):
    return ( ((e1.x - e2.x)**2 + (e1.y-e2.y)**2) <= (e1.shape.boundingRadius + e2.shape.boundingRadius)**2)

def detectCollisions(ents):
    colls = []
    for i in range(len(ents)):
        for j in range(i+1, len(ents)):
            if (colliding(ents[i], ents[j])):
                colls.append({"e1":i, "e2":j})
    return colls

## SIMULATION ITERATOR ##############################

def startTimer(puzl, win):
    global window
    # print("in timer: ", curIter, numIter)
    if (puzl.allStop or (puzl.curIter >= puzl.numIter)):
        endProgram()
        return
    puzl.curIter += 1
    puzl.iterate(puzl.curIter)
    win.title = "Round: " + str(puzl.curIter)
    win.update()
    threading.Timer(0.3, startTimer, [puzl, win]).start()

def stopLoop(puzl):
    puzl.allStop = 1

def endProgram():
    sys.exit(0)
