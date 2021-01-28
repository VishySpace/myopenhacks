from curvesqt import *
import sys
from datetime import datetime

## PUZZLES ##############################

gridsize = 700

class Puzzle():
    def __init__(self):
        global gridsize
        self.entities = []
        self.cx = gridsize/2
        self.cy = gridsize/2
        self.fixedShapes = []

        self.allStop = 0 # stop rounds
        self.curIter = 0
        self.numIter = 1000

    def Entities(self):
        return self.entities

    def FixedShapes(self):
        return self.fixedShapes

    def iterate(self, num):
        for e in range(len(self.entities)):
            self.entities[e].move()

class island(Puzzle):
    # On a primitive island there live equal numbers of yellow bellied cowards and red bellied brave warriors.
    # They don't know their own type but can tell others types.
    # How do they pair up (with one yellow and one red) and head out to explore? Being primitive they can't count or communicate.
    def __init__(self):
        global gridsize, painter, fixedShapes
        Puzzle.__init__(self)
        self.islandRadius = (int) (gridsize / 3)
        self.numP = 40
        self.pspeed = 10
        trace = 0

        # Generate people
        self.entities = []
        self.redCircle = shapePerson(6, Qt.red)
        self.yellowCircle = shapePerson(6, Qt.yellow)
        self.blueCircle = shapePerson(6, Qt.blue)
        self.emptyCircle = shapeCircle(0, Qt.white)
        self.border = FixedEntity(shapeCircle(self.islandRadius, Qt.white), self.cx, self.cy, trace)
        self.sun = FixedEntity(self.emptyCircle, self.cx, self.cy, trace)
        self.fixedShapes.append(self.border)
        self.random = []

        # a fraction of them are shapeshifters: they shift color on each move!
        prando = 0

        for p in range(self.numP):
            r = randint(0,100)
            if (r < 50):
                c = self.redCircle
            else:
                c = self.blueCircle
            pa = 2*math.pi*random()
            pr = randint(0, self.islandRadius)
            px = self.cx + pr*math.cos(pa)
            py = self.cy + pr*math.sin(pa)
            self.entities.append(FollowerEntity(c, self.pspeed, px, py, None, 1, trace))
            self.random.append(randint(0,100) < prando)
            if (self.random[p]):
                self.entities[p].doHighlight()

    def iterate(self, iter):
        permutation = np.random.permutation(self.numP)
        for n0 in permutation:
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
                                (self.entities[minP1].y + self.entities[minP2].y)/2, 0)
                self.entities[n0].following = mid
                self.entities[n0].towards = (self.entities[minP1].shape.color == self.entities[minP2].shape.color)
            self.entities[n0].move()

# bugs crawling towards each other on a polygon
class bugs(Puzzle):
    def __init__(self, n):
        global gridsize
        Puzzle.__init__(self)
        self.sides = n
        size = gridsize/4
        speed = 6
        self.createPoly(self.cx, self.cy, size, speed, self.sides)

    def createPoly(self, cx, cy, size, speed, n):
        trace = 1
        redSquare = shapeSquare(10, Qt.red)
        pts = []
        for i in range(n):
            x = cx + size * math.cos(2 * math.pi * i / n)
            y = cy + size * math.sin(2 * math.pi * i / n)
            pts.append(QPointF(x, y))
            if (i > 0):
                self.entities.append(FollowerEntity(redSquare, speed, x, y, self.entities[i-1], 1, trace))
            else:
                self.entities.append(FollowerEntity(redSquare, speed, x, y, None, 1, trace))
        self.entities[0].following = self.entities[n-1]
        self.fixedShapes.append(FixedEntity(shapePoly(pts, Qt.white), 0, 0, trace))

class orbits(Puzzle):
    def __init__(self):
        global gridsize
        Puzzle.__init__(self)
        speed = 2
        n = 7
        radius = 100
        size = gridsize/4
        trace = 1

        blueCircle = shapeCircle(2, Qt.blue)
        redCircle = shapeCircle(2, Qt.red)
        greenCircle = shapeCircle(2, Qt.green)
        yCircle = shapeCircle(6, Qt.yellow)
        sun = FixedEntity(yCircle, self.cx, self.cy, trace)

        earthSpeed = 30 # 30KMPS
        moonSpeed = 30 #1.1 KMPS
        marsSpeed = 20
        rocketSpeed = 4
        earthRadius = 3 * radius # 1.5 * 10^8 KM
        moonRadius = radius / 4 # 3.48 * 10^5KM

        startAngle = 0
        self.entities = []
        self.entities.append(PolygonEntity(blueCircle, earthSpeed, startAngle, sun, 5, earthRadius, -50, trace))
        self.entities.append(EllipseEntity(redCircle, marsSpeed, startAngle, sun, earthRadius*2.5, earthRadius, -45, trace))
        self.entities.append(EllipseEntity(greenCircle, moonSpeed, startAngle, self.entities[0], moonRadius, moonRadius, 0, trace))
        self.entities.append(FunctionEntity(redCircle, speed, 100, 200, '50*sin(4*x*2*math.pi/360)**2', 50, 700, trace))
        self.entities.append(FollowerEntity(blueCircle, rocketSpeed, self.entities[0].x, self.entities[0].y, self.entities[1], 1, trace))
        self.entities.append(sun)
        self.entities[3].doHighlight()

    def iterate(self, num):
        for e in range(len(self.entities)):
            self.entities[e].move()

def main():
    App = QApplication(sys.argv)
    window = Window(gridsize)

    seed(datetime.now().microsecond)
    if (len(sys.argv) > 1):
        if (sys.argv[1] == 'orbits'):
            prob = orbits()
        elif (sys.argv[1] == 'bugs'):
            prob = bugs(5)
        else:
            prob = island()
    else:
        prob = island()
    window.InitWindow(prob)
    window.update()
    ## startTimer() <-- uncomment to auto start the program
    sys.exit(App.exec_())
main()
