from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip,QPushButton, QLabel, QWidget, QVBoxLayout
from PyQt5.QtGui import QPainter, QBrush, QPen, QPixmap
from PyQt5.QtCore import Qt
import math
from random import seed
from random import randint
import sys
import enum
from datetime import datetime


argv = ["covid.py", -1, 1, 200, 80, 100, 0, 0, 0.5, 0]
argc = len(argv)
if (argc < 10):
    print ("Usage: covid.py Seed Visual NumPeople NumDays PctMoving PctICUBeds PctVax PctSick PctQuarantine")
    print ("Seed: -1 to generate random seed, number to use a specific seed")
    print ("StepMode: click after each day")
    print ("Pct: Percent")
    exit()
print("##", argv)
sd = int(argv[1])
if (sd <= 0):
    dt = datetime.now()
    sd = dt.microsecond
seed(sd)
visual = int(argv[2])
numPeople = int(argv[3])
numIter = int(argv[4])

# Scenarios to simulate
pctMoving = int(argv[5])
pctHospCapacity = int(argv[6])
hospCapacity = numPeople * pctHospCapacity/100
pctInitialVax = int(argv[7])
pctInitialInfected = 0.1 # int(argv[8])
pctQuarantine = int(argv[9])

# mostly fixed controls
class AllParams(object):
    def __init__(self):
        self.pctRecoveryWithCare = 90
        self.daysToRecoverWithCare = 600
        self.daysToDeathWithCare = 1400
        self.pctRecoveryWithNoCare = 5
        self.daysToRecoverWithNoCare = 2000
        self.daysToDeathWithNoCare = 2000
pars = AllParams()

# layout constants
gridsize = 700
width = 500
height = gridsize / 2
xoffset = (gridsize - width)  / 2
yoffset = (gridsize - height) / 2
radius = 5.0
ll = {'x': xoffset, 'y':yoffset}
lr = {'x':xoffset+width, 'y':yoffset}
ul = {'x':xoffset, 'y':yoffset+height}
ur = {'x':xoffset+width, 'y':yoffset+height}
moveDist = 4
curIter = 0

# counts
numInitMoving = 0
numDead = 0
numInfected = 0
numRecovered = 0
currentInfected = 0
numInitVax = 0
numInitInfected = 0
hospBeds = hospCapacity

statsText = ""
persons = []
allStop = 0
def stopLoop():
    global allStop
    allStop = 1

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "COVID-19 Simulator"
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
        global ll, ur, persons, radius
        painter = QPainter(self)
        painter.setPen(QPen(Qt.green,  2, Qt.DashLine))
        for i in range(numPeople):
            p = persons[i]
            painter.setPen(QPen(colorCode(p.color), 1, Qt.SolidLine))
            painter.setBrush(QBrush(colorCode(p.color), Qt.SolidPattern))
            painter.drawEllipse(p.cx, p.cy, 2*radius, 2*radius)
            if (p.infector != -1):
                painter.drawLine(p.cx, p.cy, persons[p.infector].cx, persons[p.infector].cy)


def colorCode(c):
    if (c == 'green'):
        return Qt.green
    if (c == 'red'):
        return Qt.red
    if (c == 'blue'):
        return Qt.blue
    if (c == 'yellow'):
        return Qt.yellow
    if (c == 'black'):
        return Qt.black
    return Qt.white

class Hstatus(enum.Enum):
    Healthy = 1
    Infected = 2
    Immune = 3
    Recovered = 4
    Dead = 5

class Person(object):
    def __init__(self, id):
        global numInfected, currentInfected, numInitInfected, numInitVax
        global ll, lr, ul, ur, numInitMoving, persons

        if (randint(0, 100) < pctMoving):
            self.moving = 1
            numInitMoving += 1
        else:
            self.moving = 0
        self.id = id
        self.angle = randint(0, 359)
        self.cx = randint(ll['x'], lr['x'])
        self.cy = randint(ll['y'], ul['y'])
        self.color = 'green'
        self.daysInfected = 0
        self.InHospital = 0
        self.status = Hstatus.Healthy
        self.prognosis = 1
        self.daysToDeath = 0
        self.daysToRecover = 0
        self.inQuarantine = 0
        self.infector = -1

        if (randint(0,100) < pctInitialInfected):
            self.makeInfect()
            numInitInfected += 1
            self.infector = self.id
        elif (randint(0,100) < pctInitialVax):
            self.color = 'green'
            self.status = Hstatus.Immune
            numInitVax += 1
        else:
            self.color = 'blue'
            self.status = Hstatus.Healthy


    def admitHospital(self):
        global hospBeds
        if (self.InHospital):
            return 1
        if (hospBeds <= 0):
            if (randint(0, 100) <= pctQuarantine):
                self.inQuarantine = 1
            else:
                self.inQuarantine = 0
            if (randint(0,100) <= pars.pctRecoveryWithNoCare):
                self.prognosis = 1
                self.daysToRecover = pars.daysToRecoverWithNoCare
            else:
                self.prognosis = 0
                self.daysToDeath = pars.daysToDeathWithNoCare
            return 0

        hospBeds -= 1
        self.InHospital = 1
        self.inQuarantine = 1
        if (randint(0,100) <= pars.pctRecoveryWithCare):
            self.prognosis = 1
            self.daysToRecover = pars.daysToRecoverWithCare
        else:
            self.prognosis = 0
            self.daysToDeath = pars.daysToDeathWithCare
        return 1

    def releaseHospital(self):
        global hospBeds
        if (self.InHospital):
            self.inQuarantine = 0
            self.InHospital = 0
            hospBeds += 1
            self.prognosis = 1
            return 1
        return 1

    def isMobile(self):
        if (self.status == Hstatus.Infected and self.inQuarantine):
            return 0
        return (self.status != Hstatus.Dead and self.moving and (not self.InHospital))

    def movePerson(self):
        global ll, lr, ul, ur
        if (not self.isMobile()):
            return
        dx = moveDist * math.cos(2 * math.pi * self.angle / 360)
        dy = moveDist * math.sin(2 * math.pi * self.angle / 360)
        self.cx += dx
        self.cy += dy
        if ((self.cx <= ll['x']) or (self.cx >= lr['x'])):
            self.cx -= dx
            self.angle = 180 - self.angle
        elif ((self.cy <= ll['y']) or (self.cy >= ul['y'])):
            self.angle = 360 - self.angle
            self.cy -= dy
        elif (randint(0, 100) < 30):
            self.angle = randint(0, 359)

    def makeInfect(self):
        global numInfected, currentInfected
        if (self.status != Hstatus.Healthy):
            return
        self.status = Hstatus.Infected
        self.color = 'red'
        self.daysInfected = 0
        numInfected += 1
        currentInfected += 1
        self.admitHospital()

    def makeDead(self):
        global currentInfected, numDead
        self.status = Hstatus.Dead
        self.releaseHospital()
        currentInfected -= 1
        self.moving = 0
        numDead += 1
        self.color = 'black'

    def makeRecover(self):
        global numRecovered, currentInfected
        self.status = Hstatus.Recovered
        numRecovered += 1
        currentInfected -= 1
        self.releaseHospital()
        self.color = 'yellow'

    def updateRecovery(self):
        if (self.status != Hstatus.Infected):
            return
        self.daysInfected += 1
        if (self.prognosis) :
            if (self.daysInfected >= self.daysToRecover):
                self.makeRecover()
                return
        else:
            if (self.daysInfected >= self.daysToDeath):
                self.makeDead()
                return

