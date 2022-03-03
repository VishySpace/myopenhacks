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
        self.connectors = []

        self.allStop = 0 # stop rounds
        self.curIter = 0
        self.numIter = 1000

    def handleCollisions(self, cols):
        if (len(cols) > 0):
            return
    def Entities(self):
        return self.entities

    def FixedShapes(self):
        return self.fixedShapes

    def Connectors(self):
        return self.connectors

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


# planes flying towards each other on a polygon
class planes(Puzzle):
    def __init__(self, n, speeds):
        global gridsize
        Puzzle.__init__(self)
        self.sides = n
        size = gridsize/4
        self.speeds = []
        self.entities = []
        self.angles = [30, 50, 270]
        self.nd = 0
        self.alldone = 0
        for i in range(n):
            self.speeds.append(speeds[i])

        self.createPoly(self.cx, self.cy, size, n)

    def createPoly(self, cx, cy, size, n):
        trace = 0
        redSquare = shapeSquare(1, Qt.red)
        blueSquare = shapeSquare(1, Qt.blue)
        pts = []
        minx = 1000
        miny = 1000
        maxx = 0
        maxy = 0
        for i in range(n):
            x = cx + size * math.cos(2 * math.pi * i / n)
            y = cy + size * math.sin(2 * math.pi * i / n)
            print(x, y)
            pts.append(QPointF(x, y))
            if (x > maxx):
                maxx = x
            if (y > maxy):
                maxy = y
            if (x <  minx):
                minx = x
            if (y < miny):
                miny = y
        self.fixedShapes.append(FixedEntity(shapePoly(pts, Qt.white, 2*size), 0, 0, trace))
        e = 0
        for i in range(floor(minx), floor(maxx)):
            for j in range(floor(miny), floor(maxy)):
                if ((i+j)%20 == 0):
                    e1 = FixedEntity(blueSquare, i, j, 0)
                    self.entities.append(e1)
                    e += 1
        print("num ", e)
        self.nd = e
        for j in range(e):
            for i in range(n):
                x = cx + size * math.cos(2 * math.pi * i / n)
                y = cy + size * math.sin(2 * math.pi * i / n)
                self.entities.append(FollowerEntity(redSquare, self.speeds[i], x, y, self.entities[j], 1, trace))
    def iterate(self, num):
        Puzzle.iterate(self, num)
        if (not self.alldone):
            for j in range(self.nd):
                done = 1
                n = self.sides
                for i in range(n):
                    if (not colliding(self.entities[j], self.entities[self.nd + j*n + i])):
                        done = 0
                if (done):
                    print("found a solution! at ", j, (self.entities[j].x - self.cx)*4.0/gridsize, (self.entities[j].y - self.cy)*4.0/gridsize)
                    self.alldone = 1
                    break
            if (self.alldone):
                redSquare = shapeSquare(3, Qt.red)
                blueSquare = shapeSquare(3, Qt.blue)
                dx = self.entities[j].x
                dy= self.entities[j].y
                self.entities.clear()
                e1 = FixedEntity(blueSquare, dx, dy, 0)
                self.entities.append(e1)
                size = gridsize / 4
                for i in range(n):
                    x = self.cx + size * math.cos(2 * math.pi * i / n)
                    y = self.cy + size * math.sin(2 * math.pi * i / n)
                    self.entities.append(FollowerEntity(redSquare, self.speeds[i], x, y, self.entities[0], 1, 1))

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
        self.fixedShapes.append(FixedEntity(shapePoly(pts, Qt.white, 2*size), 0, 0, trace))

    def iterate(self, num):
        # connectors
        Puzzle.iterate(self, num)
        for i in range(self.sides):
            if (i > 0):
                j = i-1
            else:
                j = self.sides -1
            self.connectors.append({"e1": {"x": self.entities[i].x, "y": self.entities[i].y}, \
                            "e2": {"x": self.entities[j].x, "y": self.entities[j].y}})

