import numpy as np
from random import seed
from random import randint
from datetime import datetime

import sys
msize = int(sys.argv[1])
mnum = int(sys.argv[2])

def printarr(arr, h):
    return # not printing anything
    for i in range(h):
        print(arr[i])



def flips(size, maxnum):
    w = size
    h = size
    dt = datetime.now()
    sd = dt.microsecond
    seed(sd)
    arr = [[0 for x in range(w)] for y in range(h)]
    for i in range(w):
        for j in range(h):
            arr[i][j] = randint(-maxnum,maxnum)
    printarr(arr, h)
    #print(np.sum(arr,axis=1).tolist())
    #print(np.sum(arr,axis=0).tolist())

    flipped = 1
    ct = 0
    while (flipped):
        flipped = 0
        rsum = np.sum(arr,axis=1).tolist()
        for i in range(h):
            if (rsum[i] < 0):
                flipped = 1
                #print("flipping row ", i)
                ct += 1
                for j in range(w):
                    arr[i][j] *= -1
                break

        csum = np.sum(arr,axis=0).tolist()
        for i in range(w):
            if (csum[i] < 0):
                flipped = 1
                #print("flipping column ", i)
                ct += 1
                for j in range(h):
                    arr[j][i] *= -1
                break
        #print("&&&&&&&&&&&&")
        printarr(arr, h)
        #print(np.sum(arr,axis=0).tolist())
        #print(np.sum(arr,axis=1).tolist())


    printarr(arr, h)
    #print(np.sum(arr,axis=0).tolist())
    #print(np.sum(arr,axis=1).tolist())
    return ct

i = 10
iter = 5
while (i < msize):
    ct = 0
    for j in range(iter):
        ct += flips(i, mnum)
    print(str(i) + "   " + str(ct / iter))
    i += 10
