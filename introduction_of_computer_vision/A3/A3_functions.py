import numpy as np
import cv2
import math
import time

def deleteM(M):
    idx = []
    for i in range(len(M)):
        if abs(M[i][1]-M[i][3])>=5:
            idx.append(i)
        elif abs(M[i][0]-M[i][2])>30:
            idx.append(i)
    idx.sort(reverse=True)
    for i in idx:
        M = np.delete(M, i, axis=0)
    return M


def drawline(img, lines):
    r,c,d = img.shape
    color = ((255,0,0),(0,255,0),(0,0,255))
    n=0
    for l in lines:
        x0, y0 = map(int, [0, -l[2]/l[1]])
        x1, y1 = map(int, [c, -(l[2]+l[0]*c)/l[1]])
        cv2.line(img, (x0,y0), (x1,y1), color[n], 1)
        n+=1
    return img
