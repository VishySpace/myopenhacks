import numpy as np
import scipy.optimize as sp

size = 10

# input is position (x,y) of coin count with (0,0) as origin
# x down and y right
inputarr = [
    [0, 0, 1],
    [0, 2, 0],
    [0, 3, 2],
    [0, 8, 1],
    [1, 5, 3],
    [1, 7, 3],
    [1, 8, 3],
    [2, 2, 2],
    [2, 7, 2],
    [3, 0, 0],
    [3, 2, 2],
    [3, 4, 3],
    [4, 1, 1],
    [4, 8, 0],
    [5, 3, 3],
    [5, 4, 2],
    [5, 6, 0],
    [6, 2, 3],
    [6, 3, 2],
    [6, 9, 2],
    [7, 0, 2],
    [7, 6, 3],
    [7, 8, 5],
    [8, 5, 2],
    [8, 7, 4],
    [9, 1, 3],
    [9, 3, 2],
    [9, 8, 3]
]
print(len(inputarr))
matrixsize = size * size - len(inputarr)
matrix = np.zeros([len(inputarr), matrixsize])
indexmatrix = np.ones((size, size))
reverseindex = np.zeros([matrixsize, 2])

for t in inputarr:
    index_x = t[0]
    index_y = t[1]
    indexmatrix[index_x][index_y] = 0

indexmatrixcopy = np.copy(indexmatrix)

print(indexmatrix)

for i in range(size):
    for j in range(size):
        if (j != 0):
            indexmatrix[i, j] += indexmatrix[i, j - 1]
        else:
            if (i != 0):
                indexmatrix[i, j] += indexmatrix[i - 1, size - 1]

print(indexmatrix)

b = np.zeros(len(inputarr))

index = 0
for t in inputarr:
    index_x = t[0]
    index_y = t[1]
    sum_xy = t[2]
    b[index] = sum_xy
    # for index_x, index_y in np.ndindex(size,size):
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if (i == 0 and j == 0):
                continue
            index_x2 = index_x + i
            index_y2 = index_y + j
            if (index_x2 < 0 or index_x2 >= size):
                continue
            if (index_y2 < 0 or index_y2 >= size):
                continue

            if (indexmatrixcopy[index_x2, index_y2] == 0.0):
                continue
            index_y3 = indexmatrix[index_x2, index_y2] - 1
            matrix[index, int(index_y3)] = 1
            reverseindex[int(index_y3)][0] = index_x2
            reverseindex[int(index_y3)][1] = index_y2
    index += 1

print(matrix, b)

c = np.ones(matrixsize)
# c = np.multiply(c,-1)
result = sp.linprog(c, None, None, matrix, b, (0, 1), 'revised simplex')
print(result.fun)
print(result.x)

resultmatrix = np.zeros([size, size])
onescount = 0
for i in range(len(result.x)):
    if (result.x[i] > 0.9999):
        onescount += 1
        resultmatrix[int(reverseindex[i][0])][int(reverseindex[i][1])] = 1

print(onescount)
print(resultmatrix)