def areTouching(p1, p2):
    x1 = p1.cx
    x2 = p2.cx
    y1 = p1.cy
    y2 = p2.cy

    if ((abs(x1-x2) <= 2.1*radius) and (abs(y1-y2) <= 2.1*radius)):
        return 1
    return 0

def updateLabel():
    print(str(curIter) + ',' + str(numInfected) + \
                    ',' + str(numRecovered) +
                    ',' + str(numDead) + \
                    ',' + str(currentInfected) + \
                    ',' + str(hospBeds))
    if (not visual):
        return
    #label.setText('Day: ' + str(curIter) + \
     #               '\nTotal Infected: ' + str(numInfected) + \
      #              '\nRecovered: ' + str(numRecovered) +
       #             '\nDead: ' + str(numDead) + \
        #            '\nCurrent Infected: ' + str(currentInfected) + \
         #           '\nICU Beds Remaining: ' + str(hospBeds))

def updateStatus(p1, p2):
    global numInfected, label, currentInfected, hospBeds
    if (p1.InHospital or p2.InHospital):
        return
    if (p1.inQuarantine and p1.status == Hstatus.Infected):
        return
    if (p2.inQuarantine and p2.status == Hstatus.Infected):
        return
    if (p1.status != Hstatus.Infected and p2.status != Hstatus.Infected):
        return
    if (p1.status == Hstatus.Infected and p2.status == Hstatus.Infected):
        return
    if (areTouching(p1, p2)):
        if ((p1.status == Hstatus.Infected) and (p2.status == Hstatus.Healthy)):
            p2.makeInfect()
            p2.infector = p1.infector
        elif ((p2.status == Hstatus.Infected) and (p1.status == Hstatus.Healthy)):
            p1.makeInfect()
            p1.infector = p2.infector

def printResults():
    print("## ----------- OUTPUT -----------")
    print("##STARTING PARAMETERS: Num People", numPeople, 'Mobile', numInitMoving, \
        'ICU Beds', hospCapacity, 'Vaccinated', numInitVax, 'Infected', numInitInfected, \
        "Pct. Quarantine",  pctQuarantine, "seed", sd)
    print("##HEALTH PARAMETERS: ", pars.__dict__)
    print("##RESULT**: Num Days", curIter, "Num Dead", numDead, "Total Infected", numInfected)

def displayParams():
    pstr = 'Parameters' + \
            '\nPeople: ' + str(numPeople) + \
            '\nMobile: ' + str(numInitMoving) + \
            '\nICU Beds: ' + str(hospCapacity) + \
            '\nInitial Vax: ' + str(numInitVax) + \
            '\nInitial Infected: ' + str(numInitInfected)
    print(pstr)
    if (0):
        params = Text(Point(xoffset+100, yoffset-80), pstr)
        params.setStyle('italic')
        params.setSize(20)
        params.draw(win)
        updateLabel()
        label.draw(win)

import threading

def startTimer():
    global numIter, curIter, window, numPeople
    # print("in timer: ", curIter, numIter, currentInfected)
    if ((curIter >= numIter) or (currentInfected <= 0) or (allStop)):
        endProgram()
        return
    curIter += 1
    for p in range(numPeople):
        persons[p].movePerson()
        persons[p].updateRecovery()
    for p1 in range(numPeople):
        for p2 in range(p1+1, numPeople):
            updateStatus(persons[p1], persons[p2])
    updateLabel()
    window.update()
    threading.Timer(0.3, startTimer).start()

def endProgram():
    global window
    printResults()

    # window.close()
    #QApplication.instance().quit()
    sys.exit(0)

def main():
    global window
    App = QApplication(sys.argv)
    window = Window()
    print('borders', gridsize, height, width, xoffset, yoffset, ll, lr, ul, ur)
    print('Day, Total Infected, Recovered, Dead, Current Infected, ICU Beds Available')
    for i in range(numPeople):
        persons.append(Person(i))
    window.InitWindow()
    # startTimer()
    sys.exit(App.exec_())
main()
