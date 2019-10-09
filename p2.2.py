import math
import random
import time

def bruteSolution(PairPointA):
    Alen = len(PairPointA)
    minDist = getDistance(PairPointA[0], PairPointA[1])
    colsestPair = (PairPointA[0], PairPointA[1])
    for i in range(0, Alen-2):
        for j in range(i+1, Alen-1):
            dist = getDistance(PairPointA[i], PairPointA[j])
            if minDist > dist:
                minDist = dist
                colsestPair = (PairPointA[i], PairPointA[j])
    return colsestPair, minDist

def getDistance(point1, point2):
    return math.sqrt((point1[0] - point2[0])*(point1[0] - point2[0]) + (point1[1] - point2[1])*(point1[1] - point2[1]))

def midAreaMin(sAX, sAY, delta):
    midXvalue = sAX[len(sAX)//2][0]
    sAYdelta = []
    for point in sAY:
        if midXvalue - delta <= point[0] <= midXvalue + delta:
            sAYdelta.append(point)
    if len(sAYdelta) <= 1:
        return ((0, 0), (0, 0)), (delta + 1)#return a distance bigger than delta to ignore this case
    minDist = getDistance(sAYdelta[0], sAYdelta[1])
    colsestPair = (sAYdelta[0], sAYdelta[1])
    for i in range(0, len(sAYdelta)-2):
        for j in range(i+1, len(sAYdelta)-1):
            if sAYdelta[j][1] <= sAYdelta[i][1] + delta:
                dist = getDistance(sAYdelta[i], sAYdelta[j])
            else:
                dist = delta + 1
            if minDist > dist:
                minDist = dist
                colsestPair = (sAYdelta[i], sAYdelta[j])
    return colsestPair, minDist

def findColsestPairPoint(sAX, sAY):
    if len(sAX) <= 3:
        colsestPair, minDist = bruteSolution(sAX)
        return colsestPair, minDist
    else:
        #divide
        midx = len(sAX)//2
        sAXl = sAX[0: midx]
        sAXr = sAX[midx:]
        sAYl, sAYr = [], []
        midXvalue = sAX[midx][0]
        for point in sAY:
            if point[0] < midXvalue:
                sAYl.append(point)
            else:
                sAYr.append(point)
        #recursive
        colsestPairL, minDistL = findColsestPairPoint(sAXl, sAYl)
        colsestPairR, minDistR = findColsestPairPoint(sAXr, sAYr)
        #merge
        if minDistL < minDistR:
            minDist = minDistL
            colsestPair = colsestPairL
        else:
            minDist = minDistR
            colsestPair = colsestPairR
        colsestPairM, minDistM = midAreaMin(sAX, sAY, minDist)
        if minDist > minDistM:
            minDist = minDistM
            colsestPair = colsestPairM
    return colsestPair, minDist

AX = []
AY = []
for i in range(1, 10000):
    AX.append(random.randint(0, 100000))
    AY.append(random.randint(0, 100000))
PairPointA = list(zip(AX, AY))
sAX = sorted(PairPointA, key = lambda point: point[0])
sAY = sorted(PairPointA, key = lambda point: point[1])
start = time.time()
colsestPair, minDist = findColsestPairPoint(sAX, sAY)
end = time.time()
print('closest pair point is :%s\nthe distance is :%s\ntime: %s s' %(colsestPair, minDist, (end-start)))