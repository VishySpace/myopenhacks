
import math
from random import seed
from random import randint
import sys
from math import sqrt

def is_square(n):
    return sqrt(n).is_integer()

# seed random number generator
seed(1)
# generate some integers
mysquares = []
circle = []
used = []
ct = 0

def calculateMySquares(k, n):
    arr = []
    for i in range(1, n+1):
        if (i != k):
            x = i + k
            if (is_square(x)):
                arr.append(i)
    mysquares.append(arr)

def fillCircle(pos, n):
    global ct
    curnum = circle[pos-1]
    # print("fillCircle", pos, curnum, circle)
    if (pos == n):
        if is_square(circle[pos-1] + circle[0]):
            # print(circle)
            ct += 1
        return 0
    for sq in mysquares[curnum-1]:
        if (used[sq-1]):
            continue
        circle[pos] = sq
        used[sq-1] = 1
        if fillCircle(pos+1, n):
            return 1
        circle[pos] = 0
        used[sq-1] = 0
    return 0

def fn(n):
    if ((n == 1) or (n == 3)):
        return n
    if (n%2 == 0):
        x = n/2
        return fn(x)
    if ( (n-1)%4 == 0):
        x = (n-1)/4
        return 2*fn(2*x+1) - fn(x)
    if ( (n-3)%4 == 0):
        x = (n-3)/4
        return 3*fn(2*x+1) - 2*fn(x)
    print("woah ", n)
    return(-1)

def main():
    ct = 0.0
    for n in range(1, 100):
        ct += float(n**2)/3**n
        print(ct)
    print ct
    return
    from turtle import *
    color('red', 'blue')
    begin_fill()

    global ct
    ct = 0
    j = 0
    for i in range(1, 2022):
        if (fn(i) == i):
            ct += 1
            print(i, i-j)
            left((i-j)/2)
            forward(i/32)
            j = i

    print("---- ", ct)
    end_fill()
    exitonclick()
    return



    N = int(sys.argv[1])
    for n in range(1, N):
        # print(n)
        mysquares.clear()
        circle.clear()
        used.clear()

        for i in range(1, n+1):
            calculateMySquares(i, n)
            used.append(0)
            circle.append(0)
#        print(mysquares)
        circle[0] = 1
        used[0] = 1
        ct = 0
        fillCircle(1, n)
        if (ct > 0):
            print(n, (int) (ct/2))

main()