# Blue Neutron collides into Uranium -> Creates Barium, Krypton, and 2 other neutrons which can
# then blast other Uranium atoms. Hence exponential fission or chain reaction.
class collider(Puzzle):
    def __init__(self):
        global gridsize
        Puzzle.__init__(self)
        pumpwidth = 20
        self.neutronspeed = 10
        numNeutrons = 10
        numUranium = 100
        self.entities = []
        self.redCircle = shapeCircle(6, Qt.red)
        self.yellowCircle = shapeCircle(10, Qt.yellow)
        self.greenCircle = shapeCircle(3, Qt.green)
        self.blueCircle = shapeCircle(2, Qt.blue)
        self.blackBox = shapeSquare(40, Qt.black)
        numBlockers = 2
        for i in range(numUranium):
            e1 = FixedEntity(self.redCircle, randint(int(gridsize/3), int(2*gridsize/3)), randint(int(gridsize/3), int(2*gridsize/3)), 0)
            self.entities.append(e1)

        for i in range(numBlockers):
            e1 = BoundedBoxEntity(self.blackBox, 0, randint(0, gridsize), randint(0, gridsize), \
                    0, 0, gridsize, gridsize, 0, 0)
            self.entities.append(e1)

        for i in range(numNeutrons):
            e1 = BoundedBoxEntity(self.blueCircle, self.neutronspeed, gridsize/2, gridsize/2, \
                    0, 0, gridsize, gridsize, 0, 0)
            self.entities.append(e1)



    def isNeutron(self, e1):
        return (e1.shape.color == Qt.blue)

    def isUranium(self, e1):
        return (e1.shape.color == Qt.red)

    def iterate(self, num):
        for e in range(len(self.entities)):
            self.entities[e].move()
        c = detectCollisions(self.entities)
        remList = []
        cl = len(c)
        for i in range(cl):
            e1 = self.entities[c[i]['e1']]
            e2  = self.entities[c[i]['e2']]
            if (e1.shape.color == Qt.black):
                e2.bounce()
                continue
            if ( (self.isNeutron(e1) and self.isUranium(e2)) or (self.isUranium(e1) and self.isNeutron(e2))):
                # remove Red. add 2 Green. add another Blue.
                neu = BoundedBoxEntity(self.blueCircle, 2*self.neutronspeed, e1.x, e1.y, \
                                            0, 0, gridsize, gridsize, 0, 0)
                g1 =  FixedEntity(self.greenCircle, e1.x-3, e1.y-3, 0)
                g2 = FixedEntity(self.greenCircle, e1.x+3, e1.y+3, 0)
                g3 = FixedEntity(self.yellowCircle, e1.x, e1.y, 0)
                if (self.isUranium(e2)):
                    re = c[i]['e2']
                else:
                    re = c[i]['e1']
                if (not (re in remList)):
                    remList.append(re)
                self.entities.append(neu)
                self.entities.append(g3)
                self.entities.append(g1)
                self.entities.append(g2)
        rl = len(remList)
        for r in reversed(remList):
            self.entities.pop(r)

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

        earthSpeed = 10 # 30KMPS
        moonSpeed = 15 #1.1 KMPS
        marsSpeed = 20
        rocketSpeed = 4
        earthRadius = 1.5 * radius # 1.5 * 10^8 KM
        moonRadius = radius / 4 # 3.48 * 10^5KM

        startAngle = 0
        self.entities = []
        self.entities.append(PolygonEntity(blueCircle, earthSpeed, startAngle, sun, 5, earthRadius, -50, trace))
        self.entities.append(EllipseEntity(redCircle, marsSpeed, startAngle, sun, earthRadius*2.5, earthRadius, -45, trace))
        self.entities.append(BoundedBoxEntity(redCircle, 10, 300, 400, 180, 180, 320, 480, 0, 0))
        self.entities.append(EllipseEntity(greenCircle, moonSpeed, startAngle, self.entities[0], moonRadius, moonRadius, 0, trace))
        self.entities.append(FunctionEntity(redCircle, speed, 100, 200, '50*sin(4*x*2*math.pi/360)**2', 700, trace))
        self.entities.append(FollowerEntity(blueCircle, 10, self.entities[0].x, self.entities[0].y, self.entities[2], 1, trace))
        self.entities.append(sun)


def main():
    App = QApplication(sys.argv)
    window = Window(gridsize)

    seed(datetime.now().microsecond)
    if (len(sys.argv) > 1):
        if (sys.argv[1] == 'orbits'):
            prob = orbits()
        elif (sys.argv[1] == 'bugs'):
            prob = bugs(5)
        elif (sys.argv[1] == 'collider'):
            prob = collider()
        elif (sys.argv[1] == 'planes'):
            prob = planes(5, [2, 2, 4, 4, 4])
        else:
            prob = island()
    else:
        prob = island()
    window.InitWindow(prob)
    window.update()
    ## startTimer(prob, window) <-- uncomment to auto start the program
    sys.exit(App.exec_())
main()
