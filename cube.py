import sys
size = int(sys.argv[1])
pcube = size**3
psqr = size**2
debug = 0
cubes = 0
steps = 0
numTilted = 0

def parallel(v1, v2, v3, v4):
class Cube(object):
    def __init__(self, v1, v2, v3, v4):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
        self.v4 = v4
        len = v1.SideLength(v2)

    def translated(self, c2) :
        if (self.len != c2.len):
            return 0
        if (parallel(self.v1, self.v2, v1, v2) or parallel(self.v1, self.v3, v1, v2) or parallel(self.v1, self.v4, v1, v2):
            return 1
        return 0

class Vertex(object):
    def __init__(self, x1, y1, z1):
        self.x = x1
        self.y = y1
        self.z = z1
    def fromIdx(cls, idx):
        az = (int) (idx / psqr)
        idx = idx % psqr
        ay = (int) (idx / size)
        idx = idx % size
        ax = idx
        return cls(ax, ay, az)

    def print(self, str):
        print ("%(pref)s: %(posn)s" % {"pref": str, "posn": (self.x, self.y, self.z)})
    def Shifted(self, pt):
        return Vertex(self.x-pt.x, self.y-pt.y, self.z-pt.z)
    def add(self, pt):
        return Vertex(self.x+pt.x, self.y+pt.y, self.z+pt.z)

    def SideLength(self, pt):
        return((self.x-pt.x)**2 + (self.y-pt.y)**2 + (self.z-pt.z)**2)

    def InCube(self):
        return (((self.x >= 0) and (self.x < size)) and ((self.y >= 0) and (self.y < size))and ((self.z >= 0) and (self.z < size)))
    def tilted(self, pt):
        if ((self.x == pt.x) and (self.y == pt.y)):
             return 0;
        if ((self.x == pt.x) and (self.z == pt.z)):
             return 0;
        if ((self.z == pt.z) and (self.y == pt.y)):
             return 0;
        return 1;

    def formsCube(self, pt2, pt3, pt4):
        # shift all to origin
        global numTilted
        if (debug):
            pt1.print("checking for cube!")
            pt2.print("")
            pt3.print("")
            pt4.print("")
        side2 = pt1.SideLength(pt2)
        side3 = pt1.SideLength(pt3)
        side4 = pt1.SideLength(pt4)
        if ((side2 != side3) or (side2 != side4)):
            if (debug):
                print("lengths did not match", side2, side3, side4)
            return 0
        # FIX THIS TO 1
        if (side2 < 1):
            return 0
        spt1 = self.Shifted(self)
        spt2 = pt2.Shifted(self)
        spt3 = pt3.Shifted(self)
        spt4 = pt4.Shifted(self)


        #if (side2 > 1):
        #    spt1.print("same length")
        #    spt2.print("")
        #    spt3.print("")
        #    spt4.print("")
        if ((not perpendicular(spt2, spt3)) or (not perpendicular(spt2, spt4))):
            if (debug):
                print("not perp")
            return 0
        # now check that the remaining 4 vertices are in the cube
        pt5 = spt2.add(spt3).add(self)
        if (not pt5.InCube()):
            if (debug):
                pt5.print("5 not in cube")
            return 0;
        pt6 = spt2.add(spt4).add(self)
        if (not pt6.InCube()):
             if (debug):
                 pt6.print("6 not in cube")
             return 0;
        pt7 = spt3.add(spt4).add(self)
        if (not pt7.InCube()):
             if (debug):
                 pt7.print("7 not in cube")
             return 0;
        pt8 = spt2.add(spt3).add(spt4).add(self)
        if (not pt8.InCube()):
             if (debug):
                 pt8.print("8 not in cube")
             return 0;

        if (pt1.tilted(pt2) or pt1.tilted(pt3) or pt1.tilted(pt4)):
            if (debug) :
                print("****** We got Tilt!")
                pt1.print("forms cube!")
                pt2.print("")
                pt3.print("")
                pt4.print("")
                pt5.print("computed!")
                pt6.print("")
                pt7.print("")
                pt8.print("")
                print("size = " + str(side2))
            numTilted += 1
        return 1
def perpendicular(pt1, pt2):
    dotp = ((pt1.x * pt2.x) + (pt1.y * pt2.y) + (pt1.z * pt2.z))
    # print("dotp", dotp)
    return (dotp == 0)

# print("number of points", size)
cubes = 0
for i1 in range(size):
    cubes += i1**3
for i1 in range(pcube):
    pt1 = Vertex.fromIdx(Vertex, i1)
    # pt1.print("pt1")
    steps += 1
    spt1 = pt1.Shifted(pt1)
    for i2 in range(i1+1, pcube):
        steps += 1
        pt2 = Vertex.fromIdx(Vertex,i2)
        # pt2.print("pt2")
        l2 = pt1.SideLength(pt2)
        if (l2 <= 1):
            continue;
        #if (not pt1.tilted(pt2)):
        #    continue
        spt2 = pt2.Shifted(pt1)
        for i3 in range(i2+1, pcube):
            steps += 1
            pt3 = Vertex.fromIdx(Vertex,i3)
            # pt3.print("pt3")
            l3 = pt1.SideLength(pt3)
            if (l2 != l3):
                continue
            spt3 = pt3.Shifted(pt1)
            if (not perpendicular(spt2, spt3)):
                continue
            pt5 = spt2.add(spt3).add(pt1)
            if (not pt5.InCube()):
                continue
            #if (not pt1.tilted(pt3)):
            #    continue
            for i4 in range(i3+1, pcube):
                steps += 1
                pt4 = Vertex.fromIdx(Vertex, i4)
                l4 = pt1.SideLength(pt4)
                if (l2 != l4):
                    continue
                spt4 = pt4.Shifted(pt1)
                if (not perpendicular(spt2, spt4)):
                    continue
                #if (not pt1.tilted(pt4)):
                #    continue
                if (pt1.formsCube(pt2, pt3, pt4)):
                    steps+= 1

print("stats (size, points, steps, reg cubes, tilted) ", size, pcube, steps, cubes, numTilted)
